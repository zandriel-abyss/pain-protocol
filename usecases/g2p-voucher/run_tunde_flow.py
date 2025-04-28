# usecases/g2p-voucher/run_tunde_flow.py

import sys
import os
from datetime import datetime

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\\Users\\jzack\\ML Projects\\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))
sys.path.append(os.path.join(ROOT_DIR, "compliance-engine"))

from voucher_logic import generate_voucher, validate_voucher, redeem_voucher
from did_checker import validate_did_compliance


def run_tunde_flow():
    print("Welcome to PAIN: Tunde – G2P CBDC Voucher Disbursement Flow\n")

    recipient_did = "tunde"
    amount = 75
    category = "education"

    # Step 1: DID compliance check
    print(f"Checking compliance for user DID: {recipient_did}\n") 
    is_compliant, reason = validate_did_compliance(recipient_did, ["g2p_eligible", "voucher_enabled"])

    if not is_compliant:
        print(f"DID compliance failed: {reason}")
        return

    print(" DID compliance passed. Proceeding with voucher generation...\n")
    voucher = generate_voucher(amount, usage_category=category, duration_days=7, recipient=recipient_did)

    print("\nValidating usage attempt...\n")
    is_valid, message = validate_voucher(voucher, category)

    if is_valid:
        print("Voucher is valid. Proceeding to redeem...\n")
        redeem_voucher(recipient_did, category)
    else:
        print(f" Voucher validation failed: {message}")


if __name__ == "__main__":
    run_tunde_flow()
