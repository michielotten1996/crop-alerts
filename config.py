CROPS = ["potato", "wheat", "tomato", "grape", "corn"]

# Disease rules: {crop: [{name, temp_min, temp_max, humidity_min, rain_mm_min, consecutive_days}]}
DISEASE_RULES = {
    "potato": [
        {"name": "Late Blight (P. infestans)", "temp_min": 10, "temp_max": 25, "humidity_min": 85, "rain_mm_min": 0, "days": 2},
        {"name": "Early Blight (A. solani)",   "temp_min": 20, "temp_max": 30, "humidity_min": 70, "rain_mm_min": 0, "days": 3},
    ],
    "wheat": [
        {"name": "Septoria Leaf Blotch",       "temp_min": 10, "temp_max": 25, "humidity_min": 80, "rain_mm_min": 1, "days": 2},
        {"name": "Fusarium Head Blight",       "temp_min": 15, "temp_max": 30, "humidity_min": 90, "rain_mm_min": 2, "days": 2},
    ],
    "tomato": [
        {"name": "Late Blight (P. infestans)", "temp_min": 10, "temp_max": 25, "humidity_min": 85, "rain_mm_min": 0, "days": 2},
        {"name": "Botrytis (Grey Mould)",      "temp_min": 15, "temp_max": 25, "humidity_min": 90, "rain_mm_min": 0, "days": 2},
    ],
    "grape": [
        {"name": "Downy Mildew",               "temp_min": 11, "temp_max": 30, "humidity_min": 80, "rain_mm_min": 10, "days": 1},
        {"name": "Botrytis (Grey Mould)",      "temp_min": 15, "temp_max": 25, "humidity_min": 90, "rain_mm_min": 0,  "days": 2},
    ],
    "corn": [
        {"name": "Northern Leaf Blight",       "temp_min": 18, "temp_max": 27, "humidity_min": 80, "rain_mm_min": 0, "days": 3},
        {"name": "Grey Leaf Spot",             "temp_min": 25, "temp_max": 35, "humidity_min": 85, "rain_mm_min": 0, "days": 2},
    ],
}

RISK_ACTIONS = {
    "LOW":    "No action needed. Continue routine monitoring.",
    "MEDIUM": "Scout fields this week. Consider preventive fungicide application.",
    "HIGH":   "High infection risk. Apply fungicide within 48 hours and increase field scouting.",
}
