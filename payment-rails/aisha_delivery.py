# payment-rails/aisha_delivery.py

import os
import json
from datetime import datetime, UTC

def simulate_split_payout(convert_amount, save_amount, convert_route, save_route, recipient="Aisha"):
    print("\nAisha's Payout Simulation Initiated")

    # Convert Leg
    print(f"\n Converted Portion: ${convert_amount} via {convert_route}")
    print("Conversion successful")

    convert_receipt = {
        "flow": "freelancer_income",
        "type": "conversion",
        "recipient": recipient,
        "amount": convert_amount,
        "route": convert_route,
        "rail": "stablecoin or fiat",
        "timestamp": datetime.now(UTC).isoformat() + "Z",
        "status": "delivered"
    }

    # Save Leg
    print(f"\n Savings Portion: ${save_amount} via {save_route}")
    print(" Savings deposit confirmed")

    save_receipt = {
        "flow": "freelancer_income",
        "type": "savings",
        "recipient": recipient,
        "amount": save_amount,
        "route": save_route,
        "rail": "stablecoin",
        "timestamp": datetime.now(UTC).isoformat() + "Z",
        "status": "delivered"
    }

    # Anchor both
    anchor_log(convert_receipt)
    anchor_log(save_receipt)

    return convert_receipt, save_receipt

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
