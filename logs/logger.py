import json
from datetime import datetime
from pathlib import Path


LOG_FILE = Path("logs/interactions.jsonl")


def log_interaction(
    session_id,
    user_input,
    response
):
    print("logger fn called")

    record = {
        "timestamp": datetime.now().isoformat(),
        "session_id": session_id,
        "user_input": user_input,
        "response": response
    }

    with open(LOG_FILE, "a") as f:
        f.write(
            json.dumps(record)
            + "\n"
        )