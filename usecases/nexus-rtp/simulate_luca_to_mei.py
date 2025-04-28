# simulate_luca_to_mei.py

import sys
import os
from datetime import datetime

# Dynamically locate root dir
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\Users\jzack\ML Projects\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "fx-optimizer"))
sys.path.append(os.path.join(ROOT_DIR, "routing-engine"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))

# Imports
from fx_model import predict_fx_timing
from router import choose_payment_route
from nexus_bridge import simulate_nexus_rtp_transfer
from mock_delivery import simulate_fund_delivery
from mock_cbdc_delivery import anchor_log


def run_luca_flow():
    print("Welcome to PAIN: Luca → Mei via Nexus (EUR to SGD)\n")

    amount = 100
    currency_pair = "EUR/SGD"
    urgency = "medium"

    print(f"Intent: Send €{amount} from France to Singapore via Nexus RTP")

    # FX Timing
    advice = predict_fx_timing(currency_pair, amount, urgency)
    print(f" FX Advice: {advice}")

    # Route
    route = choose_payment_route(amount, "SG", advice)
    print(f" Route Selected: {route}")

    receipt = {
        "sender_country": "France",
        "receiver_country": "Singapore",
        "currency_pair": currency_pair,
        "amount": amount,
        "urgency": urgency,
        "fx_advice": advice,
        "route_selected": route,
        "fallback_used": False,
        "rail_type": "Nexus RTP" if "Nexus" in route else "Fallback",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # Simulate Nexus route or fallback
    if "Nexus" in route:
        simulate_nexus_rtp_transfer(
            sender_country="France",
            receiver_country="Singapore",
            amount=amount,
            route=route,
            recipient="Mei"
        )
    else:
        receipt["fallback_used"] = True
        route = "USDC → SGD Stablecoin Wallet"
        receipt["route_selected"] = route
        receipt["rail_type"] = "Stablecoin"
        simulate_fund_delivery(route, amount)

    receipt["status"] = "Delivered"
    anchor_log(receipt)


if __name__ == "__main__":
    run_luca_flow()
