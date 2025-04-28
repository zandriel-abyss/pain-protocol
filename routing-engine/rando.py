import sys
import os

# Dynamically locate project root to find payment-rails modules
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), r"C:\\Users\\jzack\\ML Projects\\pain-protocol"))
sys.path.append(os.path.join(ROOT_DIR, "payment-rails"))


from rail_registry import simulate_random_rail_outage, RAIL_STATUS, reset_all_rails

# Simulate a random outage
simulate_random_rail_outage()

# Check rail status
print("\n Current Rail Status:")
print(RAIL_STATUS)