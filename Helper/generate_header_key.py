import secrets
import json
import os

def generate_header_key() -> None:
    api_key = secrets.token_hex(32)

    certs_dir = os.path.join(os.path.dirname(__file__), "../Certs")
    os.makedirs(certs_dir, exist_ok=True)

    file_path = os.path.join(certs_dir, "header_key.json")

    with open(file_path, "w") as f:
        json.dump({"api_key": api_key}, f, indent=4)

    print("Neuer api_key generiert")

generate_header_key()