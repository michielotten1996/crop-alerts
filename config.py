CROPS = ["potato", "wheat", "tomato", "grape", "corn"]

# Disease rules based on peer-reviewed forecasting models.
# Sources: BLIGHTSIM (Grünwald et al.), ShIFT model (Racca et al.),
# Plasmopara viticola primary infection thresholds (Lalancette et al.),
# Botrytis cinerea wetness-duration model (Yunis et al., Phytopathology 1994).
#
# Fields:
#   temp_min/max  — daily average temperature range triggering infection (°C)
#   humidity_min  — max daily relative humidity threshold (%)
#   rain_mm_min   — minimum daily rainfall to trigger infection (mm)
#   days          — consecutive days conditions must be met for MEDIUM risk
#                   (days+2 consecutive days → HIGH risk)
DISEASE_RULES = {
    "potato": [
        # BLIGHTSIM / Nærstad model: RH ≥ 80% is sufficient for sporangia at 17°C;
        # zoospores active 7–18°C, sporangia 10–25°C. Humidity threshold lowered
        # from legacy 90% to scientifically validated 80%.
        {"name": "Late Blight (P. infestans)", "temp_min": 7,  "temp_max": 25, "humidity_min": 80, "rain_mm_min": 0, "days": 2},
        # Early Blight: warm, alternating wet/dry; humidity threshold 70% validated
        # by Waggoner & Horsfall (1969) EPIDEM model.
        {"name": "Early Blight (A. solani)",   "temp_min": 20, "temp_max": 30, "humidity_min": 70, "rain_mm_min": 0, "days": 3},
    ],
    "wheat": [
        # ShIFT model (Racca et al. 2021): primary driver is rainfall ≥ 2.5mm during
        # stem elongation with temp 10–20°C; wetness duration key for secondary spread.
        {"name": "Septoria Leaf Blotch",       "temp_min": 10, "temp_max": 20, "humidity_min": 75, "rain_mm_min": 2.5, "days": 2},
        # Fusarium: warm, humid at anthesis; 15–30°C + rain validated by
        # Rossi et al. (2003) DONcast model.
        {"name": "Fusarium Head Blight",       "temp_min": 15, "temp_max": 30, "humidity_min": 85, "rain_mm_min": 2, "days": 2},
    ],
    "tomato": [
        # Same P. infestans model as potato — pathogen is identical.
        {"name": "Late Blight (P. infestans)", "temp_min": 7,  "temp_max": 25, "humidity_min": 80, "rain_mm_min": 0, "days": 2},
        # Botrytis: Yunis et al. (1994) — wetness > 7h/day + night temp 9–21°C.
        # Proxy with daily humidity ≥ 85% and temp in range as best available daily signal.
        {"name": "Botrytis (Grey Mould)",      "temp_min": 9,  "temp_max": 21, "humidity_min": 85, "rain_mm_min": 0, "days": 3},
    ],
    "grape": [
        # Lalancette et al. (2008): primary infection threshold rain > 2.5mm + temp > 11°C.
        # Lowered rain threshold from 10mm (Goidanich model) to 2.5mm per modern literature.
        {"name": "Downy Mildew (P. viticola)", "temp_min": 11, "temp_max": 30, "humidity_min": 75, "rain_mm_min": 2.5, "days": 1},
        # Botrytis in grape: same wetness-duration model as tomato.
        {"name": "Botrytis (Grey Mould)",      "temp_min": 9,  "temp_max": 21, "humidity_min": 85, "rain_mm_min": 0,  "days": 3},
    ],
    "corn": [
        # Northern Leaf Blight (E. turcicum): warm humid nights ≥ 18°C,
        # RH > 80% for 6h+ (Levy & Cohen 1983).
        {"name": "Northern Leaf Blight",       "temp_min": 18, "temp_max": 27, "humidity_min": 80, "rain_mm_min": 0, "days": 3},
        # Grey Leaf Spot (C. zeae-maydis): hot humid conditions, RH > 85%,
        # temp 25–35°C (Ward et al. 1999).
        {"name": "Grey Leaf Spot",             "temp_min": 25, "temp_max": 35, "humidity_min": 85, "rain_mm_min": 0, "days": 2},
    ],
}

RISK_ACTIONS = {
    "LOW":    "No action needed. Continue routine monitoring.",
    "MEDIUM": "Scout fields this week. Consider preventive fungicide application.",
    "HIGH":   "High infection risk. Apply fungicide within 48 hours and increase field scouting.",
}
