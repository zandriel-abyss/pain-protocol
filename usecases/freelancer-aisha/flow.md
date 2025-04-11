# Aisha's Flow – Split Payout (Convert + Save)

Aisha is a global freelancer who receives $800 from a client. She wants to:
- Convert part to her local currency (NGN) for spending
- Save the rest in USDC for stable value

---

## Flow Steps

1. **Aisha runs the payout CLI**:
   - Input: $800
   - Urgency: Medium
   - Currency: USD/NGN
   - Chooses to save 40% in USDC

2. **FX Engine** predicts:
   > "Wait 2 hours – expected gain in exchange rate"

3. **Route A: Convert Portion** (e.g. $480):
   - Routed to NGN wallet via stablecoin rail
   - Delivery simulated

4. **Route B: Save Portion** (e.g. $320):
   - Saved in PAIN Wallet as USDC
   - Delivery confirmed

5. **Anchoring**:
   - Each leg recorded as a separate receipt
   - Stored in `logs/anchored_receipts.json`

---

## Tech Stack Involved

| Step | File/Module |
|------|-------------|
| Input | `run_aisha_flow.py` |
| FX Logic | `fx_model.py` |
| Routing | `router.py` |
| Delivery & Anchoring | `aisha_delivery.py` |

---

## What It Demonstrates
- Multi-leg payment flow
- Smart FX timing + route choice
- Verifiable delivery logs

This shows PAIN’s ability to route money **intelligently and contextually**—balancing liquidity, volatility, and user intent.
