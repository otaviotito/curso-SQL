import pandas as pd
import matplotlib.pyplot as plt

# Dados fornecidos (top 10)
data = [
    {"skill": "go", "demand_count": 27, "avg_salary": 115320},
    {"skill": "confluence", "demand_count": 11, "avg_salary": 114210},
    {"skill": "hadoop", "demand_count": 22, "avg_salary": 113193},
    {"skill": "snowflake", "demand_count": 37, "avg_salary": 112948},
    {"skill": "azure", "demand_count": 34, "avg_salary": 111225},
    {"skill": "bigquery", "demand_count": 13, "avg_salary": 109654},
    {"skill": "aws", "demand_count": 32, "avg_salary": 108317},
    {"skill": "java", "demand_count": 17, "avg_salary": 106906},
    {"skill": "ssis", "demand_count": 12, "avg_salary": 106683},
    {"skill": "jira", "demand_count": 20, "avg_salary": 104918}
]

# Criar DataFrame e renomear colunas
df = pd.DataFrame(data)
df = df.rename(columns={
    "skill": "Skills",
    "demand_count": "Demand Count",
    "avg_salary": "Average Salary ($)"
})

# Criar figura pequena, sem margens extras
fig, ax = plt.subplots()

ax.axis('off')  # esconder eixos

# Criar tabela
table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center'
)

# Ajustar fonte e escala
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.2)

# Estilizar cores
for key, cell in table.get_celld().items():
    if key[0] == 0:
        cell.set_facecolor("#333333")
        cell.set_text_props(weight='bold', color='white')
    else:
        cell.set_facecolor("#1a1a1a")
        cell.set_text_props(color='white')

# Salvar tabela **apertada ao redor**, transparente
plt.savefig(
    "most_optimal_skills_top10_table_final.png",
    dpi=300,
    bbox_inches='tight',
    pad_inches=0,
    transparent=True
)
plt.close(fig)