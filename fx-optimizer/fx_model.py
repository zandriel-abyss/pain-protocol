# Goal:Build a function that:Takes currency_pair, amount, and urgency; Returns a suggestion: "Send now" OR "Wait 2 hours" (based on a basic rule or random logic)
# fx-optimizer/fx_model.py
import random

def predict_fx_timing(currency_pair: str, amount: float, urgency: str) -> str:
    """
    Suggests whether to send now or wait based on urgency and mock FX prediction.
    """
    print(f"Checking FX trend for {currency_pair} and amount ${amount}...")

    # Mocked logic: urgency + random signal
    fx_signal = random.choice(["up", "down"])
    
    if urgency == "high":
        return "Send now (urgency is high)"
    elif fx_signal == "up":
        return "Wait 2 hours – expected gain in exchange rate"
    else:
        return "Send now – rate may drop later"

# For test run
if __name__ == "__main__":
    suggestion = predict_fx_timing("USD/PHP", 200, "low")
    print(f"Suggestion: {suggestion}")


# import random	We'll use this to simulate FX trends (up/down)
# def predict_fx_timing(...)	This function takes in key values Maria provides
# fx_signal = random.choice(...)	Randomly simulates if rate is improving or worsening
# Logic block	Combines user urgency and mock FX to decide
# __main__	Lets you run this script directly to test it