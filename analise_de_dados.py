import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Criação dos dataframes a partir das planilhas
gabarito_df = pd.read_excel('input/Gabarito.xlsx')
respostas_alunos_df = pd.read_excel('input/Respostas.xlsx')

# Renomeando uma coluna para facilitar
gabarito_df.rename(columns={'Questão': 'num_exercicio'}, inplace=True)

# Adicionando uma nova coluna ao dataframe utilizado para facilitar
novo_df = respostas_alunos_df.merge(gabarito_df, on='num_exercicio')

# Verificando respostas dos alunos com o gabarito
novo_df['acertos'] = novo_df['resp_aluno'] == novo_df['Gabarito'].str.lower()

# Total de acertos por aluno
acertos_por_aluno = novo_df.groupby('aluno_nome')['acertos'].sum()

# Percentual de acertos por aluno
percentual_acertos_por_aluno = novo_df.groupby('aluno_nome')['acertos'].mean() * 100
resultado_formatado = percentual_acertos_por_aluno.apply(lambda x: f"{x:.2f}%")

# Média de acertos por aluno
media_acertos_por_aluno = novo_df.groupby('aluno_nome')['acertos'].mean()

total_acertos_geral = novo_df['acertos'].sum()
total_questoes = gabarito_df['num_exercicio'].nunique()
total_alunos = novo_df['aluno_nome'].nunique()

# Percentual de acertos geral
percentual_acertos_geral = total_acertos_geral / (total_questoes * total_alunos) * 100

# Média de acertos geral
media_acertos_geral = total_acertos_geral / (total_questoes * total_alunos)

# Criando novos dataframes com os resultados
resultado_geral = {
    'percentual_acertos_geral': f"{round(percentual_acertos_geral, 2)}%",
    'media_acertos_geral': media_acertos_geral,
    'total_acertos': total_acertos_geral,
}

resultados_alunos = {
    'percentual_acertos': resultado_formatado,
    'media_de_acertos': media_acertos_por_aluno,
    'total_acertos': acertos_por_aluno,
}

resultados_alunos = pd.DataFrame(resultados_alunos)
resultado_geral = pd.DataFrame(resultado_geral, index=[0])

# Output no console
print(resultados_alunos)
print(resultado_geral)

# Criando uma nova planilha como o output

resultados_alunos.to_excel("output/resultados_alunos.xlsx")
resultado_geral.to_excel("output/resultado_geral.xlsx")
