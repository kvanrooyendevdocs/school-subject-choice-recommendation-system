import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)


recommendations_path = PROCESSED_DATA_DIR / "learner_recommendations.csv"

recommendations_df = pd.read_csv(recommendations_path)


recommended_subjects_df = recommendations_df[
    recommendations_df["status"] == "Recommended"
].copy()


recommended_subjects_df = recommended_subjects_df.sort_values(
    by=["student_id", "recommendation_score"],
    ascending=[True, False]
)


recommended_subjects_df["recommendation_rank"] = (
    recommended_subjects_df
    .groupby("student_id")
    .cumcount() + 1
)


ranked_recommendations_path = (
    PROCESSED_DATA_DIR / "ranked_learner_recommendations.csv"
)

recommended_subjects_df.to_csv(ranked_recommendations_path, index=False)


elective_recommendations_df = recommended_subjects_df[
    ~recommended_subjects_df["subject"].isin(
        ["English", "Life Orientation", "Mathematics", "Mathematical Literacy"]
    )
].copy()


elective_recommendations_df["elective_recommendation_rank"] = (
    elective_recommendations_df
    .groupby("student_id")
    .cumcount() + 1
)


top_5_recommendations_df = elective_recommendations_df[
    elective_recommendations_df["elective_recommendation_rank"] <= 5
].copy()


top_5_report_path = REPORTS_DIR / "top_5_recommendations_per_learner.csv"

top_5_recommendations_df.to_csv(top_5_report_path, index=False)


print(f"Ranked learner recommendations saved at: {ranked_recommendations_path}")
print(f"Top 5 recommendations report saved at: {top_5_report_path}")
print(top_5_recommendations_df.head(25))