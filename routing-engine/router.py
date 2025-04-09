# routing-engine/router.py

import random

def choose_payment_route(amount: float, destination_country: str, fx_advice: str) -> str:
    """
    Picks a mock payment path based on FX advice, destination, and simple rules.
    """

    print(f"🚦 Choosing route for {amount} to {destination_country}...")

    # Mock logic: randomness + basic fx logic
    if "wait" in fx_advice.lower():
        route = random.choice([
            "USDC → ePHP (GlobaWallet)",
            "USDC → GCash",
            "USDT → ePHP via Agent"
        ])
    else:
        route = random.choice([
            "eAED → ePHP via CBDC rail",
            "USDC → Bank PH",
            "eAED → Cash Agent Pickup"
        ])

    return f"Best route: {route}"
