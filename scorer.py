from diseases import assess_crop
from wheat_engine import assess_wheat, wheat_summary_advice

RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
RANK_NUM = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}


def score_all(crops: list[str], forecast: list[dict]) -> list[dict]:
    results = []
    for crop in crops:
        if crop == "wheat":
            assessments = assess_wheat(forecast)
            overall = max(assessments, key=lambda a: RANK[a["risk"]], default={"risk": "LOW"})["risk"]
            results.append({
                "crop": "Wheat",
                "overall_risk": overall,
                "diseases": assessments,
                "summary_advice": wheat_summary_advice(assessments),
                "is_wheat": True,
            })
        else:
            assessments = assess_crop(crop, forecast)
            overall = max(assessments, key=lambda a: RANK[a["risk"]], default={"risk": "LOW"})["risk"]
            results.append({
                "crop": crop.capitalize(),
                "overall_risk": overall,
                "diseases": assessments,
                "summary_advice": "",
                "is_wheat": False,
            })
    return results


def score_timeline(crops: list[str], all_days: list[dict], window: int = 7) -> list[dict]:
    timeline = []
    for i, day in enumerate(all_days):
        start = max(0, i - window + 1)
        window_days = all_days[start: i + 1]
        entry = {"date": day["date"]}
        for crop in crops:
            if crop == "wheat":
                assessments = assess_wheat(window_days)
            else:
                assessments = assess_crop(crop, window_days)
            overall = max(assessments, key=lambda a: RANK[a["risk"]], default={"risk": "LOW"})["risk"]
            entry[crop.capitalize()] = RANK_NUM[overall]
        timeline.append(entry)
    return timeline
