from ghost_env import INFURA_KEY, VAULT_ADDRESS
#=== FILE: core/message_router.py ===

""" Message Router: Central dispatch system that lets bots send messages, files, or tasks to each other. """ import os import json from datetime import datetime from cole_logger import log_event

ROUTER_DIR = "data/router" os.makedirs(ROUTER_DIR, exist_ok=True)

def send_packet(sender, recipient, payload): """ Creates a packet from one bot to another. payload = {"type": "strategy", "data": {...}} """ packet = { "sender": sender, "recipient": recipient, "timestamp": datetime.utcnow().isoformat(), "payload": payload } path = os.path.join(ROUTER_DIR, f"to_{recipient}.json") with open(path, "w") as f: json.dump(packet, f, indent=2) log_event("Router", f"📦 Packet sent from {sender} to {recipient}", "info")

def receive_packet(bot_name): """Bot reads its inbox for new packets.""" path = os.path.join(ROUTER_DIR, f"to_{bot_name}.json") if not os.path.exists(path): return None try: with open(path, "r") as f: packet = json.load(f) os.remove(path) log_event("Router", f"📬 {bot_name} received a packet.", "info") return packet except Exception as e: log_event("Router", f"❌ Error reading packet: {e}", "error") return None

=== Manual test ===

if name == "main": send_packet("cole", "strategist", {"type": "strategy", "data": {"symbol": "AAPL"}}) packet = receive_packet("strategist") print(packet)

