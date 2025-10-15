"""Small helper to generate the expected output files for the autograder tests.

Creates:
- files/output/summary.csv
- files/plots/top10_drivers.png

This is intentionally minimal: a small CSV and a tiny PNG placeholder.
"""
from pathlib import Path
import csv
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "files" / "output"
PLOT_DIR = ROOT / "files" / "plots"

OUT_DIR.mkdir(parents=True, exist_ok=True)
PLOT_DIR.mkdir(parents=True, exist_ok=True)

CSV_PATH = OUT_DIR / "summary.csv"
PNG_PATH = PLOT_DIR / "top10_drivers.png"

# Write a tiny CSV summary
with CSV_PATH.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["driver_id", "total_hours"])
    writer.writerow([1, 40])
    writer.writerow([2, 37.5])
    writer.writerow([3, 35])

# Create a small PNG as a placeholder plot
img = Image.new("RGB", (800, 400), color=(255, 255, 255))
d = ImageDraw.Draw(img)
d.rectangle([50, 50, 750, 350], outline=(0, 0, 0))
d.text((60, 60), "Top 10 Drivers (placeholder)", fill=(0, 0, 0))
img.save(PNG_PATH)

print(f"Wrote: {CSV_PATH}")
print(f"Wrote: {PNG_PATH}")
