# Dockerfile
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/app  # 👈 Aquí el truco

WORKDIR /app

RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "api/main.py"]
