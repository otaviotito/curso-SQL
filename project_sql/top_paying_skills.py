import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados das top 10 skills por salário
data = [
    {"skill": "pyspark", "avg_salary": 208172},
    {"skill": "bitbucket", "avg_salary": 189155},
    {"skill": "couchbase", "avg_salary": 160515},
    {"skill": "watson", "avg_salary": 160515},
    {"skill": "datarobot", "avg_salary": 155486},
    {"skill": "gitlab", "avg_salary": 154500},
    {"skill": "swift", "avg_salary": 153750},
    {"skill": "jupyter", "avg_salary": 152777},
    {"skill": "pandas", "avg_salary": 151821},
    {"skill": "elasticsearch", "avg_salary": 145000}
]

# Criar DataFrame e ordenar do menor para o maior para gráfico vertical
df = pd.DataFrame(data).sort_values("avg_salary", ascending=False)

# Criar figura com fundo preto
fig, ax = plt.subplots(figsize=(10,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Top 3 skills mais claras, resto degradê escuro
colors = ["#FFD700", "#FFA500", "#FF8C00"] + sns.color_palette("magma", len(df)-3).as_hex()
sns.barplot(x="skill", y="avg_salary", data=df, palette=colors, ax=ax)

# Adicionar valores de salário acima das barras
for i, val in enumerate(df["avg_salary"]):
    ax.text(i, val + 2000, f"${val:,.0f}", color='white', ha='center', fontweight='bold')

# Título e labels
ax.set_title("Top 10 Highest Paying Skills for Data Analysts (2023)", fontsize=16, color='white', pad=20)
ax.set_xlabel("Skill", fontsize=12, color='white')
ax.set_ylabel("Average Salary (USD)", fontsize=12, color='white')
ax.tick_params(colors='white', labelsize=10)

# Remover bordas
for spine in ax.spines.values():
    spine.set_visible(False)

# Salvar gráfico
plt.tight_layout()
plt.savefig("skills_based_on_salary.png", dpi=300, facecolor='black')

# Mostrar gráfico
plt.show(block=True)