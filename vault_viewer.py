# === FILE: vault_viewer.py ===

# 🔐 Vault Viewer – Displays system logs, vault contents, and filtered ghost files

import os
import json

# Optional: Import ghost filter logic if defined elsewhere
try:
    from ghost_filter import GhostFilter
except ImportError:
    GhostFilter = None
    print("[VaultViewer] ⚠️ GhostFilter module not found. Ghost filtering disabled.")

LOG_FILE = "ghostforge_log.json"

class VaultViewer:
    def __init__(self, vault_path="vault/", log_path="logs/ghost_findings.txt"):
        self.vault_path = vault_path
        self.log_path = log_path
        self.ghost_filter = GhostFilter(vault_path=self.vault_path) if GhostFilter else None

    def list_all_files(self):
        files = []
        for root, _, filenames in os.walk(self.vault_path):
            for f in filenames:
                path = os.path.join(root, f)
                files.append(path)
        return files

    def list_ghost_files(self):
        if not os.path.exists(self.log_path):
            return []
        with open(self.log_path, "r") as f:
            return [json.loads(line) for line in f.readlines()]

    def render_summary(self):
        all_files = self.list_all_files()
        ghost_files = self.list_ghost_files()
        summary = {
            "total_files": len(all_files),
            "ghost_hits": len(ghost_files),
            "ghost_files": ghost_files
        }
        return summary

# === Legacy Vault Log Viewer ===
def view_vault_log():
    if not os.path.exists(LOG_FILE):
        print("[Vault] ❌ No vault log found.")
        return

    with open(LOG_FILE, "r") as f:
        entries = json.load(f)
        for entry in entries:
            print(f"[Vault] 📄 {entry['file']} | {entry['action']} @ {entry['timestamp']}")

# === Standalone Test ===
if __name__ == "__main__":
    print("\n=== VAULT SUMMARY ===")
    viewer = VaultViewer()
    report = viewer.render_summary()
    print(f"Total Files: {report['total_files']}")
    print(f"Ghost Files: {report['ghost_hits']}")
    for g in report["ghost_files"]:
        print(f"👻 {g['file']} → {g['hits']}")

    print("\n=== GHOSTFORGE LOG ===")
    view_vault_log()
    print("=======================")