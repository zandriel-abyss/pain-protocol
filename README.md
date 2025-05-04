# PAIN Protocol

**PAIN (Programmable AI-powered Interoperable Network)** is an intelligent, modular protocol designed to route global payments across CBDCs, stablecoins, bank APIs, and cash agents—while enforcing compliance, optimizing FX timing, and anchoring transaction logs.

This is a **working prototype (v0.1)** featuring:
- Maria’s CBDC-based remittance flow (UAE → PH)
- Aisha’s split freelancer payout (convert + savings)
- AI FX prediction (rule-based for now, ML-ready)
- Smart routing engine with real-time rail fallback
- DID-compatible compliance logic (basic)
- Anchored transaction receipts in JSON
- NGO batch payout simulation (multi-send)
- Rail registry + outage simulator
- Notebook-based fallback test suite

---

## Why PAIN?

> Because moving money across borders shouldn’t be expensive, complex, or legally risky.

PAIN helps:
- Individuals: send money affordably and safely
- Freelancers: save + convert with smart FX
- CFOs/SMEs: simulate optimal FX timing (coming soon)
- NGOs: deliver aid to verified recipients with programmable rails
- Governments: disburse programmable CBDC (with voucher logic)

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
│   ├── fx_model.py
│   └── data_sources.py
├── routing-engine/
│   └── router.py
├── wallet-sdk/
│   └── cli_wallet.py
├── payment-rails/
│   ├── mock_delivery.py
│   ├── mock_cbdc_delivery.py
│   ├── aisha_delivery.py
│   ├── rail_registry.py
│   ├── nexus_bridge.py
│   ├── stablecoin_mock.py
│   └── multi_payout_simulator.py
├── docs/
│   └── overview.md
├── logs/
│   └── anchored_receipts.json
├── sample_batch.json
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

### NGO Batch Payout (multi-send simulation)
```bash
python payment-rails/multi_payout_simulator.py
```

Anchored receipts are saved to:
```
logs/anchored_receipts.json
```

---

## Milestone
This is **PAIN Protocol v0.1** – a working demo of programmable money flows with:
- Routing intelligence
- CBDC + stablecoin + fallback delivery
- Anchored audit logs
- Rule-based FX optimization

### ✅ Upcoming in v0.2:
- Voucher flows (Tunde)
- Programmable disbursement logic
- API bridge simulator (e.g., Circle, mBridge)
- ML-driven FX model (Arjun use case)
- Dashboard + NGO analytics layer

---

## Contributors
- **Zack** – Co-founder, Product Architect & Lead Developer
- **Vishal** – Co-founder, Compliance Strategist

---

## 📄 License
MIT (to be defined)