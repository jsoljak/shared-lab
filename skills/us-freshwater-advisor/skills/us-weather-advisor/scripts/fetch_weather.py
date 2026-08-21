#!/usr/bin/env python3
"""
fetch_weather.py — weather layer for us-weather-advisor.

Pulls NOAA/NWS forecast (daily periods, including overnight — needed for CAMP mode)
for a given GPS point. No API key needed, but NOAA requires a descriptive User-Agent
identifying the application (not a browser string) — see their API usage policy.

Usage:
    python3 fetch_weather.py --lat 39.7684 --lon -86.1581 --json out.json
"""
import argparse
import json
import http.client
import time
import urllib.error
import urllib.request

# NOAA's API usage policy asks for a real contact so they can reach you if this
# script misbehaves. REPLACE THE EMAIL BELOW WITH YOUR OWN before real use — a
# placeholder here risks NOAA rate-limiting or blocking requests down the line.
# Written without an "@" on purpose: an email-shaped placeholder trips
# repository secret scanners, which read it as a real leaked address.
USER_AGENT = "us-weather-advisor (contact: PUT-YOUR-EMAIL-ADDRESS-HERE)"


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


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/geo+json"})
    return _http_get(req, "the NOAA/NWS API")


def _dig(data, path, source, hint=""):
    """Walk a nested key path, failing with an explanation instead of a KeyError.

    A successful HTTP fetch can still return a shape this script doesn't expect — an
    API redesign, a deprecation notice served as JSON, or an error object delivered
    with a 200. Before 2026-08-21 that surfaced as a bare KeyError traceback, which
    to the user is indistinguishable from the script being broken. Network failures
    are handled in _http_get; this covers the other half of the same failure class.
    """
    node = data
    walked = []
    for key in path:
        if not isinstance(node, dict) or key not in node:
            where = " -> ".join(walked) if walked else "(top level)"
            if isinstance(node, dict):
                found = ", ".join(sorted(node.keys())[:12]) or "nothing"
            else:
                found = f"a {type(node).__name__}, not an object"
            raise SystemExit(
                f"{source} responded, but not in the shape this script expects: no "
                f"'{key}' under {where}. Found instead: {found}. That usually means the "
                f"API changed its response format, or returned an error object with a "
                f"success status. {hint} "
                f"Report this as a problem with the source, NOT as 'no data found' — and "
                f"it is worth writing to friction-log.md, since it needs a script fix "
                f"rather than a retry."
            )
        walked.append(key)
        node = node[key]
    return node


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lat", type=float, required=True)
    ap.add_argument("--lon", type=float, required=True)
    ap.add_argument("--json", type=str, required=True)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    NWS = "The NOAA/NWS API"
    HINT = "See api.weather.gov for the current documented response format."

    points = fetch(f"https://api.weather.gov/points/{args.lat},{args.lon}")
    props = _dig(points, ["properties"], NWS, HINT)
    forecast_url = _dig(points, ["properties", "forecast"], NWS, HINT)
    hourly_url = _dig(points, ["properties", "forecastHourly"], NWS, HINT)

    forecast = fetch(forecast_url)
    hourly = fetch(hourly_url)

    periods = _dig(forecast, ["properties", "periods"], NWS, HINT)
    hourly_periods = _dig(hourly, ["properties", "periods"], NWS, HINT)[:48]  # next 48 hours
    if not periods:
        raise SystemExit(
            f"{NWS} returned a forecast with no periods in it for {args.lat},{args.lon}. "
            f"The location may be outside NWS coverage (the API covers the US and its "
            f"territories only) rather than the service being broken."
        )

    radar_station = props.get("radarStation")

    out = {
        "source": "NOAA/NWS api.weather.gov",
        "query": {"lat": args.lat, "lon": args.lon},
        "grid": {"office": props.get("gridId"), "x": props.get("gridX"), "y": props.get("gridY")},
        # A forecast is a snapshot; a storm risk is a moving target. Whenever precip
        # risk is real (thunderstorm chance, etc.), point to a live radar view instead
        # of just a probability number — this is the nearest NWS radar station's
        # standard live loop, not a static image.
        "radar_url": f"https://radar.weather.gov/station/{radar_station}/standard" if radar_station else None,
        "daily_periods": [
            {
                "name": p.get("name"),
                "is_daytime": p.get("isDaytime"),
                "temperature_f": p.get("temperature"),
                "precip_probability_pct": (p.get("probabilityOfPrecipitation") or {}).get("value"),
                "wind_speed": p.get("windSpeed"),
                "wind_direction": p.get("windDirection"),
                "short_forecast": p.get("shortForecast"),
                "detailed_forecast": p.get("detailedForecast"),
                "lead_days": i // 2,  # rough: two periods (day/night) per day
                "confidence": "lower — beyond ~7 days" if i // 2 >= 7 else "normal",
            }
            for i, p in enumerate(periods)
        ],
        "hourly_next_48h": [
            {
                "start_time": p.get("startTime"),
                "temperature_f": p.get("temperature"),
                "precip_probability_pct": (p.get("probabilityOfPrecipitation") or {}).get("value"),
                "wind_speed": p.get("windSpeed"),
                "short_forecast": p.get("shortForecast"),
            }
            for p in hourly_periods
        ],
    }
    with open(args.json, "w") as f:
        json.dump(out, f, indent=2)
    if not args.quiet:
        print(f"Forecast written to {args.json} ({len(periods)} daily periods, {len(hourly_periods)} hourly)")


if __name__ == "__main__":
    main()
