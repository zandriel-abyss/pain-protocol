# usecases/treasury-arjun/run_arjun_flow.py

import sys
import os
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\\Users\\jzack\\ML Projects\\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "fx-optimizer"))
sys.path.append(os.path.join(ROOT_DIR, "compliance-engine"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))

from fx_model import predict_fx_timing
from did_checker import validate_did_compliance
from mock_cbdc_delivery import anchor_log


def run_arjun_flow():
    print("Welcome to PAIN: Arjun – Treasury FX Timing Simulation\n")

    arjun_did = "arjun"
    currency_pair = "EUR/INR"
    invoice_amount = 10000  # euros
    urgency = "medium"

    # Compliance check for enterprise-level user
    print(f"Validating DID for Arjun ({arjun_did})...\n")
    is_valid, msg = validate_did_compliance(arjun_did, ["kyc_passed", "enterprise_access"])

    if not is_valid:
        print(f"❌ Compliance failed: {msg}")
        return

    print("✅ Compliance passed. Running FX analysis...\n")
    advice = predict_fx_timing(currency_pair, invoice_amount, urgency)

    print("Invoice Summary:")
    print(f"- Currency Pair: {currency_pair}")
    print(f"- Amount: €{invoice_amount}")
    print(f"- Urgency: {urgency}")
    print(f"- FX Suggestion: {advice}")

    # Anchor FX advice as an enterprise log
    receipt = {
        "user_did": arjun_did,
        "currency_pair": currency_pair,
        "amount": invoice_amount,
        "urgency": urgency,
        "fx_advice": advice,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "usecase": "treasury_fx_decision"
    }

    anchor_log(receipt)
    print("\n📦 FX suggestion logged for audit and ERP sync.")


if __name__ == "__main__":
    run_arjun_flow()
