import pandas as pd
import random
from pathlib import Path

#sets the base directory to the parent folder of the current file
BASE_DIR = Path(__file__).resolve().parents[1]
#defines the path to the raw data directory
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
#setsthe learner csv path
learners_path = RAW_DATA_DIR / "learners.csv"
#reads the learners csv into a dataframe
learners_df = pd.read_csv(learners_path)

#defines the list of possible subjects for the sample choices
possible_subjects = [
    "English",
    "Life Orientation",
    "Mathematics",
    "Mathematical Literacy",
    "Physical Sciences",
    "Life Sciences",
    "Accounting",
    "Business Studies",
    "Geography",
    "History",
    "Visual Arts",
    "Computer Applications Technology",
    "Information Technology",
]

#new list for storing the sample choices
sample_choices = []

#iterates through each learner in the learners dataframe to generate random subject choices
for _, learner in learners_df.iterrows():
    math_choice = random.choice(["Mathematics", "Mathematical Literacy"])
    #creates a list of elective subjects by excluding the core subjects from the possible subjects list
    elective_subjects = [
        subject for subject in possible_subjects
        if subject not in ["English", "Life Orientation", "Mathematics", "Mathematical Literacy"]
    ]
    #randomly selects 4 more choices from the elective subjects list
    chosen_electives = random.sample(elective_subjects, 4)

    #creates a dictionary for the current learners subject choices
    #also includes the student id, name and all the choices made for the subjects
    choices = {
        "student_id": learner["student_id"],
        "name": learner["name"],
        "choice_1": "English",
        "choice_2": "Life Orientation",
        "choice_3": math_choice,
        "choice_4": chosen_electives[0],
        "choice_5": chosen_electives[1],
        "choice_6": chosen_electives[2],
        "choice_7": chosen_electives[3],
    }
    #appends the choices dictionary to the sample choices list
    sample_choices.append(choices)

#converts the sample choices list into a dataframe
sample_choices_df = pd.DataFrame(sample_choices)
#defines the output path for the sample choices csv file
output_path = RAW_DATA_DIR / "sample_choices.csv"
#saves the sample choices dataframe to a csv file without the index
sample_choices_df.to_csv(output_path, index=False)

print(f"Sample parent choices created successfully at: {output_path}")
print(sample_choices_df.head())
