# **PAIN Protocol – Modular System Design Overview**

---

## 🔧 Core Design Philosophy

**PAIN (Programmable AI-powered Interoperable Network)** is designed as a **modular, programmable financial infrastructure layer** that intelligently routes cross-border payments, enforces compliance, and enables future plug-ins like fraud detection, programmable aid, and ZK compliance.

> Modularity ensures each function (FX, routing, compliance, delivery) is loosely coupled, independently testable, and extendable.

---

## System Architecture Layers

### 1. **Presentation Layer**

* **CLI Wallet** – Basic user interface to simulate user intent (e.g., send \$200 to PH, split payouts, redeem voucher)
* **Future**: Dashboard / API Gateway for treasury, NGOs, developers

---

### 2. **Logic Layer**

* **`fx_model.py`** – Predicts optimal time to send money (currently rule-based, ML-ready)
* **`router.py`** – Chooses best available rail (CBDC, stablecoin, RTP, agent)
* **`did_checker.py`** *(planned)* – Validates user credentials (DID/VC)
* **`voucher_logic.py`** – Generates and enforces rules for programmable vouchers
* **`multi_payout_simulator.py`** – Batch payout engine for NGO disbursement
* **`compliance_flags.json`** – Tracks regulatory or audit metadata (voucher redeemed, DID matched, etc.)

---

### 3. **Integration Layer (Rails)**

All rails are treated as plug-and-play modules:

* **`mock_cbdc_delivery.py`** – CBDC simulation (e.g., eAED → ePHP)
* **`stablecoin_mock.py`** – USDC-like delivery rail to agents or wallets
* **`nexus_bridge.py`** – Simulates BIS Nexus-compatible RTP rails
* **`simulate_api_bridge.py`** *(upcoming)* – Mock SEPA, mBridge, or Circle CCTP
* **`rail_registry.py`** – Live status map of which rails are available

> You can remove, upgrade, or replace any rail without disrupting other modules — **that’s what makes PAIN modular**.

---

### 4. **Data Layer**

* **Anchored Logs** – JSON receipts saved for auditability (`logs/anchored_receipts.json`)
* **Voucher Metadata** – Tracks rules, expiry, and usage state
* **FX & Compliance Inputs** – Switchable between mock, API, or future real-time sources

---

## Modular Services and Their Roles

| Service / Module      | Role                                                          |
| --------------------- | ------------------------------------------------------------- |
| `CLI Wallet`          | Frontline for capturing payment intent                        |
| `FX Optimizer`        | Suggests optimal timing or urgency routing                    |
| `Routing Engine`      | Chooses best rail based on FX, country, urgency, availability |
| `Delivery Modules`    | Simulate final step: CBDC, stablecoin, bank rails             |
| `Voucher Engine`      | Generate and validate programmable CBDC grants                |
| `Rail Registry`       | Real-time status of corridor availability                     |
| `Compliance Layer`    | Future plug-in for DID checks, ZK flags, behavioral risk      |
| `Multi-Payout Engine` | Disburse funds in batch using same logic stack                |

---

## Why Is This Modular?

| Property                         | Reason                                              |
| -------------------------------- | --------------------------------------------------- |
| **Plug-in Rails**                | Add/remove delivery types without rewriting logic   |
| **Switchable FX Engine**         | Easily move from mock logic → ML model or API       |
| **Swappable Compliance Modules** | From rule-based logic to DID to zkKYC               |
| **Separation of Concerns**       | Routing, compliance, delivery are separated         |
| **Cross-usecase Reusability**    | Aisha, Maria, Luca, NGO, G2P all use the same stack |

---

## Security & Audit Considerations

* **Every delivery is logged and anchored**
* **Voucher redemption includes validation + expiry**
* **DID checks and compliance layers will prevent misuse or leaks**
* **Future: zkCompliance hooks to maintain user privacy while satisfying regulation**

---

## Extending the Protocol

| Direction                  | Module                                                              |
| -------------------------- | ------------------------------------------------------------------- |
| **ML FX Models**           | Replace logic in `fx_model.py` with real models (LSTM, ARIMA, etc.) |
| **DID Integration**        | Hook in DIDKit or other decentralized ID frameworks                 |
| **FraudSight Integration** | Add `fraud_layer.py` to pre-screen transactions                     |
| **Analytics Dashboard**    | Build on top of anchored logs (e.g., Streamlit, Supabase)           |
| **Sandbox Testing**        | Export routes to mBridge, Circle, or Nexus-compatible APIs          |

---
