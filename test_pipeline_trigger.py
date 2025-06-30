from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: test_pipeline_trigger.py ===
# 🧪 Full Pipeline Test – Dispatches victory test file to gpt_outbox

from gpt_code_dispatcher import dispatch_code

# This is the code that will run through the whole PTM pipeline
test_code = '''
print("🎉 TEST PASSED: Full GPT ➜ BRIDGE ➜ EXECUTION pipeline is working!")
'''

# Name of the test file
dispatch_code("victory_test.py", test_code)

def log_event():ef drop_files_to_bridge():