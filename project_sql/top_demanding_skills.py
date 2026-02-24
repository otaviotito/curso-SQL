import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados fornecidos
data = [
    {"skill": "SQL", "demand_count": 7291},
    {"skill": "Excel", "demand_count": 4611},
    {"skill": "Python", "demand_count": 4330},
    {"skill": "Tableau", "demand_count": 3745},
    {"skill": "Power BI", "demand_count": 2609}
]

# Criar DataFrame e ordenar do mais demandado para o menos
df = pd.DataFrame(data).sort_values("demand_count", ascending=False)

# Criar figura com fundo preto
fig, ax = plt.subplots(figsize=(8,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Top 3 skills mais claras, resto degradê escuro
colors = ["#FFD700", "#FFA500", "#FF8C00"] + sns.color_palette("magma", len(df)-3).as_hex()
sns.barplot(x="skill", y="demand_count", data=df, palette=colors, ax=ax)

# Adicionar números absolutos acima das barras
for i, val in enumerate(df["demand_count"]):
    ax.text(i, val + 100, str(val), color='white', ha='center', fontweight='bold')

# Título e labels
ax.set_title("Top 5 In-Demand Skills for Data Analysts (2023)", fontsize=16, color='white', pad=20)
ax.set_xlabel("Skill", fontsize=12, color='white')
ax.set_ylabel("")  # remove label do eixo Y

# Remover ticks e valores do eixo Y
ax.set_yticks([])

ax.tick_params(colors='white', labelsize=10)

# Remover bordas
for spine in ax.spines.values():
    spine.set_visible(False)

# Salvar gráfico
plt.tight_layout()
plt.savefig("in_demand_skills_vertical_no_yticks.png", dpi=300, facecolor='black')

# Mostrar gráfico
plt.show(block=True)