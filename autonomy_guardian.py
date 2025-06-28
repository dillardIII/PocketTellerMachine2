# === FILE: autonomy_guardian.py ===

# 🛡️ Autonomy Guardian – Prevents runaway commands, infinite loops, or recursive logic bombs

dangerous_patterns = ["rm -rf", "infinite", "loop()", "while True", "shutdown"]

def scan_command(command):
    for danger in dangerous_patterns:
        if danger in command:
            print(f"[Guardian] 🚨 BLOCKED DANGEROUS COMMAND: {command}")
            return False
    return True