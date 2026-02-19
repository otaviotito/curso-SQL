WITH company_job_count AS (
    SELECT
        company_id,
        COUNT(*) AS total_jobs
    FROM
        job_postings_fact
    GROUP BY
        company_id
)

SELECT 
    T1.name AS company_name,
    T2.total_jobs

FROM 
    company_dim AS T1
LEFT JOIN company_job_count AS T2
ON T2.company_id = T1.company_id
ORDER BY
    total_jobs DESC