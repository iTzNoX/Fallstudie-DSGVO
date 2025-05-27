import subprocess
import os

SERVER1_URL = "https://localhost:5001"
SERVER2_URL = "https://localhost:5002"

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

copy_received_data_from_container("server2")