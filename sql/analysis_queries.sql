-- School Subject Choice Recommendation System
-- SQL Analysis Queries


-- 1. View all learners
SELECT *
FROM learners
LIMIT 10;


-- 2. Count total learners
SELECT COUNT(*) AS total_learners
FROM learners;


-- 3. Count valid vs invalid subject packages
SELECT
    status,
    COUNT(*) AS number_of_learners
FROM validated_subject_choices
GROUP BY status;


-- 4. Show subject demand from highest to lowest
SELECT
    subject,
    number_of_learners
FROM subject_demand_report
ORDER BY number_of_learners DESC;


-- 5. Show subjects with the most invalid selections
SELECT
    invalid_subject,
    number_of_invalid_choices
FROM invalid_subject_report
ORDER BY number_of_invalid_choices DESC;


-- 6. Find learners with invalid subject choices
SELECT
    student_id,
    name,
    status,
    issues
FROM validated_subject_choices
WHERE status = 'Invalid';


-- 7. Show detailed invalid choices
SELECT
    student_id,
    name,
    invalid_subject,
    reason
FROM invalid_choices
ORDER BY invalid_subject, name;


-- 8. Show top 5 elective recommendations for each learner
SELECT
    student_id,
    name,
    subject,
    recommendation_score,
    elective_recommendation_rank
FROM ranked_learner_recommendations
WHERE elective_recommendation_rank <= 5
ORDER BY student_id, elective_recommendation_rank;


-- 9. Find learners recommended for Information Technology
SELECT
    student_id,
    name,
    learner_mark,
    minimum_required_mark,
    recommendation_score
FROM learner_recommendations
WHERE subject = 'Information Technology'
  AND status = 'Recommended'
ORDER BY recommendation_score DESC;


-- 10. Find learners who selected Physical Sciences but were not eligible
SELECT
    student_id,
    name,
    invalid_subject,
    reason
FROM invalid_choices
WHERE invalid_subject = 'Physical Sciences'
ORDER BY name;