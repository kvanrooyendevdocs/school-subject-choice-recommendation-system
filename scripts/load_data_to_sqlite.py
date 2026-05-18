import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
REPORTS_DIR = BASE_DIR / "reports"

DATABASE_PATH = DATA_DIR / "school_subject_reco.db"


tables_to_load = {
    "learners": RAW_DATA_DIR / "learners.csv",
    "subject_rules": RAW_DATA_DIR / "subject_rules.csv",
    "parent_subject_choices": RAW_DATA_DIR / "parent_subject_choices.csv",
    "learner_recommendations": PROCESSED_DATA_DIR / "learner_recommendations.csv",
    "validated_subject_choices": PROCESSED_DATA_DIR / "validated_subject_choices.csv",
    "invalid_choices": PROCESSED_DATA_DIR / "invalid_choices.csv",
    "ranked_learner_recommendations": PROCESSED_DATA_DIR / "ranked_learner_recommendations.csv",
    "subject_demand_report": REPORTS_DIR / "subject_demand_report.csv",
    "invalid_subject_report": REPORTS_DIR / "invalid_subject_report.csv",
    "kpi_summary": REPORTS_DIR / "kpi_summary.csv",
}


with sqlite3.connect(DATABASE_PATH) as connection:
    for table_name, file_path in tables_to_load.items():
        if not file_path.exists():
            print(f"Skipping {table_name}: file not found at {file_path}")
            continue

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            connection,
            if_exists="replace",
            index=False,
        )

        print(f"Loaded {table_name}: {len(df)} rows")

print()
print(f"SQLite database created at: {DATABASE_PATH}")