import os
import requests
from datetime import datetime, timezone
from collections import defaultdict

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


def fetch_forecast(lat: float, lon: float) -> list[dict]:
    """Fetch 5-day/3-hour forecast and aggregate to daily summaries."""
    api_key = os.environ["OPENWEATHER_API_KEY"]
    resp = requests.get(BASE_URL, params={
        "lat": lat, "lon": lon,
        "appid": api_key,
        "units": "metric",
    }, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    daily: dict[str, list] = defaultdict(list)
    for item in data["list"]:
        dt = datetime.fromtimestamp(item["dt"], tz=timezone.utc)
        day = dt.strftime("%Y-%m-%d")
        daily[day].append({
            "temp": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "rain_mm": item.get("rain", {}).get("3h", 0),
        })

    result = []
    for day in sorted(daily.keys()):
        readings = daily[day]
        result.append({
            "date": day,
            "temp_avg": sum(r["temp"] for r in readings) / len(readings),
            "temp_min": min(r["temp"] for r in readings),
            "temp_max": max(r["temp"] for r in readings),
            "humidity_max": max(r["humidity"] for r in readings),
            "rain_mm": sum(r["rain_mm"] for r in readings),
        })

    return result
