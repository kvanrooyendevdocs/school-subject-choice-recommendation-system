import pandas as pd
from pathlib import Path

#1. Import tools.
#2. Find the main project folder.
#3. Find the raw and processed data folders.
#4. Read learners.csv.
#5. Read subject_rules.csv.
#6. Create an empty list for recommendations.
#7. For each learner:
 #     For each subject:
  #        Find the learner’s relevant mark.
   #       Compare it to the subject requirement.
    #      Decide if the subject is recommended.
     #     Calculate a recommendation score.
      #    Store the result.
#8. Convert all results into a table.
#9. Save the table as learner_recommendations.csv.
#10. Print the first few rows so we can check it.

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok = True)

learners_path = RAW_DATA_DIR / "learners.csv"
subject_rules_path = RAW_DATA_DIR / "subject_rules.csv"

learners_df = pd.read_csv(learners_path)
subject_rules_df = pd.read_csv(subject_rules_path)

recommendations = []

for _, learner in learners_df.iterrows():
    for _, rule in subject_rules_df.iterrows():

        required_field = rule["required_field"]
        learner_mark = learner[required_field]
        minimum_required_mark = rule["minimum_required_mark"]

        if learner_mark >= minimum_required_mark:
            status = "Recommended"
        else:
            status = "Not eligible"
        
        recommendation_score = learner_mark - minimum_required_mark

        recommendation = {
            "student_id": learner["student_id"],
            "name": learner["name"],
            "grade": learner["grade"],
            "subject": rule["subject"],
            "category": rule["category"],
            "required_field": required_field,
            "learner_mark": learner_mark,
            "minimum_required_mark": minimum_required_mark,
            "status": status,
            "recommendation_score": recommendation_score
        }
        recommendations.append(recommendation)

recommendations_df = pd.DataFrame(recommendations)

output_path = PROCESSED_DATA_DIR / "subject_recommendations.csv"

recommendations_df.to_csv(output_path, index=False)

print(f"Recommendations created successfully at: {output_path}")
print(recommendations_df.head(20))