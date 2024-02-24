# Use a imagem base
FROM python:3.11-slim

# Copie seus arquivos de código-fonte para o contêiner
COPY /app /app

# Defina o diretório de trabalho no contêiner
WORKDIR /app

EXPOSE 8080

# Instale quaisquer dependências ou pacotes necessários
RUN apt-get update && apt-get install -y bash
RUN pip install -r requirements.txt

# Comando a ser executado ao iniciar o contêiner
CMD ["python3", "app.py"]