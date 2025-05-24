import os
import json

DATA_DIR = "data"

REPAIRS = {
    "ghostbot_memory.json": {},
    "watchlist.json": ["AAPL", "TSLA", "MSFT", "NVDA", "QQQ"],
    "backtest_results.json": [],
    "cole_execution_log.json": [],
    "cole_evolved_strategies.json": [],
    "trades.json": [],
    "cole_file_log.json": []
}

def patch_broken_json_files():
    print("=== JSON FILE PATCH: Repairing corrupted or empty files ===\n")
    fixed = []
    for fname, default_value in REPAIRS.items():
        path = os.path.join(DATA_DIR, fname)

        try:
            if not os.path.exists(path) or os.path.getsize(path) == 0:
                raise ValueError("Missing or empty")

            # Try to load it
            with open(path, "r") as f:
                json.load(f)
            print(f"[OK] {fname} is valid.")
        except Exception as e:
            print(f"[FIXING] {fname} — Reason: {e}")
            with open(path, "w") as f:
                json.dump(default_value, f, indent=2)
            fixed.append(fname)

    if fixed:
        print("\n✅ Repaired the following files:")
        for f in fixed:
            print(f" - {f}")
    else:
        print("✅ No repairs needed. All files are good.")

# Optional direct test
if __name__ == "__main__":
    patch_broken_json_files()