import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)

invalid_choices_path = PROCESSED_DATA_DIR / "invalid_choices.csv"

invalid_choices_df = pd.read_csv(invalid_choices_path)

invalid_subject_report_df = (
    invalid_choices_df
    .value_counts("invalid_subject")
    .reset_index(name="number_of_invalid_choices")
    .sort_values(by="number_of_invalid_choices", ascending=False)
)


output_path = REPORTS_DIR / "invalid_subject_report.csv"

invalid_subject_report_df.to_csv(output_path, index=False)

print(f"Invalid subject report saved at: {output_path}")
print(invalid_subject_report_df)