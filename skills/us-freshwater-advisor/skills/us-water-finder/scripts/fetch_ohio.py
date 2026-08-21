#!/usr/bin/env python3
"""
fetch_ohio.py — Mode A (FIND) data source for Ohio.

Written via Mode E (EXPAND) on 2026-08-20. Queries Ohio DNR's Division of Watercraft
"Stream Access (All Fields)" FeatureServer for river/stream access points near a
given point. No API key needed.

IMPORTANT — this is NOT the same kind of layer as Indiana's Fish_Access_RO or
Michigan's boating-access FeatureServer:
  - It is a Division of WATERCRAFT paddling/canoe-access layer (streams/rivers
    only), not a Division of Wildlife fishing-access layer. Ohio does not have a
    confirmed dedicated statewide fishing-access-point feed at time of writing
    (see SKILL.md's data-sources table and this state's ohio.json known_gaps).
  - It covers stream/river put-ins, not lake/reservoir shoreline access or boat
    ramps on lakes. Many entries are portage points around low-head dams, not
    fishing spots per se — the FEATURE text says what it actually is; don't
    assume "found near your point" means "good bank fishing here."
  - Field coverage flags (LAUNCHRAMP/CAMPING/RESTROOM/etc.) use 1 / 0 / -1
    (yes / no / unknown), not booleans — treat -1 as "not recorded," not "no."
  - maxRecordCount on this service is 1000; a broad query can silently truncate
    (exceededTransferLimit: true in the raw response) — always filter by county
    or a tight radius rather than pulling statewide.

Usage:
    python3 fetch_ohio.py --lat 39.9612 --lon -82.9988 --radius-mi 30 --json out.json
    python3 fetch_ohio.py --waterbody "Scioto River" --json out.json
    python3 fetch_ohio.py --county Franklin --json out.json
"""
import argparse
import json
import math
import sys
import urllib.parse
import http.client
import time
import urllib.error
import urllib.request

FEATURE_SERVER = (
    "https://gis2.ohiodnr.gov/arcgis/rest/services/DWC_Services/"
    "Watercraft_Paddling_Query/FeatureServer/0/query"
)

FIELDS = [
    "WATERWAY", "FEATURE", "COUNTY", "LAT", "LONG_", "HAZARD",
    "PARKLOT", "ROADPARK", "BOATRENTAL", "LAUNCHRAMP", "CAMPING",
    "RESTROOM", "PICNIC", "DRINKINGWATER", "FOOD", "BIKETRAIL", "ADA",
]

# This service has no server-side distance/geometry filter parameter confirmed
# working in Mode E testing (2026-08-20) — unlike Indiana/Michigan's FeatureServers,
# radius search here is done client-side after a where-clause query, using a plain
# equirectangular approximation (fine at this distance scale, not geodesically exact).
def haversine_mi(lat1, lon1, lat2, lon2):
    r = 3958.8
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlmb = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlmb / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def maps_url(lat, lon):
    """Google Maps link so a result can be handed to the person as a place to go,
    not just a name and a species list."""
    if lat is None or lon is None:
        return None
    return f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"


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


def query(where="1=1", result_count=1000):
    params = {
        "where": where,
        "outFields": ",".join(FIELDS),
        "returnGeometry": "false",
        "f": "json",
        "resultRecordCount": str(result_count),
    }
    url = FEATURE_SERVER + "?" + urllib.parse.urlencode(params)
    data = _http_get(url, "the Ohio DNR FeatureServer")
    if "error" in data:
        raise RuntimeError(f"Ohio FeatureServer error: {data['error']}")
    if "features" not in data:
        raise SystemExit(
            "The Ohio FeatureServer returned a 200 but no 'features' key — found: "
            + (", ".join(sorted(data.keys())[:12]) or "nothing")
            + ". The layer may have been moved, renamed or retired. Report this as a "
              "source problem, not as 'no access points found', and log it to "
              "friction-log.md — it needs a script fix, not a retry."
        )
    truncated = data.get("exceededTransferLimit", False)
    return [f["attributes"] for f in data.get("features", []) if isinstance(f, dict) and "attributes" in f], truncated


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lat", type=float)
    ap.add_argument("--lon", type=float)
    ap.add_argument("--radius-mi", type=float, default=30.0)
    ap.add_argument("--waterbody", type=str, help="filter by waterway name (contains match)")
    ap.add_argument("--county", type=str, help="filter by Ohio county name (exact match)")
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--json", type=str, required=True)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    truncated = False
    if args.waterbody:
        safe = args.waterbody.replace("'", "''")
        results, truncated = query(where=f"WATERWAY LIKE '%{safe}%'")
    elif args.county:
        safe = args.county.replace("'", "''")
        results, truncated = query(where=f"COUNTY = '{safe}'")
    elif args.lat is not None and args.lon is not None:
        # No server-side geometry filter confirmed for this service — pull broadly
        # is not viable statewide (1000-row cap), so this path requires --county or
        # --waterbody in practice; kept here for API symmetry with Indiana/Michigan
        # and for small radii where a full unfiltered pull still fits under the cap.
        all_results, truncated = query(where="1=1", result_count=1000)
        results = [
            r for r in all_results
            if r.get("LAT") and r.get("LONG_")
            and haversine_mi(args.lat, args.lon, r["LAT"], r["LONG_"]) <= args.radius_mi
        ]
        results.sort(key=lambda r: haversine_mi(args.lat, args.lon, r["LAT"], r["LONG_"]))
        results = results[: args.limit]
    else:
        print("Provide --lat/--lon/--radius-mi, --waterbody, or --county", file=sys.stderr)
        sys.exit(1)

    for r in results:
        r["maps_url"] = maps_url(r.get("LAT"), r.get("LONG_"))

    out = {
        "source": "Ohio DNR Division of Watercraft Stream Access (Watercraft_Paddling_Query) FeatureServer",
        "note": (
            "Stream/river paddling-access points only (Division of Watercraft), NOT a "
            "confirmed statewide fishing-access-point layer (Division of Wildlife has "
            "none confirmed as of this Mode E pass). Lake/reservoir shoreline access is "
            "not covered by this feed. Added via Mode E on 2026-08-20 — unverified "
            "against a second pass; see reference-data/states/ohio.json."
        ),
        "query": {
            "lat": args.lat, "lon": args.lon, "radius_mi": args.radius_mi,
            "waterbody": args.waterbody, "county": args.county,
        },
        "possibly_truncated": truncated,
        "count": len(results),
        "sites": results,
    }
    with open(args.json, "w") as f:
        json.dump(out, f, indent=2)
    if not args.quiet:
        print(f"{len(results)} site(s) written to {args.json}" + (" (source query hit row cap — results may be incomplete)" if truncated else ""))


if __name__ == "__main__":
    main()
