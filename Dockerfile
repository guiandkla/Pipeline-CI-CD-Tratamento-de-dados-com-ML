FROM python:3.13

# Diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Instala dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código para dentro do container
COPY . .

# Cria pastas de dados (raw e ready)
RUN mkdir -p src/data/raw \
    && mkdir -p src/data/ready/transform \
    && mkdir -p src/data/ready/prediction \
    && mkdir -p src/data/scripts

# Comando que será executado ao rodar o container
CMD ["python", "main.py"]