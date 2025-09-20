import pandas as pd
import os
import glob

# Caminho para leitura dos arquivos
folder_path = 'src/data/raw'
output_folder = 'src/data/ready/transform'

# Garante que a pasta de destino exista antes de salvar os arquivos.
os.makedirs(output_folder, exist_ok=True)

# Lista todos os arquivos de Excel
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("Não foi possível encontrar um arquivo Excel.")

else:

    for excel_file in excel_files:

        try: # Lê todo o conteúdo dos arquivos Excel:
            df_temp = pd.read_excel(excel_file)

            # Converte a coluna "data" para datetime (caso ainda não esteja):
            df_temp["Data"] = pd.to_datetime(df_temp["Data"], errors="coerce")

            # Formata a data para o padrão Brasileiro (dia/mês/ano)
            df_temp["Data"] = df_temp["Data"].dt.strftime("%d/%m/%Y")

            # Cria uma nova coluna na tabela, chamada Valor total por Produto (quantidade vendida x preço unitário)

            if "Quantidade Vendida" in df_temp.columns and "Preco Unitario" in df_temp.columns:
                df_temp["Valor total por Produto"] = df_temp["Quantidade Vendida"] * df_temp["Preco Unitario"]

            # Cria uma nova coluna na tabela chamada Nome Completo (concatena Primeiro Nome + Sobrenome)
            if "Primeiro Nome" in df_temp.columns and "Sobrenome" in df_temp.columns:
                df_temp["Nome Completo"] = df_temp["Primeiro Nome"] + " " + df_temp["Sobrenome"]
                df_temp.drop(columns=["Primeiro Nome", "Sobrenome"], inplace=True)

            # Reorganiza a posição da nova coluna (Nome Completo) para a posição 1 (segundo coluna da esquerda para a direita)
            cols = df_temp.columns.tolist()
            if "Nome Completo" in cols:
                cols.remove("Nome Completo")
                cols.insert(1, "Nome Completo")
                df_temp = df_temp[cols]

            file_name = os.path.basename(excel_file) # Recebe o nome completo do arquivo Excel. Ex: base_vendas.xlsx
            name_without_ext = os.path.splitext(file_name)[0] # Retira apenas trecho do nome, sem a extenção. Ex: Base_devoluções

            # Fornece o novo nome para o arquivo de saída. Ex: Base_vendas_ready.xlsx
            output_file = os.path.join(output_folder, f"{name_without_ext}_ready.xlsx")

            # Salva o arquivo tratado:
            df_temp.to_excel(output_file, index=False, engine="openpyxl")

            print(f"Arquivo '{name_without_ext}' tratado e incluso na pasta 'ready'")

            # Informa erro na leitura do arquivo:
        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file} : {e}")

# Após o tratamento dos datos, executa automaticamente o pipeline de previsão de vendas para o ano de 2026 em Curitiba (prediction.py)
os.system('python src/scripts/prediction.py')