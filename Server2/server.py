import os
import json
from flask import Flask, request, jsonify, abort
from intern_controller import write_log_entry
app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return "running"

@app.route('/receive_data', methods=["POST"])
def receive_data():
    write_log_entry("Server2", "Empfangprozess wurde gestartet")

    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        abort(401, description="Authorization header fehlt")

    if not auth_header.startswith("Bearer "):
        abort(401, description="Ungültiges Authorization Format")

    token = auth_header.split(" ")[1]

    key_path = os.path.join(os.path.dirname(__file__), "Certs", "header_key.json")
    with open(key_path, "r") as f:
        full_api_key = json.load(f)
    header_key = full_api_key["api_key"]

    if token != header_key:
        abort(401, description="Ungültiger API Key")

    data = request.get_json()
    if not data:
        write_log_entry("Server2", "Es wurden keine Daten gesendet. Vorgang wird abgebrochen", level="ERROR")
        return jsonify("Error: keine Daten empfangen"), 400

    write_log_entry("Server2", "Daten erhalten")
    user_data_path = os.path.join(os.path.dirname(__file__), "Received_Data")
    os.makedirs(user_data_path, exist_ok=True)

    filepath = os.path.join(user_data_path, "users_received.json")
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

    write_log_entry("Server2", "Daten wurden abgespeichert", level="SUCCESS")
    return jsonify("Daten sind erfolgreich angekommen")


if __name__ == '__main__':
    cert_folder = os.path.join(os.path.dirname(__file__), "Certs")
    context = (
        os.path.join(cert_folder, "certificates.pem"),
        os.path.join(cert_folder, "key.pem"),
    )
    app.run(host='0.0.0.0', port=5000, ssl_context=context)