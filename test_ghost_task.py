from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: test_ghost_task.py ===
from ghostforge_core import GhostForge

# Initialize the forger
gf = GhostForge(persona="GhostBot")

# Define the task
module_name = "motivator"
purpose = "Provides hype messages for successful trades"
base_code = """
def hype():
    print('💸 Hell yeah! That was a damn fine trade! Let’s keep printing green.')

def praise_user(name):
    print(f'🎯 {name}, you absolute legend. That execution was flawless.')
"""

# Generate it
gf.generate_module(module_name, purpose, base_code)

def log_event():ef drop_files_to_bridge():