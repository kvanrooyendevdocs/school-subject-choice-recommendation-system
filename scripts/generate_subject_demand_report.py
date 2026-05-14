import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)


choices_path = RAW_DATA_DIR / "parent_subject_choices.csv"

choices_df = pd.read_csv(choices_path)


choice_columns = [
    "choice_1",
    "choice_2",
    "choice_3",
    "choice_4",
    "choice_5",
    "choice_6",
    "choice_7",
]


all_selected_subjects = []

for _, row in choices_df.iterrows():
    for column in choice_columns:
        subject = row[column]

        all_selected_subjects.append(subject)


subject_demand_df = pd.DataFrame(all_selected_subjects, columns=["subject"])

subject_demand_report = (
    subject_demand_df
    .value_counts("subject")
    .reset_index(name="number_of_learners")
    .sort_values(by="number_of_learners", ascending=False)
)


output_path = REPORTS_DIR / "subject_demand_report.csv"

subject_demand_report.to_csv(output_path, index=False)

print(f"Subject demand report saved at: {output_path}")
print(subject_demand_report)