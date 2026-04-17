from diseases import assess_crop

RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
RANK_NUM = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}


def score_all(crops: list[str], forecast: list[dict]) -> list[dict]:
    """Score all crops against a window of days."""
    results = []
    for crop in crops:
        assessments = assess_crop(crop, forecast)
        overall = max(assessments, key=lambda a: RANK[a["risk"]], default={"risk": "LOW"})["risk"]
        results.append({
            "crop": crop.capitalize(),
            "overall_risk": overall,
            "diseases": assessments,
        })
    return results


def score_timeline(crops: list[str], all_days: list[dict], window: int = 7) -> list[dict]:
    """
    For each day in all_days, score crops using a rolling window of `window` days
    ending on that day. Returns a list of {date, crop: risk_level} dicts.
    """
    timeline = []
    for i, day in enumerate(all_days):
        start = max(0, i - window + 1)
        window_days = all_days[start: i + 1]
        entry = {"date": day["date"]}
        for crop in crops:
            assessments = assess_crop(crop, window_days)
            overall = max(assessments, key=lambda a: RANK[a["risk"]], default={"risk": "LOW"})["risk"]
            entry[crop.capitalize()] = RANK_NUM[overall]
        timeline.append(entry)
    return timeline
