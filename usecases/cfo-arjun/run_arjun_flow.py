# usecases/cfo-arjun/run_arjun_flow.py

import json
import os
import sys
from tabulate import tabulate  # built-in friendly table display

# Import FX Engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../fx-optimizer')))
from fx_model import predict_fx_timing

def load_invoices(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def run_arjun_flow():
    print("PAIN Protocol – Arjun’s FX & Treasury Simulator\n")

    invoices = load_invoices("usecases/cfo-arjun/invoices.json")
    rows = []

    for invoice in invoices:
        currency_pair = f"INR/{invoice['currency']}"
        fx_advice = predict_fx_timing(currency_pair, invoice["amount"], "medium")

        row = [
            invoice["invoice_id"],
            invoice["vendor"],
            invoice["currency"],
            f"${invoice['amount']}",
            f"{invoice['due_in_days']} days",
            fx_advice
        ]
        rows.append(row)

    headers = ["Invoice ID", "Vendor", "Currency", "Amount", "Due In", "FX Advice"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    run_arjun_flow()