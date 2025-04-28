# compliance-engine/did_checker.py

import json
import os
from datetime import datetime

MOCK_DID_FOLDER = os.path.join(r"C:\Users\jzack\ML Projects\pain-protocol\mock_dids")


def load_did_profile(did: str):
    filepath = os.path.join(MOCK_DID_FOLDER, f"{did}.json")
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as f:
        return json.load(f)


def validate_did_compliance(did: str, required_tags=None):
    required_tags = required_tags or []
    profile = load_did_profile(did)

    if not profile:
        return False, "DID not found"

    # Basic checks
    if profile.get("status") != "verified":
        return False, "DID not verified"

    # Check required tags (e.g., 'g2p_eligible', 'kyc_passed')
    for tag in required_tags:
        if tag not in profile.get("tags", []):
            return False, f"Missing required tag: {tag}"

    return True, "DID compliance passed"


# Optional CLI test
if __name__ == "__main__":
    result, msg = validate_did_compliance("tunde", ["g2p_eligible"])
    print("✅" if result else "❌", msg)