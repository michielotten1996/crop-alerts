import requests
from datetime import date, timedelta
from collections import defaultdict

HISTORICAL_URL = "https://archive-api.open-meteo.com/v1/archive"
FORECAST_URL   = "https://api.open-meteo.com/v1/forecast"

COMMON_PARAMS = {
    "daily": "temperature_2m_mean,temperature_2m_min,temperature_2m_max,relative_humidity_2m_max,precipitation_sum",
    "timezone": "auto",
}


def fetch_historical(lat: float, lon: float, days_back: int = 90) -> list[dict]:
    """Fetch historical daily weather from Open-Meteo (free, no API key)."""
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=days_back - 1)
    resp = requests.get(HISTORICAL_URL, params={
        "latitude": lat, "longitude": lon,
        "start_date": start.isoformat(),
        "end_date": end.isoformat(),
        **COMMON_PARAMS,
    }, timeout=15)
    resp.raise_for_status()
    return _parse(resp.json())


def fetch_forecast(lat: float, lon: float) -> list[dict]:
    """Fetch 7-day forecast from Open-Meteo (free, no API key)."""
    resp = requests.get(FORECAST_URL, params={
        "latitude": lat, "longitude": lon,
        "forecast_days": 7,
        **COMMON_PARAMS,
    }, timeout=15)
    resp.raise_for_status()
    return _parse(resp.json())


def fetch_all(lat: float, lon: float, days_back: int = 90) -> list[dict]:
    """Historical + forecast combined, sorted by date."""
    historical = fetch_historical(lat, lon, days_back)
    forecast   = fetch_forecast(lat, lon)
    seen = {d["date"] for d in historical}
    combined = historical + [d for d in forecast if d["date"] not in seen]
    return sorted(combined, key=lambda d: d["date"])


def _parse(data: dict) -> list[dict]:
    daily = data["daily"]
    dates = daily["time"]
    return [
        {
            "date":         dates[i],
            "temp_avg":     daily["temperature_2m_mean"][i] or 0,
            "temp_min":     daily["temperature_2m_min"][i]  or 0,
            "temp_max":     daily["temperature_2m_max"][i]  or 0,
            "humidity_max": daily["relative_humidity_2m_max"][i] or 0,
            "rain_mm":      daily["precipitation_sum"][i]   or 0,
        }
        for i in range(len(dates))
    ]
