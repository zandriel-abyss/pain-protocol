# PAIN Protocol

**PAIN (Programmable AI-powered Interoperable Network)** is an intelligent, modular protocol designed to route global payments across CBDCs, stablecoins, bank APIs, and cash agents—while enforcing compliance, optimizing FX timing, and anchoring transaction logs.

This is a **working prototype (v0.1)** featuring:
- Maria’s CBDC-based remittance flow (UAE → PH)
- Aisha’s split freelancer payout (convert + savings)
- AI FX prediction
- Smart routing engine
- DID-compatible compliance logic (basic)
- Anchored transaction receipts in JSON

---

## Why PAIN?

> Because moving money across borders shouldn’t be expensive, complex, or legally risky.

PAIN helps:
- Individuals: send money affordably and safely
- Freelancers: save + convert with smart FX
- CFOs/SMEs: simulate optimal FX timing (coming soon)
- NGOs: deliver aid to verified recipients (upcoming)

---

## Repo Structure

```bash
pain-protocol/
├── usecases/
│   ├── remittance-maria/
│   │   └── run_maria_flow.py
│   ├── freelancer-aisha/
│   │   └── run_aisha_flow.py
├── fx-optimizer/
│   └── fx_model.py
├── routing-engine/
│   └── router.py
├── wallet-sdk/
│   └── cli_wallet.py
├── payment-rails/
│   ├── mock_delivery.py
│   ├── mock_cbdc_delivery.py
│   └── aisha_delivery.py
├── docs/
│   └── overview.md
├── logs/
│   └── anchored_receipts.json
```

---

## Running a Flow

### Maria’s Flow (CBDC remittance)
```bash
python usecases/remittance-maria/run_maria_flow.py
```

### Aisha’s Flow (freelancer split payment)
```bash
python usecases/freelancer-aisha/run_aisha_flow.py
```

Anchored receipts are saved to:
```
logs/anchored_receipts.json
```

---

## Milestone
This is **PAIN Protocol v0.1** – a working demo of programmable money flows with routing, compliance logic, and anchored receipts.

Upcoming in v0.2:
- NGO voucher flows (Tunde)
- Compliance rule engine
- FX scenario simulator for Arjun (CFO)
- ML-powered FX prediction

---

## Contributors
- **Zack** – Co-founder, Product Architect & Lead Developer
- **Vishal** – Co-founder, Compliance Strategist

---

## 📄 License
MIT (to be defined)