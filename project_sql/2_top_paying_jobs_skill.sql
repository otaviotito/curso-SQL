/*
Question: What skills are required for the top-paying data analyst jobs?
- Use the top 10 highest-paying Data Analyst jobs from the first query
- Add the specific skills required for these roles
- Why? It provides a detailed look at which high-paying jobs demand certain skills,
    helping job seekers understand which skills to develop to align with top salaries
*/

WITH top_paying_jobs AS (

SELECT
    job_id,
    job_title,
    salary_year_avg,
    name AS company_name
FROM
    job_postings_fact AS T1
LEFT JOIN company_dim AS T2
ON T1.company_id = T2.company_id
WHERE
    job_title_short = 'Data Analyst' AND
    job_location = 'Anywhere' AND
    salary_year_avg IS NOT NULL
ORDER BY salary_year_avg DESC
LIMIT 10
)

SELECT 
    T1.*,
    T3.skills
FROM top_paying_jobs AS T1

INNER JOIN skills_job_dim AS T2
ON T1.job_id = T2.job_id

INNER JOIN skills_dim AS T3
ON T2.skill_id = T3.skill_id

ORDER BY salary_year_avg DESC