# wallet-sdk/cli_wallet.py

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\Users\jzack\ML Projects\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))
sys.path.append(os.path.join(ROOT_DIR, "compliance-engine"))

from did_checker import validate_did_compliance


def wallet_interface():
    print("Welcome to PAIN CLI Wallet")

    did = input("🔐 Enter your DID (e.g., 'tunde'): ").strip()
    required_tags = ["kyc_passed"]  # Base level compliance

    print(f"\nValidating DID {did}...")
    is_valid, msg = validate_did_compliance(did, required_tags)

    if not is_valid:
        print(f"❌ Access denied: {msg}")
        return

    print("✅ Identity validated. You may now access payment tools.\n")

    # Example options
    print("Available actions:")
    print("1. Send Money (remittance)")
    print("2. Redeem Voucher")
    print("(More features coming soon...)\n")

    action = input("Select an action (1 or 2): ").strip()

    if action == "1":
        print("🔁 Redirecting to remittance flow (to be implemented)...")
    elif action == "2":
        print(f"🎫 Checking voucher eligibility for {did}... (launch run_tunde_flow or similar flow)\n")
    else:
        print("❓ Invalid selection")


if __name__ == "__main__":
    wallet_interface()
