import os
import json
from datetime import datetime

def write_log_entry(server_name: str, message: str, level: str = "INFO") -> None:
    log_dir = os.path.join(os.path.dirname(__file__), "Logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"{server_name}.log.jsonl")

    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level.upper(),
        "message": message
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")