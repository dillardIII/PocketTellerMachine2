# === FILE: command_dispatcher.py ===

# 📬 Command Dispatcher – Sends commands between components, bots, or AI agents

inbox = []

def queue_command(command):
    print(f"[Dispatcher] 📨 Queued: {command}")
    inbox.append(command)

def dispatch():
    while inbox:
        command = inbox.pop(0)
        print(f"[Dispatcher] 🚀 Dispatching: {command}")
        # Placeholder: trigger ReflexEngine or another component