from ghost_env import INFURA_KEY, VAULT_ADDRESS
# task_router.py
# Routes interpreted commands to the correct bot, module, or action pipeline.

from auto_fixer_bot import fix_code
from auto_uploader import upload_code
from system_bridge import launch_system_task
from ai_persona_registry import get_persona
import traceback

def route_task(structured_command):
    try:
        action = structured_command.get("action")
        target = structured_command.get("target")
        payload = structured_command.get("payload", {})

        if action == "fix_code":
            return fix_code(payload.get("code", ""), payload.get("language"))

        elif action == "upload_code":
            return upload_code(payload.get("filename"), payload.get("content"))

        elif action == "launch_system_task":
            return launch_system_task(target, payload)

        elif action == "summon_persona":
            persona_name = payload.get("name")
            persona = get_persona(persona_name)
            return f"Persona {persona_name} summoned: {persona.describe()}"

        else:
            return f"[⚠️ Unhandled Action]: {action}"

    except Exception as e:
        traceback.print_exc()
        return f"[ERROR in Task Router]: {str(e)}"

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():