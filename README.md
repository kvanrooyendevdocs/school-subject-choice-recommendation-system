# School Subject Choice Recommendation System

## Project Overview

This project is a Python-based subject choice recommendation and validation system for schools.

The goal of the project is to help schools guide learners and parents when selecting subjects. The system uses learner marks and subject-specific rules to recommend suitable subjects, validate parent choices, and identify invalid subject selections.

This project is designed as a data science and analytics portfolio project. It demonstrates how Python can be used to solve a real-world school administration problem using structured data, rule-based logic, and automated reporting.

---

## Problem Statement

Schools often collect subject choices through forms or spreadsheets. This can lead to several problems:

- Learners may select subjects they do not qualify for.
- Parents may choose invalid subject combinations.
- Staff may need to manually check large numbers of submissions.
- Subject demand may be difficult to analyse.
- Invalid choices may only be discovered late in the process.

This project aims to reduce manual checking by automatically validating choices against learner data and subject rules.

---

## Project Objectives

The system is designed to:

1. Generate sample learner data.
2. Generate subject rules and minimum requirements.
3. Recommend subjects based on learner performance.
4. Generate sample parent subject choices.
5. Validate whether selected subjects are allowed.
6. Identify learners with invalid subject choices.
7. Create structured CSV outputs for further analysis.

---

## Tools and Technologies Used

- Python
- Pandas
- CSV files
- Git and GitHub

## Setup Instructions

Clone the repository or download the project files.

Install the required Python libraries:


py -m pip install -r requirements.txt
Then run the full pipeline:
py scripts/run_pipeline.py
---

## Project Structure

```text
School-Subject-Reco-System/
│
├── data/
│   ├── raw/
│   │   ├── learners.csv
│   │   ├── subject_rules.csv
│   │   └── parent_subject_choices.csv
│   │
│   └── processed/
│       ├── learner_recommendations.csv
│       ├── validated_subject_choices.csv
│       └── invalid_choices.csv
│
├── notebooks/
│
├── reports/
│
├── scripts/
│   ├── generate_sample_data.py
│   ├── generate_subject_rules.py
│   ├── recommend_subjects.py
│   ├── generate_sample_choices.py
│   └── validate_choices.py
│
├── visuals/
│
├── .gitignore
└── README.md

Data Files
Raw Data

The data/raw folder contains the input data used by the system.

File	Description
learners.csv	Sample learner information and marks
subject_rules.csv	Subject requirements and minimum marks
parent_subject_choices.csv	Sample parent/learner subject selections
Processed Data

The data/processed folder contains the output files created by the scripts.

File	Description
learner_recommendations.csv	Recommendation status for each learner and subject
validated_subject_choices.csv	Validation results for each learner's full subject package
invalid_choices.csv	Detailed list of invalid subject selections
How the System Works

The system follows this process:

Learner data + subject rules
        ↓
Generate subject recommendations
        ↓
Parent/learner subject choices
        ↓
Validate selected subjects
        ↓
Create validation reports
Scripts
1. generate_sample_data.py

Creates sample learner data with marks for different Grade 9 subject areas.

Output:

data/raw/learners.csv
2. generate_subject_rules.py

Creates subject rules, including minimum mark requirements and the learner mark field used for each subject.

Output:

data/raw/subject_rules.csv

Example rule:

Physical Sciences requires natural_science_mark >= 65
3. recommend_subjects.py

Compares each learner's marks against each subject rule.

Output:

data/processed/learner_recommendations.csv

The recommendation logic is:

If learner_mark >= minimum_required_mark:
    Recommended
Else:
    Not eligible

The script also calculates a recommendation score:

recommendation_score = learner_mark - minimum_required_mark
4. generate_sample_choices.py

Creates sample parent/learner subject choices.

Output:

data/raw/parent_subject_choices.csv

Each learner is assigned:

English
Life Orientation
Mathematics or Mathematical Literacy
Four elective subjects
5. validate_choices.py

Validates each learner's selected subjects.

Output:

data/processed/validated_subject_choices.csv
data/processed/invalid_choices.csv

The validation checks:

The learner chose exactly 7 subjects.
The learner selected English.
The learner selected Life Orientation.
The learner selected either Mathematics or Mathematical Literacy.
The learner did not select both Mathematics and Mathematical Literacy.
The learner did not select subjects they are not eligible for.



## How to Run the Project

The full project pipeline can be run with one command from the main project folder:

py scripts/run_pipeline.py

This runs all project scripts in the correct order:

1. Generate sample learner data
2. Generate subject rules
3. Generate subject recommendations
4. Generate sample parent choices
5. Validate subject choices
6. Generate subject demand report
7. Create subject demand chart
8. Generate executive summary
9. Rank learner recommendations
10. Generate invalid subject report
11. Create invalid subject chart
12. Generate KPI summary
13. Load data into SQLite database

Individual scripts can also be run separately:

py scripts/generate_sample_data.py
py scripts/generate_subject_rules.py
py scripts/recommend_subjects.py
py scripts/generate_sample_choices.py
py scripts/validate_choices.py
py scripts/generate_subject_demand_report.py
py scripts/visualise_subject_demand.py
py scripts/generate_executive_summary.py
py scripts/rank_learner_recommendations.py
py scripts/generate_invalid_subject_report.py
py scripts/visualise_invalid_subject_report.py
py scripts/generate_kpi_summary.py
py scripts/load_data_to_sqlite.py

Example Outputs
Learner Recommendation Example
Learner	Subject	Learner Mark	Required Mark	Status	Score
John Smith	Physical Sciences	78	65	Recommended	13
Sipho Dlamini	Information Technology	45	70	Not eligible	-25
Invalid Choice Example
Learner	Invalid Subject	Reason
Sipho Dlamini	Physical Sciences	Learner does not meet the minimum requirement
Michael Brown	Accounting	Learner does not meet the minimum requirement

Project Status

Current version: Version 1

The project currently supports:

Sample data generation
Subject rule generation
Subject recommendation
Parent choice simulation
Subject choice validation
Invalid choice reporting