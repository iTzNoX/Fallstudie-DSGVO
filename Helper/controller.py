import requests
import subprocess
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

def copy_received_data_from_container(container_name):
    container_path = "/app/Received_Data/users_received.json"
    local_path = os.path.join(os.path.dirname(os.getcwd()), "Server2", "Received_Data")

    try:
        subprocess.run(
            ["docker", "cp", f"{container_name}:{container_path}", local_path],
            check = True)

        print("Ordner im Container wurde erfolgreich ins Projekt kopiert")

    except subprocess.CalledProcessError as e:
        print(str(e))

    except Exception as e:
        print(str(e))

def copy_logs_from_container(container_name, local):
    container_path = "/app/Logs"
    local_path = local

    os.makedirs(local_path, exist_ok=True)

    try:
        subprocess.run(
            ["docker", "cp", f"{container_name}:{container_path}/.", local_path],
            check=True)

        print(f"Logs-Ordner für {container_name} wurde erfolgreich aus dem Container kopiert.")

    except subprocess.CalledProcessError as e:
        print(str(e))
    except Exception as e:
        print(str(e))


send_data()
copy_received_data_from_container("server2")
copy_logs_from_container("server1", "../Server1/Logs")
copy_logs_from_container("server2", "../Server2/Logs")