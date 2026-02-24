import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados
data = [
    {"job_title": "Data Analyst", "company": "Mantys", "salary": 650000},
    {"job_title": "Director of Analytics", "company": "Meta", "salary": 336500},
    {"job_title": "Associate Director - Data Insights", "company": "AT&T", "salary": 255829},
    {"job_title": "Data Analyst, Marketing", "company": "Pinterest", "salary": 232423},
    {"job_title": "Data Analyst (Hybrid/Remote)", "company": "UCLA Health", "salary": 217000},
    {"job_title": "Principal Data Analyst (Remote)", "company": "SmartAsset", "salary": 205000},
    {"job_title": "Director, Data Analyst - Hybrid", "company": "Inclusively", "salary": 189309},
    {"job_title": "Principal Data Analyst, AV Performance", "company": "Motional", "salary": 189000},
    {"job_title": "Principal Data Analyst", "company": "SmartAsset", "salary": 186000},
    {"job_title": "ERM Data Analyst", "company": "Get It Recruit", "salary": 184000}
]

df = pd.DataFrame(data).sort_values("salary", ascending=False)

# Criar figura com fundo preto
fig, ax = plt.subplots(figsize=(12,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Cores: primeiros 3 mais claros, o resto degradê escuro
colors = ["#FFD700", "#FFA500", "#FF8C00"] + sns.color_palette("magma", len(df)-3).as_hex()
sns.barplot(x="salary", y="job_title", data=df, palette=colors, ax=ax)

# Texto e títulos em branco
ax.set_title("Top 10 Highest Paying Remote Data Analyst Roles (2023)", fontsize=16, color='white', pad=20)
ax.set_xlabel("Average Salary (USD)", fontsize=12, color='white')
ax.set_ylabel("")
ax.tick_params(colors='white', labelsize=10)

# Remover spines (bordas) para cleaner look
for spine in ax.spines.values():
    spine.set_visible(False)

# Salvar imagem final
plt.tight_layout()
plt.savefig("top_paying_roles_highlight.png", dpi=300, facecolor='black')
plt.show()