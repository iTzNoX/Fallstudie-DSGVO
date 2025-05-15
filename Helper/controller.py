import requests

SERVER1_URL = "http://localhost:5001"

def send_data():
    url = f"{SERVER1_URL}/send_data"
    try:
        response = requests.post(url)
        response.raise_for_status()
        print("Daten wurden erfolgreich verschickt")
        return response.json()
    except Exception as e:
        print(e)
        return None

send_data()