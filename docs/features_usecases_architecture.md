# 🧩 PAIN Protocol – Features, Use Cases & System Architecture

## 🔧 Feature Overview

| Feature Name | Type | Phase | Used In | Status | Description |
| --- | --- | --- | --- | --- | --- |
| AI FX Optimizer | Core | Phase 1 | Maria, Aisha, Arjun | ✅ Complete (rule-based) | Predicts best time and rate to send funds |
| Smart Routing Engine | Core | Phase 1 | All | ✅ Complete | Determines optimal route across rails (CBDC, stablecoin, RTP, agent) |
| DID Resolver | Compliance | Phase 2 | Tunde, NGO | 🟡 In Progress | Verifies user identity through decentralized credentials |
| Wallet Interface (CLI) | Wallet | Phase 1 | Maria, Aisha | ✅ Complete | Command-line interface to enter intent, split logic, initiate flows |
| Mock Payment Rails | Integration | Phase 1 | Maria, Aisha | ✅ Complete | Simulated CBDC, stablecoin, and cash agent delivery rails |
| Rail Registry + Outage Simulator | Core Infra | Phase 2 | All | ✅ Complete | Simulates real-time availability of payment rails |
| Nexus Bridge Logic | Integration | Phase 2 | Luca | ✅ Complete | Routes through BIS Nexus corridor (e.g., EUR → SGD RTP) |
| ERP Integration (stub) | Integration | Phase 2 | Arjun | 🟡 In Progress | Hooks for treasury/ERP data (invoices, timing) |
| Voucher Distribution Logic | Wallet + Rules | Phase 2 | Tunde | ✅ Complete | Generate, validate, and redeem programmable aid vouchers |
| Working Capital Simulator | Core | Phase 2 | Arjun | Planned | Visualize FX outcomes on treasury flow timing |
| Multi-Payout Engine | NGO Tool | Phase 2 | Anna, Tunde | ✅ Complete | Batch-simulates NGO disbursement to multiple recipients |
| zkCompliance Module | Compliance | Phase 3 | Institutional, NGO | Planned | Enables zero-knowledge AML/KYC checks and validation |
| Plugin Framework | Infra | Phase 3 | Developers | Planned | Enables custom FX logic, DID providers, and bridge hooks |

---

## ✅ Use Case Snapshots

### 1. **Maria – Cross-Border P2P CBDC (with Fallback)**
- **Goal**: eAED → ePHP (fallback to stablecoin if needed)
- **Features Used**: FX Optimizer, Routing Engine, CBDC + stablecoin delivery, Anchoring

### 2. **Aisha – Freelancer Payout Split (Save + Convert)**
- **Goal**: Split into USDC savings + NGN local cash
- **Features Used**: CLI, FX Optimizer, Dual-rail logic, Anchoring

### 3. **Luca → Mei – RTP via BIS Nexus (EUR → SGD)**
- **Goal**: Cross-border bank-to-wallet using Nexus-compatible corridor
- **Features Used**: Nexus Bridge, FX Timing, Fallback Resilience, Anchoring

### 4. **Tunde – Purpose-Bound CBDC Aid**
- **Goal**: CBDC voucher with usage constraints (food, school, expiry)
- **Features Used**: Voucher Logic, DID (planned), Anchoring, Compliance Layer

### 5. **Arjun – Treasury FX Simulation**
- **Goal**: Optimize timing of B2B payments across FX corridors
- **Features Used**: FX Optimizer, ERP Integration (stub), Scenario Analysis

### 6. **NGO Multi-Payout (Anna, Tunde)**
- **Goal**: Disburse funds to verified recipients via mixed rails
- **Features Used**: Multi-Payout Engine, Routing, Anchored Receipts

---

## 🧾 Summary Table

| Use Case | Goal | Rail Used | Key Feature |
| --- | --- | --- | --- |
| Maria | Remittance (CBDC → PH) | CBDC, fallback | Smart fallback, anchored receipt |
| Aisha | Freelancer payout | Stablecoin + fiat | Dual-leg payout, FX logic |
| Luca–Mei | RTP via Nexus | Bank corridor | Nexus bridge logic |
| Tunde | Aid with conditions | CBDC + voucher | Voucher logic, DID anchor |
| Arjun | Treasury timing sim | ERP + FX | Scenario FX advice |
| NGO Batch | Multi-recipient payout | All rails | Routing + batch engine |

---

✅ Built for programmable decisions across **CBDC, stablecoin, RTP, and agent** rails  
✅ Anchors every transaction with **audit-ready receipts**  
✅ Adapts in real-time with FX signals, urgency, and corridor availability  
✅ Modular, open architecture for future compliance, fraud, and dashboard extensions

---

## 🧱 System Architecture Overview

### 📦 Core Layers

- **Presentation Layer**: `cli_wallet.py` (CLI), future web/DID portals
- **Logic Layer**: `fx_model.py`, `router.py`, `voucher_logic.py`, `multi_payout_simulator.py`
- **Integration Layer**: `mock_cbdc_delivery.py`, `stablecoin_mock.py`, `nexus_bridge.py`
- **Data Layer**: JSON logs, voucher metadata, compliance flags, anchored receipts

---

### 🔄 Typical Flow: Maria's CBDC Remittance (Fallback-Aware)

```
[User Input via CLI Wallet]
       ↓
[predict_fx_timing()] ← urgency, FX trend
       ↓
[choose_payment_route()] ← rail availability, country support
       ↓
→ if CBDC: simulate_cbdc_delivery()
→ else: simulate_stablecoin_transfer()
       ↓
[anchor_log()] → logs/anchored_receipts.json
```

---

### 🧠 Intelligence Modules

- `fx_model.py` – Rule-based logic for now, ML-ready (e.g., volatility, delta trends)
- `rail_registry.py` – Live simulation of online/offline payment rails
- `voucher_logic.py` – Programmatic voucher creation, validation, redemption

---

### 🛠 Tech Stack

| Layer | Stack |
|-------|-------|
| Lang & CLI | Python 3.x + CLI prompt scripts |
| Data | JSON (mock inputs, anchored logs) |
| ML-Ready | NumPy, scikit-learn, pandas (FX models coming) |
| API Hooks | REST-style stubs for future SEPA, Circle, mBridge |
| Dashboard | Jupyter Notebook / Streamlit (planned) |

---
