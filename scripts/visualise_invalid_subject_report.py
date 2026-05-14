import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

REPORTS_DIR = BASE_DIR / "reports"
VISUALS_DIR = BASE_DIR / "visuals"

VISUALS_DIR.mkdir(parents=True, exist_ok=True)


report_path = REPORTS_DIR / "invalid_subject_report.csv"

invalid_subject_report_df = pd.read_csv(report_path)


plt.figure(figsize=(12, 7))

plt.barh(
    invalid_subject_report_df["invalid_subject"],
    invalid_subject_report_df["number_of_invalid_choices"]
)

plt.xlabel("Number of Invalid Choices")
plt.ylabel("Subject")
plt.title("Invalid Subject Choices by Subject")

plt.gca().invert_yaxis()

plt.tight_layout()

output_path = VISUALS_DIR / "invalid_subject_chart.png"

plt.savefig(output_path, dpi=300)

print(f"Invalid subject chart saved at: {output_path}")