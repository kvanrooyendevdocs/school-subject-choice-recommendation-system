import pandas as pd
import random 
from pathlib import Path


# This finds the main project folder.
# __file__ means "this current Python file".
# .parents[1] moves up from scripts/ to the main project folder.
BASE_DIR = Path(__file__).resolve().parents[1]

#folders to save data 
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
#check exists
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", 
               "Heidi", "Ivan", "Judy", "Karl", "Leo", "Mallory", "Nina", 
               "Oscar", "Peggy", "Quentin", "Rita", "Sam", "Trudy"
]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
              "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", 
              "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson"
]

learners = []

for student_number in range(1, 101):
    learner = {
        "student_id": 1000 + student_number,
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "grade": 9,
        "math_mark": random.randint(30, 95),
        "english_mark": random.randint(35, 95),
        "natural_science_mark": random.randint(25, 95),
        "social_science_mark": random.randint(35, 95),
        "ems_mark": random.randint(30, 95),
        "creative_arts_mark": random.randint(40, 95),
    }
    learners.append(learner)

learners_df = pd.DataFrame(learners)

output_path = RAW_DATA_DIR / "learners.csv"

learners_df.to_csv(output_path, index=False)

print(f"Sample learner data created successfully at: {output_path}")
print(learners_df.head())
    