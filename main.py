import argparse
import os
from dotenv import load_dotenv
from weather import fetch_forecast
from scorer import score_all
from report import generate
from config import CROPS

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Crop disease early warning")
    parser.add_argument("--lat", type=float, default=52.3, help="Latitude")
    parser.add_argument("--lon", type=float, default=4.9,  help="Longitude")
    parser.add_argument("--crops", default=",".join(CROPS), help="Comma-separated crops")
    args = parser.parse_args()

    crops = [c.strip().lower() for c in args.crops.split(",")]

    print(f"Fetching forecast for ({args.lat}, {args.lon})…")
    forecast = fetch_forecast(args.lat, args.lon)
    print(f"  Got {len(forecast)} days of forecast data")

    scores = score_all(crops, forecast)

    print("\nRisk summary:")
    for s in scores:
        print(f"  {s['crop']:<10} {s['overall_risk']}")

    filename = generate(scores, forecast, args.lat, args.lon)
    print(f"\nReport saved → {filename}")


if __name__ == "__main__":
    main()
