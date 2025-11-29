FROM python:3.12-slim

# Evita arquivos .pyc e logs presos em buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define pasta de trabalho
WORKDIR /app

# Instala dependências do sistema necessárias para compilar algumas libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Comando de entrada
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]