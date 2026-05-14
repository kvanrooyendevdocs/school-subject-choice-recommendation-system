import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)


choices_path = RAW_DATA_DIR / "parent_subject_choices.csv"
recommendations_path = PROCESSED_DATA_DIR / "learner_recommendations.csv"

choices_df = pd.read_csv(choices_path)
recommendations_df = pd.read_csv(recommendations_path)


choice_columns = [
    "choice_1",
    "choice_2",
    "choice_3",
    "choice_4",
    "choice_5",
    "choice_6",
    "choice_7",
]


validation_results = []
invalid_choice_details = []


for _, choice_row in choices_df.iterrows():
    student_id = choice_row["student_id"]
    learner_name = choice_row["name"]

    selected_subjects = [
        choice_row[column]
        for column in choice_columns
        if pd.notna(choice_row[column])
    ]

    issues = []

    if len(selected_subjects) != 7:
        issues.append("Learner must choose exactly 7 subjects.")

    if "English" not in selected_subjects:
        issues.append("English is required.")

    if "Life Orientation" not in selected_subjects:
        issues.append("Life Orientation is required.")

    has_mathematics = "Mathematics" in selected_subjects
    has_mathematical_literacy = "Mathematical Literacy" in selected_subjects

    if has_mathematics and has_mathematical_literacy:
        issues.append("Learner cannot choose both Mathematics and Mathematical Literacy.")

    if not has_mathematics and not has_mathematical_literacy:
        issues.append("Learner must choose either Mathematics or Mathematical Literacy.")

    learner_recommendations = recommendations_df[
        recommendations_df["student_id"] == student_id
    ]

    eligible_subjects = learner_recommendations[
        learner_recommendations["status"] == "Recommended"
    ]["subject"].tolist()

    for subject in selected_subjects:
        if subject not in eligible_subjects:
            issues.append(f"Learner is not eligible for {subject}.")

            invalid_choice_details.append(
                {
                    "student_id": student_id,
                    "name": learner_name,
                    "invalid_subject": subject,
                    "reason": "Learner does not meet the minimum requirement.",
                }
            )

    if issues:
        final_status = "Invalid"
    else:
        final_status = "Valid"

    validation_results.append(
        {
            "student_id": student_id,
            "name": learner_name,
            "selected_subjects": ", ".join(selected_subjects),
            "status": final_status,
            "issues": " | ".join(issues),
        }
    )


validation_results_df = pd.DataFrame(validation_results)
invalid_choice_details_df = pd.DataFrame(invalid_choice_details)

validation_output_path = PROCESSED_DATA_DIR / "validated_subject_choices.csv"
invalid_choices_output_path = PROCESSED_DATA_DIR / "invalid_choices.csv"

validation_results_df.to_csv(validation_output_path, index=False)
invalid_choice_details_df.to_csv(invalid_choices_output_path, index=False)

print(f"Validated choices saved at: {validation_output_path}")
print(f"Invalid choices saved at: {invalid_choices_output_path}")
print(validation_results_df.head(20))