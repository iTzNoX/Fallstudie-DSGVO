import os
import json
import requests
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return "running"

@app.route('/send_data', methods=["POST"])
def send_data():
    user_data_path = os.path.join(os.path.dirname(__file__), "User_Data", "users.json")

    with open(user_data_path, "r") as f:
        data = json.load(f)

    server2_url = "https://server2:5000/receive_data"

    try:
        response = requests.post(server2_url,
                                 json=data,
                                 verify=os.path.join(os.path.dirname(__file__), "../Certs", "certificates.pem"))
        if response.status_code == 200:
            return jsonify("Daten wurden gesendet")
        else:
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