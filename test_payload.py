from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: test_payload.py ===

# 🎉 Payload Test – Confirms PTM can process files autonomously

print("[TestPayload] ✅ Payload received and executed.")
with open("ptm_outbox/payload_result.txt", "w") as f:
    f.write("Payload executed successfully by PTM.")

def log_event():ef drop_files_to_bridge():