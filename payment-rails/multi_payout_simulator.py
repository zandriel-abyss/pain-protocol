# payment-rails/multi_payout_simulator.py

import sys
import os
import json
from datetime import datetime

# Add root and routing-engine path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\\Users\\jzack\\ML Projects\\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "routing-engine"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))

from router import choose_payment_route
from mock_cbdc_delivery import simulate_cbdc_delivery
from mock_delivery import simulate_fund_delivery
from stablecoin_mock import simulate_stablecoin_transfer  # optional fallback
from rail_registry import check_rail_status


def load_batch(filename="sample_batch.json"):
    with open(filename, "r") as f:
        return json.load(f)


def process_batch_payouts(batch):
    for entry in batch:
        name = entry["name"]
        country = entry["receiver_country"]
        amount = entry["amount"]
        urgency = entry.get("urgency", "medium")
        currency_pair = entry.get("currency_pair", "USD/LOCAL")

        print(f"\n Processing payout for {name} → {country} | ${amount}")

        route = choose_payment_route(amount, country, "Send now")
        print(f"  Route: {route}")

        if "CBDC" in route:
            if check_rail_status("CBDC_UAE"):
                simulate_cbdc_delivery("HQ", country, amount, route, recipient=name)
            else:
                print(" CBDC unavailable. Skipping.")
        elif "USDC" in route:
            simulate_stablecoin_transfer("HQ", country, amount, route, recipient=name)
        else:
            simulate_fund_delivery(route, amount)


# CLI Test
if __name__ == "__main__":
    batch = load_batch()
    process_batch_payouts(batch)
