# === FILE: ghost_filter.py ===

# 👻 GhostFilter – Filters vault files for anomalies, haunted tags, and suspicious traits

import os
import hashlib
import time
import json

class GhostFilter:
    def __init__(self, vault_path="vault/", log_path="logs/ghost_findings.txt"):
        self.vault_path = vault_path
        self.log_path = log_path
        self.ghost_signatures = [
            "🧟", "haunted", "possession", "unknown_origin", "corrupted",
            "👻", "spectral", "phantom", "anomaly", "poltergeist"
        ]
        self.previous_hashes = {}

    def file_hash(self, path):
        with open(path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def scan(self):
        findings = []
        for root, _, files in os.walk(self.vault_path):
            for file in files:
                full_path = os.path.join(root, file)
                try:
                    hash = self.file_hash(full_path)
                    if full_path in self.previous_hashes and self.previous_hashes[full_path] != hash:
                        findings.append({"file": full_path, "hits": ["mutation"]})
                    else:
                        self.previous_hashes[full_path] = hash

                    with open(full_path, "r", errors="ignore") as f:
                        content = f.read().lower()
                        hits = [sig for sig in self.ghost_signatures if sig in content]
                        if hits:
                            findings.append({"file": full_path, "hits": hits})

                except Exception as e:
                    findings.append({"file": full_path, "hits": [f"error: {e}"]})

        self.log_findings(findings)
        return findings

    def log_findings(self, findings):
        if not findings:
            return
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        with open(self.log_path, "a") as log:
            for finding in findings:
                log.write(json.dumps(finding) + "\n")
        print(f"[GhostFilter] 👻 Logged {len(findings)} ghost findings.")

# === Standalone Run ===
if __name__ == "__main__":
    gf = GhostFilter()
    results = gf.scan()
    print(f"\n=== Ghost Scan Complete ===")
    for r in results:
        print(f"👻 {r['file']} → {r['hits']}")