/*
Answer: What are the top skills based on salary?
- Look at the average salary associated wich each skill for Data Analyst positions
- Focused on roles with specified salaries, regardless of location
- Why? It reveals how differente skills impact salary for Data Analyst and
 helps identify the most financially rewarding skills to acquire or improve
 */

 SELECT 
    skills,
    ROUND(AVG(salary_year_avg),0) AS avg_salary
FROM job_postings_fact AS T1

INNER JOIN skills_job_dim AS T2
ON T1.job_id = T2.job_id

INNER JOIN skills_dim AS T3
ON T2.skill_id = T3.skill_id

WHERE job_title_short = 'Data Analyst'
AND salary_year_avg IS NOT NULL
and job_work_from_home = True
GROUP BY
    skills
ORDER BY
    avg_salary DESC
LIMIT 10