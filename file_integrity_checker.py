# file_integrity_checker.py – Scans PTM system for file/import mismatches

import os

EXPECTED_FILES = {
    "cole_live_injector.py": ["inject_cole"],
    "core_memory_logger.py": ["log_core_memory"],
    "boot_autonomy.py": ["Flask", "CORS", "status_api"],
    "autonomy_lock_key.py": ["MemoryKernel", "SelfHealingWatcher", "VPSBridge"],
    "token_fetcher_bot.py": ["TokenFetcherBot"],
}

def validate_file_structure(base_path="."):
    print("[FileChecker] 🔎 Scanning file structure for inconsistencies...\n")
    missing_files = []
    mismatch_alerts = []

    for filename, expected_imports in EXPECTED_FILES.items():
        filepath = os.path.join(base_path, filename)
        if not os.path.exists(filepath):
            print(f"❌ Missing file: {filename}")
            missing_files.append(filename)
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        for imp in expected_imports:
            if imp not in content:
                mismatch_alerts.append(f"⚠️ '{imp}' not found in {filename}")
    
    if not missing_files and not mismatch_alerts:
        print("✅ All expected files and imports are present.\n")
    else:
        print("\n--- VALIDATION REPORT ---")
        for alert in mismatch_alerts:
            print(alert)
        if missing_files:
            print("\nMissing files:", ", ".join(missing_files))

if __name__ == "__main__":
    validate_file_structure()