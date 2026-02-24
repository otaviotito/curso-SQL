/* Question: What are the most in-demand skills for data analyst?
- Join job postings to inner join table similar to query 2
- Identify the top 5 in-demand skills for a data analyst.
- Focus on all postings.
- Why? Retrieves the top 5 skills with the highest demand in the job market,
providing insights into the most valuable skills for job seekers.
*/

SELECT 
    skills,
    COUNT(T2.job_id) AS demand_count
FROM job_postings_fact AS T1

INNER JOIN skills_job_dim AS T2
ON T1.job_id = T2.job_id

INNER JOIN skills_dim AS T3
ON T2.skill_id = T3.skill_id

WHERE job_title_short = 'Data Analyst'
AND job_work_from_home = True
GROUP BY
    skills
ORDER BY
    demand_count DESC
LIMIT 5