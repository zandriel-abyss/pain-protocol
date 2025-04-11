import sys
import os

# Dynamically locate root dir (portable across machines)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\Users\jzack\ML Projects\pain-protocol"))

# Add all necessary module folders
sys.path.append(os.path.join(ROOT_DIR, "wallet-sdk"))
sys.path.append(os.path.join(ROOT_DIR, "fx-optimizer"))
sys.path.append(os.path.join(ROOT_DIR, "routing-engine"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))

# Now import modules
from fx_model import predict_fx_timing
from router import choose_payment_route
from mock_delivery import simulate_fund_delivery
from mock_cbdc_delivery import simulate_cbdc_delivery  # new import

def run_maria_flow():
    print("Welcome to PAIN: Maria’s Remittance Flow\n")

    amount = 200
    currency_pair = "USD/PHP"
    urgency = "low"

    print(f"Input: Send ${amount} from {currency_pair} (Urgency: {urgency})")

    # FX Timing
    advice = predict_fx_timing(currency_pair, amount, urgency)
    print(f" FX Advice: {advice}")

    # Routing
    route = choose_payment_route(amount, "PH", advice)
    print(f" Route Selected: {route}")

    # Delivery Logic – choose based on route content
    if "CBDC" in route or "eAED" in route:
        simulate_cbdc_delivery(
            sender_country="UAE",
            receiver_country="Philippines",
            amount=amount,
            route=route,
            recipient="Maria's Mom"
        )
    else:
        delivery = simulate_fund_delivery(route, amount)
        print(f"Delivery Status: {delivery}")

if __name__ == "__main__":
    run_maria_flow()
