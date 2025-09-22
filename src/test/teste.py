import pandas as pd
import calendar

# Teste 1: Testa se o script cria corretamente "Dia", "Mes" e "Ano".
def teste_criar_data():

    # Dados informados para teste
    data = {"Data": ["01/01/2024", "17/02/2025", "18/3/2026"], "Loja": ["Curitiba", "Curitiba", "Curitiba"]}
    df_teste1 = pd.DataFrame(data)

    # Simula a criação das colunas de data
    df_teste1["Data"] = pd.to_datetime(df_teste1["Data"], dayfirst=True)
    df_teste1["Dia"] = df_teste1["Data"].dt.day
    df_teste1["Mes"] = df_teste1["Data"].dt.month
    df_teste1["Ano"] = df_teste1["Data"].dt.year

    # Asserções para verificar se os valores estão corretos
    assert list(df_teste1["Dia"]) == [1, 17, 18]
    assert list(df_teste1["Mes"]) == [1, 2, 3]
    assert list(df_teste1["Ano"]) == [2024, 2025, 2026]


# Teste 2: Verificando o cálculo do valor total
def teste_calculo_valor_total():

    # Dados de teste
    dados_teste = pd.DataFrame({
        "Preco Unitario": [10, 20, 30],
        "Quantidade Vendida": [2, 3, 4]
    })

    # Calcula o valor total
    dados_teste["Valor total por Produto"] = dados_teste["Preco Unitario"] * dados_teste["Quantidade Vendida"]

    # Valores esperados
    valores_esperados = [20, 60, 120]

    # Verifica se o resultado está correto
    assert list(dados_teste["Valor total por Produto"]) == valores_esperados

# Teste 3: Verifica a criação do DataFrame de previsão
def teste_criar_dataframe_previsao():

    # Simula a criação do DataFrame de previsão
    novas_datas = []
    for mes in range(1, 13):
        for dia in range(1, calendar.monthrange(2026, mes)[1]+1):
            novas_datas.append({
                "Dia": dia,
                "Mes": mes,
                "Ano": 2026,
            })
    df_previsao = pd.DataFrame(novas_datas)
    
    # Informa a quantidade de dias (do ano)
    assert len(df_previsao) == 365

# Teste 4: Testa o filtro de lojas
def teste_filtro_lojas():

    # Lojas informadas para teste
    df_teste4 = pd.DataFrame({"Loja": ["Maringá", "Curitiba", "São José dos Pinhais"]})
 
    # Faz o filtro da loja igual está no código original (prediction.py)
    df_curitiba = df_teste4[df_teste4["Loja"] == "Curitiba"].copy()

    # Testa se o filtro está funcionando
    assert list(df_curitiba["Loja"] == "Curitiba")

# Teste 5: Verifica a agregação e formatação
def teste_agrupar_e_formatar_resumo_mensal():

    # Cria um DataFrame de teste
    dados = {
        "Mes": [1, 1, 2, 2],
        "Ano": [2026, 2026, 2026, 2026],
        "Quantidade Vendida": [10, 20, 30, 40],
        "Valor total previsto": [100.5, 200.5, 300.5, 400.5]
    }
    df_previsao = pd.DataFrame(dados)

    # Simula a agregação
    resumo_mensal = df_previsao.groupby(["Mes", "Ano"]).agg({
        "Quantidade Vendida": "sum",
        "Valor total previsto": "sum"
    }).reset_index()

    # Formata valores
    resumo_mensal["Valor total previsto"] = resumo_mensal["Valor total previsto"].map("R$ {:,.2f}".format)
    resumo_mensal["Quantidade Vendida"] = resumo_mensal["Quantidade Vendida"].astype(int)
    
    # Testa se a agregação e formatação está funcionando
    assert len(resumo_mensal) == 2
    assert list(resumo_mensal["Quantidade Vendida"]) == [30, 70]
    assert list(resumo_mensal["Valor total previsto"]) == ["R$ 301.00", "R$ 701.00"]