# 💎 Vault Viewer – Shows everything in your PTM vault directory

import os

VAULT_PATH = "vault"

def show_vault_contents():
    print("[VaultViewer] 🔍 Checking vault contents...")
    if not os.path.exists(VAULT_PATH):
        print(f"[VaultViewer] 🚫 No vault found at '{VAULT_PATH}'")
        return
    for root, dirs, files in os.walk(VAULT_PATH):
        level = root.replace(VAULT_PATH, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")

if __name__ == "__main__":
    show_vault_contents()