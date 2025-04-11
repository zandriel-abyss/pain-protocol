# Maria's Flow – Remittance via CBDC

Maria is a migrant worker in the UAE. She wants to send 200 AED to her mother in the Philippines. Her bank issues eAED (UAE’s CBDC), and her mother receives ePHP (PH CBDC) via a digital wallet or cash agent.

---

## Flow Steps

1. **Maria enters details** in the wallet CLI:
   - Amount: 200
   - Currency pair: USD/PHP
   - Urgency: Low

2. **FX Engine** predicts:
   > "Wait 2 hours – expected gain in exchange rate"

3. **Router Engine** selects route:
   > "eAED → ePHP via mBridge (CBDC rail)"

4. **Compliance Layer** (placeholder): Validates jurisdictional KYC/DID

5. **CBDC Transfer Simulation**:
   - Transfer simulated from UAE to PH
   - Receipt anchored to logs

6. **Anchored Result** saved to `logs/anchored_receipts.json`

---

## Tech Stack Involved

| Step | File/Module |
|------|-------------|
| Input | `cli_wallet.py` |
| FX Logic | `fx_model.py` |
| Routing | `router.py` |
| Delivery | `mock_cbdc_delivery.py` |
| Anchoring | `log_anchor()` in same module |

---

## What It Demonstrates
- FX intelligence
- CBDC route simulation
- Modular flow logic
- Anchored receipts

This is PAIN's first full programmable, cross-border transfer simulation using public- or bank-issued CBDC logic.