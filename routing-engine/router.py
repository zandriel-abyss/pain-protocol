# routing-engine/router.py

import sys
import os

# Dynamically locate project root to find payment-rails modules
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\\Users\\jzack\\ML Projects\\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))

from rail_registry import check_rail_status

# Basic route selector with fallback awareness

def choose_payment_route(amount: float, destination_country: str, fx_advice: str) -> str:
    """
    Decides the best route based on destination, FX advice, and rail availability.
    """

    # Default decision tree
    if destination_country == "PH":
        if check_rail_status("CBDC_UAE") and check_rail_status("CBDC_PHP"):
            return "CBDC Rail: eAED → ePHP"
        elif check_rail_status("USDC_Stablecoin"):
            return "Fallback: USDC → GCash Agent"
        else:
            return "Fallback: Cash Agent Pickup"

    elif destination_country == "NG":
        if check_rail_status("USDC_Stablecoin"):
            return "Stablecoin Rail: USDC → Naira Agent"
        else:
            return "Fallback: Cash Agent Pickup"

    elif destination_country == "SG":
        if check_rail_status("Nexus_RTP_EUR_SGD"):
            return "Nexus RTP Rail: EUR → SGD via PayNow"
        elif check_rail_status("USDC_Stablecoin"):
            return "Fallback: USDC → SGD Stablecoin Wallet"
        else:
            return "Fallback: Manual Cash Delivery"

    else:
        if check_rail_status("USDC_Stablecoin"):
            return "Generic Stablecoin Fallback"
        else:
            return "Manual Cash Delivery"


# CLI Test
if __name__ == "__main__":
    route = choose_payment_route(200, "PH", "Send now")
    print(f"Route Chosen: {route}")
