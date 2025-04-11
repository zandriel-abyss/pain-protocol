# PAIN Protocol – Project Overview

**PAIN (Programmable AI-powered Interoperable Network)** is a rail-agnostic protocol that enables smart, compliant, cross-border money flows. It orchestrates payments across CBDCs, stablecoins, and traditional rails using AI-driven FX timing, programmable compliance logic, and verifiable identity layers.

---

## Mission
> To make cross-border payments affordable, programmable, and legally interoperable—regardless of geography, currency, or rails.

---

## 🔧 What PAIN Does

| Layer | Purpose |
|-------|---------|
| FX Engine | Predicts optimal timing to send funds (e.g. "Wait 2 hours") |
| Routing Engine | Picks the best delivery rail (CBDC, stablecoin, cashout, bank) |
| Compliance Layer | Checks DID/KYC credential validity and country rules |
| Execution Layer | Simulates or performs transfers with audit logs |
| Anchoring | Logs each transaction into verifiable JSON receipts |

---

## Supported Use Cases (Phase 1)

| Persona | Summary |
|---------|---------|
| Maria | Migrant worker sends remittance from UAE to PH via CBDC or agent |
| Aisha | Freelancer splits payout between savings (USDC) and local currency |

---

## Modules

```bash
fx-optimizer/        # Predict FX timing (LSTM or rules)
routing-engine/      # Determine rail path (e.g., CBDC vs USDC)
payment-rails/       # Simulate transfers and delivery
compliance-engine/   # (coming soon) DID + jurisdiction logic
wallet-sdk/          # CLI interfaces for user flows
usecases/            # Run scripts for Maria, Aisha
```

---

## Supported Rails

| Rail Type | Examples |
|-----------|----------|
| Stablecoins | USDC, DAI on Polygon/Solana |
| CBDC | eAED, ePHP (via mBridge) |
| Cash Agents | GCash, M-Pesa, Western Union |
| Banks | UPI, SEPA, ACH (planned) |

---

## Who Is It For?
- Migrant workers and freelancers
- NGOs sending programmable aid
- Mid-market CFOs managing FX risk
- Developers building rails, wallets, or compliance tools

---

## What’s Next (Phase 2+)
- NGO disbursement flow (Tunde)
- Compliance rule engine + DID validator
- Treasury simulator (Arjun use case)
- Bridge to external sandbox CBDCs (mBridge, Dunbar)

---

*PAIN is not a blockchain—it’s the programmable layer that lets you move money through any rail, smarter and safer.*
