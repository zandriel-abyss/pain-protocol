# fx-optimizer/data_sources.py

import os
import requests

# Fallback mock data
MOCK_FX_DATA = {
    "USD/PHP": {"current": 56.20, "1hr_ago": 56.10, "volatility": 0.3},
    "USD/NGN": {"current": 1450, "1hr_ago": 1442, "volatility": 2.1},
    "EUR/USD": {"current": 1.086, "1hr_ago": 1.082, "volatility": 0.2}
}

# Switchable data source

def get_fx_data(currency_pair: str, source="mock"):
    if source == "mock":
        return MOCK_FX_DATA.get(currency_pair, {
            "current": 1.0,
            "1hr_ago": 1.0,
            "volatility": 0.0
        })
    elif source == "openexchangerates":
        return fetch_from_openexchangerates(currency_pair)
    else:
        raise ValueError("Unsupported FX data source")

# Live API stub (requires signup + API key)
def fetch_from_openexchangerates(currency_pair):
    base_url = "https://openexchangerates.org/api/latest.json"
    app_id = os.getenv("OPENEXCHANGE_APP_ID")  # store your API key as an env variable

    if not app_id:
        raise EnvironmentError("OPENEXCHANGE_APP_ID not set in environment variables")

    response = requests.get(f"{base_url}?app_id={app_id}")
    if response.status_code != 200:
        raise ConnectionError("Failed to fetch FX rates from OpenExchangeRates")

    data = response.json().get("rates", {})

    base, quote = currency_pair.split("/")
    if base != "USD":
        raise NotImplementedError("Only USD base pairs are supported in OpenExchangeRates")

    current_rate = data.get(quote)
    if not current_rate:
        raise ValueError(f"Rate for {currency_pair} not found")

    # Fake 1hr_ago estimation and basic volatility for now
    return {
        "current": current_rate,
        "1hr_ago": round(current_rate * 0.995, 4),
        "volatility": 0.4  # placeholder
    }
