# Introduction

This project explores the data analyst job market using SQL, focusing on compensation, demand, and skill trends. The goal was to understand which skills drive higher salaries and which are most valuable in today’s market.

All analysis was performed using PostgreSQL on a dataset containing job postings, salary data, locations, and required skills.

SQL queries used in this project can be found in the: [project_sql folder](/project_sql/)
# Background

As someone interested in building a strong career in data analytics, I wanted to better understand:

- Where are the highest-paying opportunities?

- What skills do those roles require?

- Which skills are most in demand?

- Which skills offer the best balance between salary and demand?

The dataset used in this project comes from a SQL course and includes structured job posting data across multiple companies and locations.

# Tools i used

Tools Used

- SQL – Core tool for querying and analyzing the dataset

- PostgreSQL – Database system used for managing the data

- VS Code – Writing and executing SQL scripts

- Git & GitHub – Version control and project documentation

# The Analysis

## 1️⃣ Top Paying Data Analyst Roles

Identified the highest-paying remote Data Analyst positions by filtering for non-null salaries and sorting by average annual salary.

🗄️ SQL snippet:
```sql
SELECT
    job_id,
    job_title,
    job_location,
    job_schedule_type,
    salary_year_avg,
    job_posted_date,
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
LIMIT 10;
```
🔑 Key Insights:

- Salary ranges from $184,000 to $650,000

- Companies include Mantys, Meta, AT&T, Pinterest, SmartAsset

- Variety of roles from Data Analyst to Director of Analytics

📈 Graph:

![Top Paying Jobs](Assets\top_paying_roles.png)

## 2️⃣ Skills for Top Paying Jobs

This analysis identifies the skills most required for the top-paying Data Analyst roles.

🗄️ SQL snippet:
```sql
WITH top_paying_jobs AS (
    SELECT	
        job_id,
        job_title,
        salary_year_avg,
        name AS company_name
    FROM
        job_postings_fact
    LEFT JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
    WHERE
        job_title_short = 'Data Analyst' AND 
        job_location = 'Anywhere' AND 
        salary_year_avg IS NOT NULL
    ORDER BY
        salary_year_avg DESC
    LIMIT 10
)
SELECT 
    top_paying_jobs.*,
    skills
FROM top_paying_jobs
INNER JOIN skills_job_dim ON top_paying_jobs.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
ORDER BY
    salary_year_avg DESC;
```
🔑 Key Insights:

- SQL appears in 8 out of the 10 top-paying roles.

- Python appears in 7 roles.

- Tableau appears in 6 roles.

- Other skills like R, Snowflake, Pandas, and Excel are also valued.


📈 Graph:

![Top Paying Jobs Skills](Assets\top_paying_jobs_skills.png)

## 3️⃣ In-Demand Skills for Data Analysts

This analysis identifies the skills most frequently requested in Data Analyst job postings, highlighting what employers value most for remote positions.

🗄️ SQL Snippet:
```
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
```
🔑 Key Insights

- SQL and Excel are fundamental, highlighting strong demand for foundational data skills.

- Python, Tableau, and Power BI are highly requested, showing the importance of programming and visualization tools.

- Focusing on these skills will align your profile with the most in-demand requirements in 2023.

📊 Graph:

![Top Demanding Skills](Assets\top_demanding_skills.png)

## 4️⃣ Skills Based on Salary

This analysis explores the average salaries associated with different skills, revealing which skills command the highest pay for Data Analysts.

🗄️ SQL Snippet:
```
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
```
🔑 Key Insights

Specialized skills like PySpark, Bitbucket, Couchbase, DataRobot, and Jupyter are associated with the highest average salaries, highlighting the premium on big data, machine learning, and predictive modeling expertise.

Skills related to software development and deployment (GitLab, Swift) indicate that proficiency in automation and efficient data pipelines is highly valued.

Cloud and data engineering tools (Elasticsearch) show the growing importance of cloud analytics environments in maximizing earning potential.

📊 Graph:
![Top Paying Skills](Assets\top_paying_skills.png)

## 5️⃣ Most Optimal Skills to Learn

This analysis combines insights from demand and salary data to identify skills that are both highly requested and offer higher average salaries, helping Data Analysts focus on skills that maximize career value.

🗄️ SQL Snippet:
```
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
```
🔑 Key Insights

High-Demand Programming Languages: Python and R are widely required, with demand counts of 236 and 148 respectively, and average salaries around $101k, showing foundational importance.

Cloud Tools & Technologies: Snowflake, Azure, AWS, and BigQuery show significant demand and higher average salaries, highlighting the growing importance of cloud and big data skills.

Business Intelligence & Visualization Tools: Tableau and Looker are in high demand, with salaries ranging from $99k to $104k, emphasizing the value of visualization and BI expertise.

Database Technologies: SQL Server, Oracle, and NoSQL skills are consistently sought after, demonstrating the ongoing need for robust data storage and retrieval skills.

📊 Graph:

![Optimal Skills to Learn](Assets\optimal_skills.png)
# What i Learned

During this project, I really leveled up my SQL and data analysis skills:

Advanced Query Crafting 🧩: Learned to write complex queries with multiple joins and temporary tables (WITH clauses), which allowed me to explore patterns across job postings and skills effectively.

Data Aggregation Mastery 📊: Got very comfortable using GROUP BY, COUNT(), and AVG() to summarize large datasets and uncover insights from millions of job postings.

Analytical Thinking 💡: Turned real-world questions into structured SQL queries, learning how to interpret results and extract actionable insights, like which skills are in high demand and which are associated with higher salaries.

# Conclusions

📌 Conclusions & Insights

From analyzing the data analyst job market, several patterns became clear:

- Top-Paying Data Analyst Jobs: Remote roles can offer a wide salary range, up to $650,000. Companies value experience and technical expertise highly.

- Skills for High Salaries: Proficiency in SQL, Python, and specialized tools like PySpark or cloud platforms correlates with higher average salaries.

- Most In-Demand Skills: SQL and Excel remain essential; Python, Tableau, and Power BI are increasingly required for modern data analysis.

- Optimal Skills for Career Growth: Combining demand and compensation data, learning top skills like SQL, Python, cloud tools, and visualization platforms positions a candidate competitively.

Takeaways:

- Foundational skills matter, but specialized technical skills create a salary premium.

- Focusing on both high-demand and high-paying skills can accelerate career growth.

- Regularly reviewing market trends helps align learning with industry needs.

- This project was a practical exercise in turning data into insights, enhancing both technical SQL skills and strategic understanding of the data analyst job market.