import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok = True)


subject_rules = [
    {
        "subject": "English",
        "minimum_required_mark": 0,
        "required_field": "english_mark",
        "category": "Core"
    },
    {
        "subject": "Life Orientation",
        "minimum_required_mark": 0,
        "required_field": "english_mark",
        "category": "Core"
    },
    {
        "subject": "Mathematics",
        "minimum_required_mark": 60,
        "required_field": "math_mark",
        "category": "Core"
    },
    {
        "subject": "Mathematical Literacy",
        "minimum_required_mark": 0,
        "required_field": "math_mark",
        "category": "Core"
    },
    {
        "subject": "Physical Sciences",
        "minimum_required_mark": 65,
        "required_field": "natural_science_mark",
        "category": "Science"
    },
    {
        "subject": "Life Sciences",
        "minimum_required_mark": 55,
        "required_field": "natural_science_mark",
        "category": "Science"
    },
    {
        "subject": "Accounting",
        "minimum_required_mark": 60,
        "required_field": "ems_mark",
        "category": "Commerce"
    },
    {
        "subject": "Business Studies",
        "minimum_required_mark": 50,
        "required_field": "ems_mark",
        "category": "Commerce"
    },
    {
        "subject": "Geography",
        "minimum_required_mark": 50,
        "required_field": "social_science_mark",
        "category": "Humanities"
    },
    {
        "subject": "History",
        "minimum_required_mark": 50,
        "required_field": "social_science_mark",
        "category": "Humanities"
    },
    {
        "subject": "Visual Arts",
        "minimum_required_mark": 60,
        "required_field": "creative_arts_mark",
        "category": "Arts"
    },
    {
        "subject": "Computer Applications Technology",
        "minimum_required_mark": 55,
        "required_field": "math_mark",
        "category": "Technology"
    },
    {
        "subject": "Information Technology",
        "minimum_required_mark": 70,
        "required_field": "math_mark",
        "category": "Technology"
    }
]

subject_rules_df = pd.DataFrame(subject_rules)

output_path = RAW_DATA_DIR / "subject_rules.csv"

subject_rules_df.to_csv(output_path, index=False)

print(f"Subject rules created successfully at: {output_path}")
print(subject_rules_df)