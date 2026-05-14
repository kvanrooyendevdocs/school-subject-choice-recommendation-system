import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)


validated_choices_path = PROCESSED_DATA_DIR / "validated_subject_choices.csv"
subject_demand_path = REPORTS_DIR / "subject_demand_report.csv"
invalid_subject_report_path = REPORTS_DIR / "invalid_subject_report.csv"


validated_choices_df = pd.read_csv(validated_choices_path)
subject_demand_df = pd.read_csv(subject_demand_path)
invalid_subject_report_df = pd.read_csv(invalid_subject_report_path)


total_learners = validated_choices_df["student_id"].nunique()

valid_packages = validated_choices_df[
    validated_choices_df["status"] == "Valid"
].shape[0]

invalid_packages = validated_choices_df[
    validated_choices_df["status"] == "Invalid"
].shape[0]

invalid_percentage = (invalid_packages / total_learners) * 100


most_selected_subject = subject_demand_df.iloc[0]["subject"]
most_selected_subject_count = subject_demand_df.iloc[0]["number_of_learners"]

least_selected_subject = subject_demand_df.iloc[-1]["subject"]
least_selected_subject_count = subject_demand_df.iloc[-1]["number_of_learners"]


if invalid_subject_report_df.empty:
    most_invalid_subject = "None"
    most_invalid_subject_count = 0
else:
    most_invalid_subject = invalid_subject_report_df.iloc[0]["invalid_subject"]
    most_invalid_subject_count = invalid_subject_report_df.iloc[0]["number_of_invalid_choices"]


kpi_summary = {
    "total_learners": total_learners,
    "valid_subject_packages": valid_packages,
    "invalid_subject_packages": invalid_packages,
    "invalid_percentage": round(invalid_percentage, 2),
    "most_selected_subject": most_selected_subject,
    "most_selected_subject_count": most_selected_subject_count,
    "least_selected_subject": least_selected_subject,
    "least_selected_subject_count": least_selected_subject_count,
    "subject_with_most_invalid_choices": most_invalid_subject,
    "most_invalid_choices_count": most_invalid_subject_count,
}


kpi_summary_df = pd.DataFrame([kpi_summary])

csv_output_path = REPORTS_DIR / "kpi_summary.csv"

kpi_summary_df.to_csv(csv_output_path, index=False)


text_output_path = REPORTS_DIR / "kpi_summary.txt"

summary_lines = [
    "School Subject Choice Recommendation System",
    "KPI Summary",
    "=" * 50,
    "",
    f"Total learners processed: {total_learners}",
    f"Valid subject choice packages: {valid_packages}",
    f"Invalid subject choice packages: {invalid_packages}",
    f"Invalid package percentage: {round(invalid_percentage, 2)}%",
    "",
    f"Most selected subject: {most_selected_subject} ({most_selected_subject_count} learners)",
    f"Least selected subject: {least_selected_subject} ({least_selected_subject_count} learners)",
    "",
    f"Subject with most invalid choices: {most_invalid_subject} ({most_invalid_subject_count} invalid choices)",
]

summary_text = "\n".join(summary_lines)

with open(text_output_path, "w", encoding="utf-8") as file:
    file.write(summary_text)


print(f"KPI summary CSV saved at: {csv_output_path}")
print(f"KPI summary text file saved at: {text_output_path}")
print()
print(summary_text)