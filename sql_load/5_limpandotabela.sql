-- tabela temporária para importar tudo cru
CREATE TEMP TABLE skills_job_dim_staging (
    job_id INT,
    skill_id INT
);

\copy skills_job_dim_staging 
FROM 'C:\Users\rccur\Downloads\skills_job_dim.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8');