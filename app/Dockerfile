FROM python:3.9

RUN apt-get update && \
    apt-get install -y unixodbc unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y gnupg curl && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    rm -rf /var/lib/apt/lists/*
    
# Cria um diretório para o aplicativo e configura como o diretório de trabalho
RUN mkdir /app
WORKDIR /app

# Copia os arquivos de requisitos e o aplicativo para o diretório do aplicativo
COPY requirements.txt ./
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 para permitir que o aplicativo seja acessado externamente
EXPOSE 5000

# Define o comando para iniciar o aplicativo quando o contêiner for iniciado
CMD ["python", "./app.py"]