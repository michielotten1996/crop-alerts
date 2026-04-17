from diseases import assess_crop

RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}


def score_all(crops: list[str], forecast: list[dict]) -> list[dict]:
    """Score all crops against the forecast."""
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
