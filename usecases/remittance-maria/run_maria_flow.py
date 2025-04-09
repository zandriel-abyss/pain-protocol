# usecases/remittance-maria/run_maria_flow.py

import sys
import os

# Add paths to find our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\jzack\ML Projects\pain-protocol\wallet-sdk')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\jzack\ML Projects\pain-protocol\fx-optimizer')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\jzack\ML Projects\pain-protocol\routing-engine')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\jzack\ML Projects\pain-protocol\payment-rails')))


from fx_model import predict_fx_timing
from router import choose_payment_route
from mock_delivery import simulate_fund_delivery

def run_maria_flow():
    print("🌍 Welcome to PAIN: Maria’s Remittance Flow\n")

    amount = 200
    currency_pair = "USD/PHP"
    urgency = "low"

    print(f"👩 Input: Send ${amount} from {currency_pair} (Urgency: {urgency})")

    # FX Timing
    advice = predict_fx_timing(currency_pair, amount, urgency)
    print(f"🧠 FX Advice: {advice}")

    # Routing
    route = choose_payment_route(amount, "PH", advice)
    print(f"🛰 Route Selected: {route}")

    # Delivery
    delivery = simulate_fund_delivery(route, amount)
    print(f"📦 Delivery Status: {delivery}")

if __name__ == "__main__":
    run_maria_flow()
