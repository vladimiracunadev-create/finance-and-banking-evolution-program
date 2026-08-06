from pathlib import Path
import csv

root = Path(__file__).parents[1]
classes = sorted((root / "modules").glob("*/classes/*.md"))
out = root / "progress-tracker.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["class_path", "status", "score", "notes"])
    for path in classes:
        writer.writerow([path.relative_to(root), "not-started", "", ""])
print(out)
