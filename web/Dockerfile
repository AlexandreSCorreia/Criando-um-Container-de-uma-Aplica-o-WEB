FROM python:3.9
    
# Cria um diretório para o aplicativo e configura como o diretório de trabalho
RUN mkdir /app
WORKDIR /app

# Copia os arquivos de requisitos e o aplicativo para o diretório do aplicativo
COPY requirements.txt ./
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 para permitir que o aplicativo seja acessado externamente
EXPOSE 5002

# Define o comando para iniciar o aplicativo quando o contêiner for iniciado
CMD ["python", "./app.py"]