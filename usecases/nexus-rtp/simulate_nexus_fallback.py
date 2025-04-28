# usecases/nexus-rtp/simulate_nexus_fallback.py

import sys
import os
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\Users\jzack\ML Projects\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "fx-optimizer"))
sys.path.append(os.path.join(ROOT_DIR, "routing-engine"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))

from fx_model import predict_fx_timing
from router import choose_payment_route
from nexus_bridge import simulate_nexus_rtp_transfer
from stablecoin_transfer import simulate_stablecoin_transfer
from mock_cbdc_delivery import anchor_log


def run_nexus_fallback_flow():
    print("Welcome to PAIN: Nexus Corridor with Fallback Simulation\n")

    amount = 150
    currency_pair = "EUR/SGD"
    urgency = "low"

    print(f"Intent: Send €{amount} from Germany to Singapore with fallback option")

    # FX advice
    advice = predict_fx_timing(currency_pair, amount, urgency)
    print(f" FX Advice: {advice}")

    # Simulated availability flag
    NEXUS_AVAILABLE = False

    # Primary route logic
    if NEXUS_AVAILABLE:
        route = "Nexus RTP (EUR → SGD via PayNow)"
        fallback_used = False
        simulate_nexus_rtp_transfer("Germany", "Singapore", amount, route, recipient="Mei")
    else:
        route = "Fallback: USDC → SGD wallet"
        fallback_used = True
        simulate_stablecoin_transfer("Germany", "Singapore", amount, route, recipient="Mei")

    # Anchor receipt
    receipt = {
        "sender_country": "Germany",
        "receiver_country": "Singapore",
        "currency_pair": currency_pair,
        "amount": amount,
        "urgency": urgency,
        "fx_advice": advice,
        "primary_route": "Nexus",
        "fallback_used": fallback_used,
        "route_selected": route,
        "status": "Delivered",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    anchor_log(receipt)


if __name__ == "__main__":
    run_nexus_fallback_flow()