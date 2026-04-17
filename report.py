from datetime import date
from jinja2 import Environment, FileSystemLoader
from config import RISK_ACTIONS


def generate(scores: list[dict], all_days: list[dict], timeline: list[dict], lat: float, lon: float) -> str:
    env = Environment(loader=FileSystemLoader("templates"))
    tmpl = env.get_template("report.html")

    forecast = [d for d in all_days if d["date"] >= date.today().isoformat()][:7]
    if not forecast:
        forecast = all_days[-7:]

    html = tmpl.render(
        date=date.today().strftime("%B %d, %Y"),
        lat=lat,
        lon=lon,
        scores=scores,
        forecast=forecast,
        all_days=all_days,
        timeline=timeline,
        actions=RISK_ACTIONS,
    )

    filename = f"crop_alert_{date.today()}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    return filename
