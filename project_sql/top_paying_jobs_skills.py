import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Top 10 empregos mais bem pagos e as skills de cada um
top_10_jobs = [
    {"job_id": 226942, "skills": ["SQL", "Python", "Tableau"]},
    {"job_id": 547382, "skills": ["SQL", "Python"]},
    {"job_id": 552322, "skills": ["SQL", "R", "Excel"]},
    {"job_id": 99305, "skills": ["Python", "Tableau"]},          # SQL não aparece
    {"job_id": 1021647, "skills": ["Python", "Excel"]},          # SQL não aparece
    {"job_id": 168310, "skills": ["SQL", "Python", "Tableau"]},
    {"job_id": 731368, "skills": ["SQL", "Python"]},
    {"job_id": 310660, "skills": ["SQL", "Python"]},
    {"job_id": 1749593, "skills": ["SQL", "R"]},
    {"job_id": 387860, "skills": ["SQL", "Excel"]}
]

# Contar quantos dos 10 empregos pedem cada skill
skill_counts = {}
for job in top_10_jobs:
    for skill in job["skills"]:
        skill_counts[skill] = skill_counts.get(skill, 0) + 1

# Transformar em DataFrame e ordenar
df = pd.DataFrame(list(skill_counts.items()), columns=["skill", "job_count"]).sort_values("job_count", ascending=False)

# Criar figura com fundo preto
fig, ax = plt.subplots(figsize=(10,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Top 3 skills mais claras, resto degradê escuro
colors = ["#FFD700", "#FFA500", "#FF8C00"] + sns.color_palette("magma", len(df)-3).as_hex()
sns.barplot(x="job_count", y="skill", data=df, palette=colors, ax=ax)

# Título e labels
ax.set_title("Skill Occurrence in Top 10 Highest Paying Data Analyst Jobs", fontsize=16, color='white', pad=20)
ax.set_xlabel("Number of Jobs (out of 10)", fontsize=12, color='white')
ax.set_ylabel("")
ax.tick_params(colors='white', labelsize=10)

# Remover bordas
for spine in ax.spines.values():
    spine.set_visible(False)

# Salvar gráfico
plt.tight_layout()
plt.savefig("top_10_jobs_skills_count_correct.png", dpi=300, facecolor='black')

# Mostrar gráfico
plt.show(block=True)