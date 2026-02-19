SELECT 
    T1.job_title_short,
    T1.job_location,
    T1.job_via,
    T1.job_posted_date,
    T1.salary_year_avg
FROM (
    SELECT *
    FROM january_jobs
    UNION ALL
    SELECT *
    FROM february_jobs
    UNION ALL
    SELECT *
    FROM march_jobs
) AS T1

WHERE T1.salary_year_avg > 70000
AND T1.job_title_short =  'Data Analyst'
ORDER BY T1.salary_year_avg DESC