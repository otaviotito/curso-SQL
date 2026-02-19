SELECT 
    COUNT(job_id) AS job_hosted_count,
    EXTRACT (MONTH FROM job_posted_date) AS month,
    EXTRACT (YEAR FROM job_posted_date) AS year
FROM
    job_postings_fact
WHERE
    job_title_short =  'Data Analyst'
GROUP BY
    job_posted_date
ORDER BY
    job_Hosted_count DESC
