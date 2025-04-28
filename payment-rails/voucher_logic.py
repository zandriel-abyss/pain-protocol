# payment-rails/voucher_logic.py

from datetime import datetime, timedelta
import json
import os

# Voucher Rule Engine

def validate_voucher(voucher, category, current_time=None):
    current_time = current_time or datetime.utcnow()

    # Check expiry
    if "expires_at" in voucher:
        expires = datetime.fromisoformat(voucher["expires_at"].replace("Z", ""))
        if current_time > expires:
            return False, "Voucher expired"

    # Check category
    if "allowed_categories" in voucher:
        if category not in voucher["allowed_categories"]:
            return False, "Category not allowed"

    return True, "Voucher valid"

def generate_voucher(amount, usage_category="education", duration_days=7, recipient="Tunde Beneficiary"):
    voucher = {
        "recipient": recipient,
        "amount": amount,
        "allowed_categories": [usage_category],
        "issued_at": datetime.utcnow().isoformat() + "Z",
        "expires_at": (datetime.utcnow() + timedelta(days=duration_days)).isoformat() + "Z",
        "status": "active",
        "rail": "CBDC",
        "metadata": {
            "purpose": usage_category,
            "notes": "Programmatic CBDC voucher"
        }
    }
    anchor_voucher(voucher)
    return voucher

def anchor_voucher(data, filename="anchored_vouchers.json"):
    path = r"C:\Users\jzack\ML Projects\pain-protocol\logs"
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

    print(f"Anchored voucher saved to {file_path}")

def redeem_voucher(recipient, category):
    file_path = os.path.join(r"C:\Users\jzack\ML Projects\pain-protocol\logs", "anchored_vouchers.json")

    if not os.path.exists(file_path):
        print("No vouchers available for redemption.")
        return

    with open(file_path, "r") as f:
        vouchers = json.load(f)

    for voucher in vouchers:
        if voucher["recipient"] == recipient and voucher["status"] == "active":
            is_valid, message = validate_voucher(voucher, category)

            if is_valid:
                voucher["status"] = "redeemed"
                voucher["redeemed_at"] = datetime.utcnow().isoformat() + "Z"
                print(f" Voucher redeemed successfully for {category}.")
                break
            else:
                print(f" Voucher validation failed: {message}")
                break
    else:
        print(f" No active voucher found for {recipient} in category: {category}")

    with open(file_path, "w") as f:
        json.dump(vouchers, f, indent=2)