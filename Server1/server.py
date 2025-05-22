import os
import json
import requests
from flask import Flask, jsonify
from intern_controller import write_log_entry
app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return "running"

@app.route('/send_data', methods=["POST"])
def send_data():
    write_log_entry("Server1", "Sendevorgang gestartet")
    user_data_path = os.path.join(os.path.dirname(__file__), "User_Data", "users.json")

    with open(user_data_path, "r") as f:
        data = json.load(f)
    write_log_entry("Server1", "Daten wurden ausgelesen")

    server2_url = "https://server2:5000/receive_data"

    try:
        response = requests.post(server2_url,
                                 json=data,
                                 verify=os.path.join(os.path.dirname(__file__), "Certs", "certificates.pem"))
        if response.status_code == 200:
            write_log_entry("Server1", "Daten wurden gesendet", level="SUCCESS")
            return jsonify("Daten wurden gesendet")
        else:
            write_log_entry("Server1", "Sendeprozess wurde unterbrochen", level="ERROR")
            return jsonify(f"Daten wurden nicht gesendet: \n"
                           f"{response.text}")
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    cert_folder = os.path.join(os.path.dirname(__file__), "Certs")
    context = (
        os.path.join(cert_folder, "certificates.pem"),
        os.path.join(cert_folder, "key.pem"),
    )
    app.run(host='0.0.0.0', port=5000, ssl_context=context)