import subprocess
import os

SERVER1_URL = "https://localhost:5001"
SERVER2_URL = "https://localhost:5002"

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

copy_logs_from_container("server1", "../Server1/Logs")
copy_logs_from_container("server2", "../Server2/Logs")