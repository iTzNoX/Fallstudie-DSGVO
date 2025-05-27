import requests
import os

SERVER1_URL = "https://localhost:5001"
SERVER2_URL = "https://localhost:5002"

def send_data():
    url = f"{SERVER1_URL}/send_data"
    cert_path = os.path.join(os.path.dirname(__file__), "../Certs", "certificates.pem")

    try:
        response = requests.post(url, verify=cert_path)
        print(f"Status Code von Server1: {response.status_code}")
        print(f"Response-Text von Server1: {response.text}")

        response.raise_for_status()

        try:
            return response.json()
        except Exception:
            print("Antwort von Server1 ist kein JSON")
            return response.text

    except requests.exceptions.RequestException as e:
        print(e)
        return None

send_data()