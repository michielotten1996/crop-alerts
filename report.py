from datetime import date
from jinja2 import Environment, FileSystemLoader
from config import RISK_ACTIONS


def generate(scores: list[dict], forecast: list[dict], lat: float, lon: float) -> str:
    env = Environment(loader=FileSystemLoader("templates"))
    tmpl = env.get_template("report.html")

    html = tmpl.render(
        date=date.today().strftime("%B %d, %Y"),
        lat=lat,
        lon=lon,
        scores=scores,
        forecast=forecast[:5],
        actions=RISK_ACTIONS,
    )

    filename = f"crop_alert_{date.today()}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    return filename
