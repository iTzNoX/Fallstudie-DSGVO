# DSGVO-konforme Datenübertragungssoftware

## Projektübersicht

Dieses Projekt entstand im Rahmen einer Fallstudie zur Bachelorarbeit. Ziel war die Entwicklung und Evaluation einer 
einfachen Softwarelösung zur DSGVO-konformen Übertragung personenbezogener Daten zwischen zwei Serverinstanzen. Dabei 
lag der Fokus auf praxisnahe Herausforderungen, wie sie insbesondere in kleinen Unternehmen ohne spezialisiertes 
IT-Personal auftreten können.

## Zielsetzung

- Entwicklung einer abgesicherten Datenübertragung zwischen zwei Servern  
- Implementierung grundlegender DSGVO-relevanter Maßnahmen  
- Identifikation von Umsetzungs- und Verständnisschwierigkeiten  
- Analyse des Prozesses aus Perspektive kleiner Unternehmen  

## Technologien

- Python 3.12  
- Flask  
- Docker  
- cryptography  
- requests  
- pytest  
- faker  

## Setup zur Ausführung

### 1. Zertifikate und API-Key generieren

```bash
python Certs/generate_certificate.py  
python Certs/generate_header_key.py
```

### 2. Testdaten generieren

```bash
python Helper/DataGenerator.py
```

*(Die voreingestellte run Option kann genutzt werden, um Schritt 3 und 4 zu überspringen)*

### 3. Docker Container generieren

```bash
cd Server1  
docker build -t server1 .

cd ../Server2  
docker build -t server2 .
```

### 4. Docker Container starten

```bash
docker run -d -p 5001:5000 --name server1 server1  
docker run -d -p 5002:5000 --name server2 server2
```

### 5. Datenübertragung starten

```bash
python Helper/controller.py
```

Falls Fehler auftreten, können die Tests genutzt werden, um die Verschlüsselung zu überprüfen.  
Siehe: [`Tests/TLS/Connection.py`](Tests/TLS/Connection.py)

---

Die Server sind anschließend nach dem Starten unter folgenden Links zum kontrollieren erreichbar:

**Server1:**  
https://localhost:5001/

**Server2:**  
https://localhost:5002/