# Verwende Python 3.12 Slim
FROM python:3.12-slim

# Setze Arbeitsverzeichnis
WORKDIR /app

# Kopiere Abhängigkeiten und installiere sie
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code
COPY . .

# Starte
CMD ["python", "server.py"]