import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

REPORTS_DIR = BASE_DIR / "reports"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)


subject_demand_path = REPORTS_DIR / "subject_demand_report.csv"
validated_choices_path = PROCESSED_DATA_DIR / "validated_subject_choices.csv"
invalid_choices_path = PROCESSED_DATA_DIR / "invalid_choices.csv"


subject_demand_df = pd.read_csv(subject_demand_path)
validated_choices_df = pd.read_csv(validated_choices_path)
invalid_choices_df = pd.read_csv(invalid_choices_path)


total_learners = validated_choices_df["student_id"].nunique()

valid_choices_count = validated_choices_df[
    validated_choices_df["status"] == "Valid"
].shape[0]

invalid_choices_count = validated_choices_df[
    validated_choices_df["status"] == "Invalid"
].shape[0]

top_subjects = subject_demand_df.head(5)
lowest_subjects = subject_demand_df.tail(5)

most_common_invalid_subjects = (
    invalid_choices_df
    .value_counts("invalid_subject")
    .reset_index(name="number_of_invalid_choices")
    .sort_values(by="number_of_invalid_choices", ascending=False)
    .head(5)
)


summary_lines = []

summary_lines.append("School Subject Choice Recommendation System")
summary_lines.append("Executive Summary")
summary_lines.append("=" * 50)
summary_lines.append("")

summary_lines.append(f"Total learners processed: {total_learners}")
summary_lines.append(f"Valid subject choice packages: {valid_choices_count}")
summary_lines.append(f"Invalid subject choice packages: {invalid_choices_count}")
summary_lines.append("")

summary_lines.append("Top 5 subjects by demand:")
for _, row in top_subjects.iterrows():
    summary_lines.append(
        f"- {row['subject']}: {row['number_of_learners']} learners"
    )

summary_lines.append("")

summary_lines.append("Lowest 5 subjects by demand:")
for _, row in lowest_subjects.iterrows():
    summary_lines.append(
        f"- {row['subject']}: {row['number_of_learners']} learners"
    )

summary_lines.append("")

summary_lines.append("Most common invalid subject choices:")
if most_common_invalid_subjects.empty:
    summary_lines.append("- No invalid subject choices found.")
else:
    for _, row in most_common_invalid_subjects.iterrows():
        summary_lines.append(
            f"- {row['invalid_subject']}: {row['number_of_invalid_choices']} invalid selections"
        )

summary_lines.append("")

summary_lines.append("Key interpretation:")
summary_lines.append(
    "This report helps the school understand subject demand, identify invalid choices, "
    "and support earlier intervention before final subject allocations are confirmed."
)

summary_text = "\n".join(summary_lines)

output_path = REPORTS_DIR / "executive_summary.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(summary_text)

print(f"Executive summary saved at: {output_path}")
print()
print(summary_text)