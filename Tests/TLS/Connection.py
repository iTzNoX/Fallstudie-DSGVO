import json
import os
import socket
import ssl
import pytest
import requests


@pytest.mark.parametrize("host,port", [("localhost", 5001), ("localhost", 5002)])
def test_tls_connection(host, port):
    context = ssl.create_default_context(cafile=os.path.join(os.path.dirname(__file__), "../../Certs", "certificates.pem"))
    with socket.create_connection((host, port), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            protocol_version = ssock.version()
            assert protocol_version is not None, "Keine TLS-Verbindung aufgebaut"
            print(f"TLS Version: {protocol_version}")

@pytest.mark.parametrize("api_key, expected_status", [(
        json.load(open(os.path.join(os.path.dirname(__file__), "..", "..", "Certs", "header_key.json")))["api_key"],
        200),
        ("0000000000000000000000000000000000000000000000000000000000000000",
        401)])
def test_api_key_auth(api_key, expected_status):
    cert_path = os.path.join(os.path.dirname(__file__), "..", "..", "Certs", "certificates.pem")
    server2_url = "https://localhost:5002/receive_data"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    test_data = {"test": "api key auth"}

    response = requests.post(server2_url, json=test_data, headers=headers, verify=cert_path)
    assert response.status_code == expected_status