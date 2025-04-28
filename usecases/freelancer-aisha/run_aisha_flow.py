# usecases/freelancer-aisha/run_aisha_flow.py

import sys
import os
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\\Users\\jzack\\ML Projects\\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "fx-optimizer"))
sys.path.append(os.path.join(ROOT_DIR, "routing-engine"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))
sys.path.append(os.path.join(ROOT_DIR, "compliance-engine"))

from fx_model import predict_fx_timing
from router import choose_payment_route
from aisha_delivery import simulate_split_payout
from did_checker import validate_did_compliance
from mock_cbdc_delivery import anchor_log


def run_aisha_flow():
    print("Welcome to PAIN: Aisha’s Freelancer Payout\n")

    user_did = input("Enter your DID (e.g., 'aisha'): ").strip()
    print(f"Validating DID: {user_did}...")
    is_valid, reason = validate_did_compliance(user_did, ["kyc_passed", "freelancer_verified"])

    if not is_valid:
        print(f"Access denied: {reason}")
        return

    print("DID validated. Proceeding to payout split...\n")

    total_amount = 800
    currency_pair = "USD/NGN"
    urgency = "medium"

    print(f"Incoming Payment: ${total_amount} from global client")
    print(f"Currency Pair: {currency_pair} | Urgency: {urgency}")

    # FX Suggestion
    advice = predict_fx_timing(currency_pair, total_amount, urgency)
    print(f"FX Advice: {advice}")

    try:
        save_pct = float(input("What % would you like to save in USDC (e.g. 30): "))
        save_amount = round((save_pct / 100) * total_amount, 2)
        convert_amount = round(total_amount - save_amount, 2)
    except:
        print("Invalid input. Defaulting to 50/50 split.")
        save_amount = 400
        convert_amount = 400

    print(f"\nYou’ll convert ${convert_amount} to Naira and save ${save_amount} in USDC")

    # Routes
    convert_route = choose_payment_route(convert_amount, "NG", advice)
    save_route = "USDC → PAIN Wallet (multi-currency)"

    # Anchor both legs
    anchor_log({
        "user_did": user_did,
        "type": "freelancer_payout",
        "convert_amount": convert_amount,
        "convert_route": convert_route,
        "save_amount": save_amount,
        "save_route": save_route,
        "fx_advice": advice,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

    simulate_split_payout(convert_amount, save_amount, convert_route, save_route)


if __name__ == "__main__":
    run_aisha_flow()