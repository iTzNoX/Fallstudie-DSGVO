import os
import socket
import ssl
import pytest

@pytest.mark.parametrize("host,port", [("localhost", 5001), ("localhost", 5002)])
def test_tls_connection(host, port):
    context = ssl.create_default_context(cafile=os.path.join(os.path.dirname(__file__), "../../Certs", "certificates.pem"))
    with socket.create_connection((host, port), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            protocol_version = ssock.version()
            assert protocol_version is not None, "Keine TLS-Verbindung aufgebaut"
            print(f"TLS Version: {protocol_version}")
