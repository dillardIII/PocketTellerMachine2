from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: rebuild_ghostforge_core.py ===
# 🔧 Rebuilds ghostforge_core.py – AI code writing brain

with open("ghostforge_core.py", "w") as f:
    f.write('''# === FILE: ghostforge_core.py ===
class GhostForgeCore:
    def write_code(self, filename, content):
        with open(filename, "w") as f:
            f.write(content)
        print(f"[GhostForgeCore] ✅ Wrote {filename}")
''')
print("[rebuild_ghostforge_core] ✅ ghostforge_core.py rebuilt.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():