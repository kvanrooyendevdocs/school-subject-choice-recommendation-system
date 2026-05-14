import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

REPORTS_DIR = BASE_DIR / "reports"
VISUALS_DIR = BASE_DIR / "visuals"

VISUALS_DIR.mkdir(parents=True, exist_ok=True)


report_path = REPORTS_DIR / "subject_demand_report.csv"

subject_demand_df = pd.read_csv(report_path)

# Create a horizontal bar chart to visualize subject demand
plt.figure(figsize=(12, 7))

# The y-axis will have the subjects and the x-axis will have the number of learners.
plt.barh(
    subject_demand_df["subject"],
    subject_demand_df["number_of_learners"]
)

# Add labels and title to the chart
plt.xlabel("Number of Learners")
plt.ylabel("Subject")
plt.title("Subject Demand by Number of Learners")

# Invert the y-axis to have the most popular subjects at the top
plt.gca().invert_yaxis()

# Adjust layout to prevent clipping of labels
plt.tight_layout()

output_path = VISUALS_DIR / "subject_demand_chart.png"

plt.savefig(output_path, dpi=300)

print(f"Subject demand chart saved at: {output_path}")