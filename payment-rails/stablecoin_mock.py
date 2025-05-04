# payment-rails/stablecoin_mock.py

from datetime import datetime

def simulate_stablecoin_transfer(sender_country, receiver_country, amount, route, recipient="Receiver"):
    print(f"\n Stablecoin Transfer Initiated: {sender_country} → {receiver_country}")
    print(f"Via: {route}")
    print(f"Recipient: {recipient}")
    print(f"Amount: ${amount} (USDC-equivalent)")
    print("Delivered via stablecoin rail")

    return {
        "from": sender_country,
        "to": receiver_country,
        "amount": amount,
        "asset": "USDC",
        "route": route,
        "status": "delivered",
        "recipient": recipient,
        "rail": "Stablecoin",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


# CLI test
if __name__ == "__main__":
    tx = simulate_stablecoin_transfer("HQ", "Nigeria", 250, "USDC → Agent")
    print("\nStablecoin Transfer Receipt:")
    print(tx)