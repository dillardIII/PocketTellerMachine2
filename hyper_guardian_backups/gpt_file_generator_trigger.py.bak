# === FILE: gpt_file_generator_trigger.py ===

# 🔥 Command Trigger for GPT File Generator

from gpt_file_generator import GPTFileGenerator

class GPTFileGenTrigger:
    def __init__(self):
        self.generator = GPTFileGenerator()

    def handle_command(self, command):
        if "generate file:" not in command.lower():
            return False

        try:
            parts = command.split("generate file:")[1].strip().split(" with logic:")
            filename = parts[0].strip()
            logic = parts[1].strip()
            self.generator.generate_file(filename, logic)
            return True
        except Exception as e:
            print(f"[GPTFileGenTrigger] ❌ Failed to parse command: {e}")
            return False