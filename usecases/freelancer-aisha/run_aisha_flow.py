# usecases/freelancer-aisha/run_aisha_flow.py

import sys
import os

# Add module paths
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\Users\jzack\ML Projects\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "fx-optimizer"))
sys.path.append(os.path.join(ROOT_DIR, "routing-engine"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))

# Import core modules
from fx_model import predict_fx_timing
from router import choose_payment_route
from aisha_delivery import simulate_split_payout

def run_aisha_flow():
    print("Welcome to PAIN: Aisha’s Freelancer Payout\n")

    total_amount = 800
    currency_pair = "USD/NGN"
    urgency = "medium"

    print(f"Incoming Payment: ${total_amount} from global client")
    print(f"Currency Pair: {currency_pair} | Urgency: {urgency}")

    # FX Suggestion
    advice = predict_fx_timing(currency_pair, total_amount, urgency)
    print(f"FX Advice: {advice}")

    # User chooses savings %
    try:
        save_pct = float(input("What % would you like to save in USDC (e.g. 30): "))
        save_amount = round((save_pct / 100) * total_amount, 2)
        convert_amount = round(total_amount - save_amount, 2)
    except:
        print("Invalid input. Defaulting to 50/50 split.")
        save_amount = 400
        convert_amount = 400

    print(f"\n You’ll convert ${convert_amount} to Naira and save ${save_amount} in USDC")

    # Routes
    convert_route = choose_payment_route(convert_amount, "NG", advice)
    save_route = "USDC → PAIN Wallet (multi-currency)"

    # Simulate and anchor both
    simulate_split_payout(convert_amount, save_amount, convert_route, save_route)

if __name__ == "__main__":
    run_aisha_flow()
