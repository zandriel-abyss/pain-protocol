# fx-optimizer/fx_model.py

from data_sources import get_fx_data

def determine_trend(fx_data):
    delta = fx_data["current"] - fx_data["1hr_ago"]
    if delta > 0.05:
        return "up"
    elif delta < -0.05:
        return "down"
    else:
        return "flat"

def predict_fx_timing(currency_pair: str, amount: float, urgency: str, source="mock") -> str:
    print(f"Checking FX for {currency_pair}, amount ${amount}, urgency: {urgency} (source: {source})")

    fx_data = get_fx_data(currency_pair, source)
    trend = determine_trend(fx_data)
    volatility = fx_data["volatility"]

    print(f"Current Rate: {fx_data['current']} | 1hr Ago: {fx_data['1hr_ago']} | Δ: {trend} | Volatility: {volatility}")

    # Decision logic
    if urgency == "high":
        return "Send now (high urgency)"
    elif trend == "up" and volatility < 1.0:
        return "Wait 2 hours – expected gain in exchange rate"
    elif trend == "down" or volatility > 2.0:
        return "Send now – market is volatile"
    else:
        return "Send now – minimal expected change"

# Test run
if __name__ == "__main__":
    result = predict_fx_timing("USD/PHP", 200, "low", source="mock")
    print(f"Suggestion: {result}")
