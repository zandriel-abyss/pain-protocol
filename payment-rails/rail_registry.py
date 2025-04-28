# payment-rails/rail_registry.py

import random
from datetime import datetime

# Registry to simulate the availability status of different payment rails

# Initial mock registry (expandable)
RAIL_STATUS = {
    "CBDC_UAE": True,
    "CBDC_PHP": True,
    "Nexus_RTP_EUR_SGD": True,
    "USDC_Stablecoin": True,
    "SEPA_Bank_Rail": True,
    "Circle_CCTP": True
}

# Check if a rail is online
def check_rail_status(rail_name: str) -> bool:
    """
    Returns the live status of a given rail.
    """
    return RAIL_STATUS.get(rail_name, False)

# Randomly simulate a rail outage (testing fallback logic)
def simulate_random_rail_outage():
    """
    Randomly simulates one rail going down for testing fallback logic.
    """
    rails = list(RAIL_STATUS.keys())
    down_rail = random.choice(rails)
    RAIL_STATUS[down_rail] = False
    print(f"Simulated outage: {down_rail} is now OFFLINE ({datetime.utcnow().isoformat()}Z)")

# Bring everything back online for clean test setups
def reset_all_rails():
    """
    Resets all rails back to online status.
    """
    for rail in RAIL_STATUS:
        RAIL_STATUS[rail] = True
    print("All rails have been reset to ONLINE.")


# CLI test
if __name__ == "__main__":
    print("Initial Rail Status:")
    print(RAIL_STATUS)

    simulate_random_rail_outage()
    print("\nRail Status After Outage:")
    print(RAIL_STATUS)

    reset_all_rails()
    print("\nRail Status After Reset:")
    print(RAIL_STATUS)
