from ghost_env import INFURA_KEY, VAULT_ADDRESS
from brain import calculate_grade, execute_trade

# Example trade results to grade
results = [150, 75, 30, 5, -10, -30, -100]

print("[TRADE GRADING TEST]:")
for r in results:
    grade = calculate_grade(r)
    print(f"Result: {r} → Grade: {grade}")

# Simulate a trade and grade
trade = execute_trade("MSFT", "covered_call", 55)
print("[TRADE EXECUTION AND GRADING]:", trade)

def log_event():ef drop_files_to_bridge():