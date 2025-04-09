# wallet-sdk/cli_wallet.py

import sys
import os

# Allow import from fx-optimizer folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\jzack\ML Projects\pain-protocol\fx-optimizer')))
from fx_model import predict_fx_timing
# add at the top
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\jzack\ML Projects\pain-protocol\routing-engine')))
from router import choose_payment_route

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\jzack\ML Projects\pain-protocol\payment-rails')))
from mock_delivery import simulate_fund_delivery


def run_wallet_interface():
    print("👋 Welcome to PAIN Wallet (CLI)")
    
    # Step 1: Get user inputs
    try:
        amount = float(input("Enter the amount to send (e.g. 200): "))
        currency_pair = input("Enter the currency pair (e.g. USD/PHP): ").strip().upper()
        urgency = input("Urgency (high / medium / low): ").strip().lower()
    except Exception as e:
        print("❌ Invalid input. Please try again.")
        return

    # Step 2: Call FX Engine
    print("\n🔄 Processing your transfer...")
    advice = predict_fx_timing(currency_pair, amount, urgency)

    # Step 3: Output FX suggestion
    print(f"\n🧠 PAIN FX Advice: {advice}")

    # Step 4: Choose routing
    route = choose_payment_route(amount, currency_pair.split("/")[-1], advice)
    print(f"🛰 Routing Decision: {route}")

    # Step 5: Simulate fund delivery
    delivery_result = simulate_fund_delivery(route, amount)
    print(f"\n📦 Delivery Status: {delivery_result}")


# Run the CLI
if __name__ == "__main__":
    run_wallet_interface()
