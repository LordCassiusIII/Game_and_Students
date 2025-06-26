import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o dataset (tenta caminho do usuário; senão, usa caminho interno)
try:
    df = pd.read_csv(r"c:\Users\cassi\Downloads\gameandgrade new.csv")
except FileNotFoundError:
    df = pd.read_csv("/mnt/data/gameandgrade new.csv.csv")

# 2. Criar categoria de anos de jogo
df['Playing Years Category'] = df['Playing Years'].apply(lambda x: '3+' if x >= 3 else str(x))

# 3. Estatísticas de Playing Hours por Playing Years
stats = (
    df.groupby('Playing Years Category')['Playing Hours']
      .agg(
          Média='mean',
          Mediana='median',
          Desvio_Padrão='std',
          Mínimo='min',
          Máximo='max'
      )
      .round(2)
      .reset_index()
)
stats.columns = [
    'Anos Jogando',
    'Média (h/sem)',
    'Mediana',
    'Desvio Padrão',
    'Mínimo',
    'Máximo'
]

# Impressão das perguntas e da tabela
print("\n=== Perguntas de Cássio José: ===\n")

print("=== Pergunta 1: ===")
print(
    "Qual é a distribuição do número médio de horas jogadas por semana (Playing Hours) "
    "de acordo com o número de anos que a pessoa joga (Playing Years)?\n"
    "→ Agrupe os dados por anos de experiência jogando (0, 1, 2, 3+ anos) e "
    "calcule média, mediana, desvio padrão, mínimo e máximo."
)
print("\nEstatísticas de horas jogadas por nível de experiência:\n")
print(stats.to_string(index=False, justify='center'))

# 4. Top 3 escolaridade dos pais entre quem joga
gamers = df[df['Playing Games'] == 1]

print("\n=== Pergunta 2: ===")
print(
    "Quais são os níveis mais frequentes de escolaridade dos pais entre os estudantes que jogam?\n"
    "→ Considere apenas os estudantes que jogam (Playing Games = 1), e calcule "
    "frequência absoluta e relativa dos níveis de escolaridade do pai e da mãe, "
    "identificando os três mais comuns."
)

def imprime_top3(coluna, label):
    cnt = (
        gamers[coluna]
        .value_counts()
        .rename_axis(label)
        .reset_index(name='Absoluto')
    )
    cnt['Relativo (%)'] = (cnt['Absoluto'] / cnt['Absoluto'].sum() * 100).round(2)
    top3 = cnt.nlargest(3, 'Absoluto').reset_index(drop=True)
    
    print(f"\nTop 3 escolaridade — {label}:\n")
    print(top3.to_string(index=False, justify='center'))
    return top3

top3_father = imprime_top3('Father Education', 'Pai')
top3_mother = imprime_top3('Mother Education', 'Mãe')


# ——— Gráficos ———

# Gráfico 1: Média de horas jogadas por categoria de experiência
plt.figure()
plt.bar(stats['Anos Jogando'], stats['Média (h/sem)'])
plt.title('Média de Horas Jogadas por Semana\npor Categoria de Anos Jogando')
plt.xlabel('Anos Jogando')
plt.ylabel('Média (h/sem)')
plt.tight_layout()
plt.show()

# Gráficos 2 e 3: Top 3 escolaridade dos pais
def plot_top3(top3_df, label):
    plt.figure()
    plt.bar(top3_df[label].astype(str), top3_df['Relativo (%)'])
    plt.title(f'Top 3 Escolaridade — {label}')
    plt.xlabel(label)
    plt.ylabel('Relativo (%)')
    plt.tight_layout()
    plt.show()

plot_top3(top3_father, 'Pai')
plot_top3(top3_mother, 'Mãe')

