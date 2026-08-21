#!/usr/bin/env python3
"""
fetch_michigan.py — Mode A (FIND) data source for Michigan.

Queries Michigan DNR's authoritative, actively-maintained Boating/Fishing Access
Sites FeatureServer (MRBIS — Michigan Recreational Boating Information System) for
access points near a given point. No API key needed.

Note: this is a boating-access-focused layer (ramps, piers, parking, toilets) —
it's the best confirmed public GPS/access dataset for Michigan, but it is NOT the
same shape as Indiana's "Fish_Access_RO" layer (no species/fee fields here). Treat
missing fields as "not in this dataset," not "doesn't exist."

Usage:
    python3 fetch_michigan.py --lat 42.9634 --lon -85.6681 --radius-mi 30 --json out.json
    python3 fetch_michigan.py --waterbody "Gun Lake" --json out.json
"""
import argparse
import json
import sys
import urllib.parse
import http.client
import time
import urllib.error
import urllib.request

FEATURE_SERVER = (
    "https://services3.arcgis.com/Jdnp1TjADvSDxMAX/arcgis/rest/services/"
    "DNR_State_Sponsored_Developed_Boating_Access_Sites_Public_View/FeatureServer/0/query"
)

FIELDS = [
    "name", "LABELNAME", "waterbody", "WaterbodyType", "BAS_Type", "DESCRIP",
    "OWNEDBY", "ADMINBY", "MAINTBY", "nLanes", "CarryDown", "nPiers",
    "nTrailerableParking", "nVehicleOnlyParking",
    "nVaultToilets", "nFlushToilets", "nOtherToilets",
    "County", "Latitude", "Longitude",
]


def _http_get(req_or_url, source, timeout=20, retries=2):
    """Fetch JSON, retrying transient failures, and fail with a readable message.

    Before 2026-08-21 none of these scripts caught network errors at all: a USGS 503 or a
    NOAA rate-limit surfaced as a raw Python traceback, which is what a real session would
    have shown the user. Transient server-side failures (5xx, 429, timeouts) are worth a
    short retry; a 4xx means the request itself is wrong and retrying only wastes time.
    """
    transient = (408, 429, 500, 502, 503, 504)
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req_or_url, timeout=timeout) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code in transient:
                if attempt < retries:
                    time.sleep(2 ** attempt)
                    continue
                raise SystemExit(
                    f"{source} returned HTTP {e.code} after {retries + 1} attempts. "
                    f"That is a server-side failure, not a problem with the query — it is "
                    f"usually temporary. Do NOT report this as 'no data found': data may "
                    f"well exist. Say the source is unreachable right now and suggest "
                    f"retrying in a few minutes."
                )
            raise SystemExit(
                f"{source} rejected the request with HTTP {e.code} ({e.reason}). This "
                f"usually means the query is wrong (bad station/site ID, malformed "
                f"parameters, or the API changed) rather than the service being down."
            )
        except (OSError, http.client.HTTPException) as e:
            # Deliberately broad. urllib surfaces transport failures as URLError,
            # TimeoutError, ConnectionResetError and http.client.RemoteDisconnected,
            # and those do NOT share one narrow base class — catching URLError alone
            # let a dropped connection through as a raw traceback (found in testing,
            # 2026-08-21). HTTPError is handled above and must stay above this, since
            # it is itself a URLError/OSError subclass.
            if attempt < retries:
                time.sleep(2 ** attempt)
                continue
            detail = getattr(e, "reason", None) or e
            raise SystemExit(
                f"Could not reach {source} after {retries + 1} attempts: {detail}. "
                f"Treat this as temporarily unreachable, NOT as an empty result — never "
                f"report 'no data found' on a connection failure."
            )
        except json.JSONDecodeError:
            raise SystemExit(
                f"{source} returned something that isn't valid JSON — most likely an error "
                f"page instead of data. The endpoint may have changed."
            )


def query(where="1=1", geometry=None, distance_m=None, result_count=25):
    params = {
        "where": where,
        "outFields": ",".join(FIELDS),
        "returnGeometry": "false",
        "f": "json",
        "resultRecordCount": str(result_count),
    }
    if geometry:
        params.update({
            "geometry": f"{geometry[0]},{geometry[1]}",
            "geometryType": "esriGeometryPoint",
            "inSR": "4326",
            "outSR": "4326",
            "distance": str(distance_m),
            "units": "esriSRUnit_Meter",
        })
    url = FEATURE_SERVER + "?" + urllib.parse.urlencode(params)
    data = _http_get(url, "the Michigan DNR FeatureServer")
    if "error" in data:
        raise RuntimeError(f"Michigan FeatureServer error: {data['error']}")
    if "features" not in data:
        raise SystemExit(
            "The Michigan FeatureServer returned a 200 but no 'features' key — found: "
            + (", ".join(sorted(data.keys())[:12]) or "nothing")
            + ". The layer may have been moved, renamed or retired. Report this as a "
              "source problem, not as 'no access points found', and log it to "
              "friction-log.md — it needs a script fix, not a retry."
        )
    return [f["attributes"] for f in data.get("features", []) if isinstance(f, dict) and "attributes" in f]


def maps_url(lat, lon):
    """Google Maps link so a result can be handed to the person as a place to go,
    not just a name and a species list."""
    if lat is None or lon is None:
        return None
    return f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lat", type=float)
    ap.add_argument("--lon", type=float)
    ap.add_argument("--radius-mi", type=float, default=30.0)
    ap.add_argument("--waterbody", type=str, help="filter by waterbody name (contains match)")
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--json", type=str, required=True)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if args.waterbody:
        safe = args.waterbody.replace("'", "''")
        results = query(where=f"waterbody LIKE '%{safe}%'", result_count=args.limit)
    elif args.lat is not None and args.lon is not None:
        distance_m = args.radius_mi * 1609.34
        results = query(geometry=(args.lon, args.lat), distance_m=distance_m, result_count=args.limit)
    else:
        print("Provide either --lat/--lon/--radius-mi or --waterbody", file=sys.stderr)
        sys.exit(1)

    for r in results:
        r["maps_url"] = maps_url(r.get("Latitude"), r.get("Longitude"))

    out = {
        "source": "Michigan DNR Boating/Fishing Access Sites (MRBIS) FeatureServer",
        "note": "Access-point/amenity data only. Regulations (closed seasons, size/bag "
                "limits) are NOT in this feed — see references/michigan-regulations.md.",
        "query": {
            "lat": args.lat, "lon": args.lon, "radius_mi": args.radius_mi,
            "waterbody": args.waterbody,
        },
        "count": len(results),
        "sites": results,
    }
    with open(args.json, "w") as f:
        json.dump(out, f, indent=2)
    if not args.quiet:
        print(f"{len(results)} site(s) written to {args.json}")


if __name__ == "__main__":
    main()
