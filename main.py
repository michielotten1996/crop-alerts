import argparse
from weather import fetch_all
from scorer import score_all, score_timeline
from report import generate
from config import CROPS


def main():
    parser = argparse.ArgumentParser(description="Crop disease early warning")
    parser.add_argument("--lat",      type=float, default=52.3,           help="Latitude")
    parser.add_argument("--lon",      type=float, default=4.9,            help="Longitude")
    parser.add_argument("--crops",    default=",".join(CROPS),            help="Comma-separated crops")
    parser.add_argument("--days",     type=int,   default=90,             help="Days of history to fetch")
    args = parser.parse_args()

    crops = [c.strip().lower() for c in args.crops.split(",")]

    print(f"Fetching {args.days} days of weather data for ({args.lat}, {args.lon})…")
    all_days = fetch_all(args.lat, args.lon, days_back=args.days)
    print(f"  Got {len(all_days)} days total (history + forecast)")

    # Score current risk using last 7 days + forecast
    recent = all_days[-14:]
    scores = score_all(crops, recent)

    # Score every day for the timeline chart
    timeline = score_timeline(crops, all_days)

    print("\nCurrent risk summary:")
    for s in scores:
        print(f"  {s['crop']:<10} {s['overall_risk']}")

    filename = generate(scores, all_days, timeline, args.lat, args.lon)
    print(f"\nReport saved → {filename}")


if __name__ == "__main__":
    main()
