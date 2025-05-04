# 🗺️ PAIN Protocol – Development Roadmap

This document outlines the phased development of the **Programmable AI-powered Interoperable Network (PAIN)** Protocol. Each phase includes goals, modules, and completed vs upcoming tasks.

---

## 🚀 Phase 1 – Core Flows (Completed ✅)

### 🎯 Goal:
Build foundational logic for programmable payment routing and anchored audit trails.

### ✅ Features:
- CLI Wallet MVP
- AI-powered FX model (rule-based)
- Routing engine with rail selection
- Simulated CBDC and stablecoin delivery
- Anchored receipt logs

### 🧪 Use Cases:
- ✅ Maria (CBDC Remittance UAE → PH)
- ✅ Aisha (Freelancer payout: convert + save)

---

## 🌍 Phase 2 – Integrations & Simulations (In Progress 🟡)

### 🎯 Goal:
Simulate integration with real-world rails and prepare for pilot-ready prototypes.

### ✅ Done:
- Rail registry with live status
- Fallback logic in routing engine
- NGO payout batch simulator (multi-send)
- Stablecoin delivery mock
- `simulate_api_bridge.py` for future API integration (e.g., Circle, SEPA, mBridge)
- Test notebook for outage simulation

### 🟡 Current:
- DID credential simulation for onboarding
- Anchor compliance + expiry rules (vouchers)
- Tunde flow: programmable CBDC disbursement
- Arjun flow: treasury FX simulation dashboard

---

## 🧬 Phase 3 – Ecosystem & Privacy (Planned 🔜)

### 🎯 Goal:
Expand into real-time dashboards, explainable fraud detection, privacy safeguards, and plug-in ecosystems.

### 🔜 Features:
- FraudSight module (wallet anomaly detection + reason codes)
- NGO + treasury dashboard analytics (receipts, flags, patterns)
- zk-compliance layer (privacy-preserving controls)
- Mobile app prototype / wallet plug-in
- API sandbox hooks (Circle, mBridge, SEPA)

---

## 📦 By Milestone

| Version | Highlights |
|---------|------------|
| **v0.1** | Core flows, routing, anchoring (✅ Complete) |
| **v0.2** | NGO + voucher use cases, API bridge sim, DID onboarding (🟡 In Progress) |
| **v0.3** | FraudSight ML, dashboards, zk layer, pilot sandbox prep (🔜 Next) |

---

## 📍 Contributors
- Zack – Product Architect & Engineer
- Vishal – Co-founder & Compliance Analyst
