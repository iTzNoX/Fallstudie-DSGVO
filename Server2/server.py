import os
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return "running"

@app.route('/receive_data', methods=["POST"])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify("Error: keine Daten empfangen"), 400

    user_data_path = os.path.join(os.path.dirname(__file__), "Received_Data")
    os.makedirs(user_data_path, exist_ok=True)

    filepath = os.path.join(user_data_path, "users_received.json")
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify("Daten sind erfolgreich angekommen")


if __name__ == '__main__':
    cert_folder = os.path.join(os.path.dirname(__file__), "Certs")
    context = (
        os.path.join(cert_folder, "certificates.pem"),
        os.path.join(cert_folder, "key.pem"),
    )
    app.run(host='0.0.0.0', port=5000, ssl_context=context)