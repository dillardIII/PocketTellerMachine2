from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: test_cole_brain.py ===
"""
Test Script for cole_brain.py:
Runs a full set of read/write/clear tests on the brain memory system.
"""

from cole_brain import log_memory, get_last, clear_memory, get_log_file
import os

TEST_CATEGORY = "test_memory"
TEST_VALUE = "This is a memory test value."

def run_memory_test():
    print("\n=== 🧠 Cole Brain Memory Test ===")
    
    # 1. Clear any prior test memory
    print("[TEST] Clearing test memory...")
    clear_memory(TEST_CATEGORY)

    # 2. Log test value
    print(f"[TEST] Logging: ({TEST_CATEGORY}) = '{TEST_VALUE}'")
    log_memory(TEST_CATEGORY, TEST_VALUE)

    # 3. Retrieve value
    print("[TEST] Retrieving last memory entry...")
    retrieved = get_last(TEST_CATEGORY)
    print(f"[TEST] Retrieved: '{retrieved}'")

    # 4. Check correctness
    if retrieved == TEST_VALUE:
        print("✅ PASS: Memory value correctly saved and retrieved.")
    else:
        print("❌ FAIL: Memory value mismatch.")
        print(f"   Expected: {TEST_VALUE}")
        print(f"   Got:      {retrieved}")

    # 5. File existence check
    brain_file = get_log_file()
    if os.path.exists(brain_file):
        print(f"📁 PASS: Brain file exists at: {brain_file}")
    else:
        print("❌ FAIL: Brain file not found!")

    # 6. Final clear and confirm
    print("[TEST] Clearing memory again...")
    clear_memory(TEST_CATEGORY)
    cleared = get_last(TEST_CATEGORY)
    if cleared is None:
        print("✅ PASS: Memory cleared successfully.")
    else:
        print("❌ FAIL: Memory not cleared. Value still exists:", cleared)

if __name__ == "__main__":
    run_memory_test()

def log_event():ef drop_files_to_bridge():