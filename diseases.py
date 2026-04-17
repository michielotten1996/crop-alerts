from config import DISEASE_RULES


def check_disease(rule: dict, forecast: list[dict]) -> tuple[str, int]:
    """Return (risk_level, consecutive_days_triggered) for a single disease rule."""
    streak = 0
    max_streak = 0

    for day in forecast:
        conditions_met = (
            rule["temp_min"] <= day["temp_avg"] <= rule["temp_max"]
            and day["humidity_max"] >= rule["humidity_min"]
            and day["rain_mm"] >= rule["rain_mm_min"]
        )
        if conditions_met:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0

    required = rule["days"]
    if max_streak >= required + 2:
        return "HIGH", max_streak
    elif max_streak >= required:
        return "MEDIUM", max_streak
    else:
        return "LOW", max_streak


def assess_crop(crop: str, forecast: list[dict]) -> list[dict]:
    """Return disease assessments for a crop."""
    rules = DISEASE_RULES.get(crop, [])
    results = []
    for rule in rules:
        level, days = check_disease(rule, forecast)
        results.append({
            "disease": rule["name"],
            "risk": level,
            "trigger_days": days,
        })
    return results
