import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import locale
import calendar

# Pastas
input_file = 'src/data/ready/transform/base_vendas_ready.xlsx'
output_folder = 'src/data/ready/prediction'
os.makedirs(output_folder, exist_ok=True)

# Lê o arquivo tratado
df = pd.read_excel(input_file)

# Filtra apenas Curitiba
df_curitiba = df[df["Loja"] == "Curitiba"].copy()

# Cria features da data
df_curitiba["Data"] = pd.to_datetime(df["Data"], dayfirst=True)
df_curitiba["Dia"] = df_curitiba["Data"].dt.day
df_curitiba["Mes"] = df_curitiba["Data"].dt.month
df_curitiba["Ano"] = df_curitiba["Data"].dt.year

# Variáveis explicativas e alvo
X = df_curitiba[["Dia", "Mes", "Ano", "Preco Unitario", "Quantidade Vendida"]]
y = df_curitiba["Valor total por Produto"]

# Treina modelo de regressão linear
model = LinearRegression()
model.fit(X, y)


novas_datas = []
for mes in range(1, 13):
    for dia in range(1, calendar.monthrange(2026, mes)[1]+1):
        novas_datas.append({
            "Dia": dia,
            "Mes": mes,
            "Ano": 2026,
            # Para simplificação: preço e quantidade média histórica
            "Preco Unitario": X["Preco Unitario"].mean(),
            "Quantidade Vendida": X["Quantidade Vendida"].mean()
        })

df_previsao = pd.DataFrame(novas_datas)

# Faz previsão diária
df_previsao["Valor total previsto"] = model.predict(df_previsao[["Dia","Mes","Ano","Preco Unitario","Quantidade Vendida"]])

# Agrupar por mês e ano
resumo_mensal = df_previsao.groupby(["Mes", "Ano"]).agg({
    "Quantidade Vendida": "sum",
    "Valor total previsto": "sum"
}).reset_index()

resumo_mensal["Mês"] = resumo_mensal["Mes"].apply(lambda x: calendar.month_name[x])

# Reordena colunas para ficar mais claro
resumo_mensal = resumo_mensal[["Mês", "Ano", "Quantidade Vendida", "Valor total previsto"]]

# Formata valores
resumo_mensal["Valor total previsto"] = resumo_mensal["Valor total previsto"].map("R$ {:,.2f}".format)
resumo_mensal["Quantidade Vendida"] = resumo_mensal["Quantidade Vendida"].astype(int)

# Salva Excel final
output_file = os.path.join(output_folder, "previsao_vendas_2026.xlsx")
resumo_mensal.to_excel(output_file, index=False, engine="openpyxl")

output_file = os.path.basename(output_file)
name_without_ext = os.path.splitext(output_file)[0]

print(f"Arquivo '{name_without_ext}' pronto e disponível na pasta 'prediction'")