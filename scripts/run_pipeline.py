import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


scripts_to_run = [
    "generate_sample_data.py",
    "generate_subject_rules.py",
    "recommend_subjects.py",
    "generate_sample_choices.py",
    "validate_choices.py",
    "generate_subject_demand_report.py",
    "visualise_subject_demand.py",
    "generate_executive_summary.py",
    "rank_learner_recommendations.py",
    "generate_invalid_subject_report.py",
    "visualise_invalid_subject_report.py",
    "generate_kpi_summary.py",
    "load_data_to_sqlite.py",
]


for script_name in scripts_to_run:
    script_path = BASE_DIR / "scripts" / script_name

    print("=" * 70)
    print(f"Running: {script_name}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=BASE_DIR,
        text=True,
    )

    if result.returncode != 0:
        print(f"Pipeline stopped because {script_name} failed.")
        sys.exit(result.returncode)


print("=" * 70)
print("Pipeline completed successfully.")
print("=" * 70)