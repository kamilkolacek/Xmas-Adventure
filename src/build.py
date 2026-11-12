"""Rebuild index.html from the template, the Leaflet stylesheet and the packed map data.

Usage (from the repo root):  python3 src/build.py
"""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
src = root / "src"
page = (src / "template.html").read_text()
page = page.replace("/*LEAFLETCSS*/", (src / "leaflet.css").read_text())
page = page.replace("/*DATA*/", (src / "data.js").read_text())
(root / "index.html").write_text(page)
print("Wrote", root / "index.html")
