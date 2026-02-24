SELECT
    T3.skill_id,
    T3.skills,
    COUNT(T2.job_id) AS demand_count,
    ROUND(AVG(T1.salary_year_avg), 0) AS avg_salary
FROM job_postings_fact AS T1
INNER JOIN skills_job_dim AS T2 ON T1.job_id = T2.job_id
INNER JOIN skills_dim AS T3 ON T2.skill_id = T3.skill_id
WHERE
    job_title_short = 'Data Analyst'
    AND salary_year_avg IS NOT NULL
    AND job_work_from_home = True 
GROUP BY T3.skill_id
HAVING COUNT(T2.job_id) > 10
ORDER BY
    avg_salary DESC,
    demand_count DESC
LIMIT 25;