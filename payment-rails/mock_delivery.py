# payment-rails/mock_delivery.py

import random

def simulate_fund_delivery(route: str, amount: float, recipient: str = "Maria's Mom") -> str:
    """
    Simulates sending money through the chosen route.
    Randomly succeeds or fails to mimic real-world uncertainty.
    """

    print(f"\nDelivering ${amount} via: {route}")
    
    success = random.choices(["success", "delay", "failed"], weights=[0.7, 0.2, 0.1])[0]

    if success == "success":
        return f"Delivered successfully to {recipient} via {route}"
    elif success == "delay":
        return f"Delivery delayed. Funds are pending clearance."
    else:
        return f"Delivery failed. Please retry or choose another route."
