from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot_initiator.py ===
from team_comm_router import build_packet, send_packet
from team_listener import listen_for_packets

# Simulate sending a file or message
def example_send():
    packet = build_packet(
        sender="Cole",
        recipient="Strategist",
        content_type="ping",
        data={"msg": "Yo Strat, what’s the play today?"}
    )
    send_packet(packet)

# Simulate Cole checking his inbox
def example_listen():
    listen_for_packets("Cole")
    listen_for_packets("Strategist")

if __name__ == "__main__":
    example_send()
    example_listen()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():