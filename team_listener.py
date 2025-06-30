from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: team_listener.py ===
from team_comm_router import read_inbox, clear_inbox, send_packet

def process_packet(packet, team_name):
    sender = packet['sender']
    data = packet['data']
    msg_type = packet['type']

    print(f"[{team_name} RECEIVED] From: {sender} | Type: {msg_type}")
    print(f"  >> {data}")

    # Example: Echo logic
    if msg_type == "ping":
        response = {
            "reply": "pong",
            "received_at": packet["timestamp"]
        }
        send_packet(build_packet(team_name, sender, "pong", response))

def listen_for_packets(team_name):
    packets = read_inbox(team_name)
    if not packets:
        print(f"[{team_name}] Inbox empty.")
        return

    for packet in packets:
        process_packet(packet, team_name)

    clear_inbox(team_name)

def log_event():ef drop_files_to_bridge():