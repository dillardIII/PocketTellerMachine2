# === FILE: gpt_command_handler.py ===

from gpt_file_dropper import drop_file

def handle_command(command):
    if command.startswith("drop_file:"):
        try:
            _, filename, file_content = command.split(":", 2)
            drop_file(filename.strip(), file_content.strip())
            return f"[GPT Handler] ✅ File dropped: {filename}"
        except Exception as e:
            return f"[GPT Handler] ❌ Failed to drop file: {e}"
    else:
        return f"[GPT Handler] ❓ Unknown command: {command}"