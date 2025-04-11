# payment-rails/mock_cbdc_delivery.py

import os
import json
from datetime import datetime, UTC

def simulate_cbdc_delivery(sender_country, receiver_country, amount, route, recipient="Receiver"):
    print(f"CBDC Transfer Initiated: {sender_country} → {receiver_country}")
    print(f"Route: {route}")
    print(f"Compliance Passed ")
    print(f"{amount} successfully transferred to {recipient} via CBDC rail\n")

    # Prepare receipt log
    receipt = {
        "from_country": sender_country,
        "to_country": receiver_country,
        "amount": amount,
        "route": route,
        "recipient": recipient,
        "rail": "CBDC",
        "timestamp": datetime.now(UTC).isoformat() + "Z",
        "status": "delivered"
    }

    anchor_log(receipt)
    return receipt

def anchor_log(data, filename="anchored_receipts.json"):
    path = "logs"
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, filename)

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(data)

    with open(file_path, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"Anchored receipt saved to {file_path}")

