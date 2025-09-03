# 📊 Pipeline CI/CD com Tratamento de Dados e Machine Learning

Atividade **Somativa 1 - DevOps** do curso de **Análise e Desenvolvimento de Sistemas - PUCPR/EAD**.

## 👨‍🎓 Aluno
- **Guilherme Andrei Klabunde**

## 📝 Descrição da atividade
Esta atividade consiste na criação de um **pipeline CI/CD** (Continuous Integration e Continuous Delivery/Deploy), utilizando **Docker** para conteinerização e publicação da imagem no **Docker Hub**.  

O sistema foi desenvolvido para realizar:
- Tratamento de dados em planilhas Excel.  
- Padronização e organização dos dados para criação de dashboards.  
- Previsão de vendas por meio de **Machine Learning (Regressão)**.  

## 🛠️ Tecnologias utilizadas
- Python 3.13  
- Scikit-Learn  
- Pandas  
- Openpyxl  
- Docker  
- Git  

## 📂 Descrição do Sistema
Muitas empresas ainda utilizam o **Excel** para o controle de vendas, contratos e outros dados.  
Com o crescimento do negócio, aumenta também o número de planilhas, o que pode resultar em **excesso de arquivos** e **perda de informações estratégicas**.  

Este sistema foi desenvolvido para:  
- Tratar os dados de planilhas Excel.  
- Padronizar informações.  
- Criar uma nova planilha organizada e pronta para análise.  
- Utilizar **Machine Learning** para prever as vendas de uma loja fictícia em **Curitiba-PR**, no ano de 2026.  

> ⚠️ Observação: a previsão pode ser melhorada com um volume maior de dados, visto que o conjunto utilizado é limitado.  

## ⚙️ Funcionalidades do Sistema
1. O sistema lê planilhas Excel (`.xlsx`) da pasta **Data Raw** (dados brutos).  
2. Padroniza as informações e cria uma nova coluna com o **valor total de vendas**.  
3. Salva as planilhas tratadas na pasta **Data Ready**.  
4. Executa automaticamente o algoritmo de **Machine Learning** para prever vendas em 2026.  
5. Salva o resultado final na pasta **Prediction**.  
6. Finaliza o processo.
