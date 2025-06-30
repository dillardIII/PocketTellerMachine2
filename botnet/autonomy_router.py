from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Autonomy Router – PTM Botnet Communication Handler

This router handles inter-bot communication and packet handoff logic.
Bots can send, receive, and forward intelligence, build tasks, data packets,
or behavior updates to each other via this channel.
"""

import json
import os
from datetime import datetime
from cole_logger import log_event  # ✅ Logging support

# === ROUTING SYSTEM PATHS ===
ROUTER_LOG_FILE = "logs/autonomy_router_log.json"
BOT_PIPELINE_FILE = "data/bot_pipeline.json"
ROUTING_DIR = "data/bot_packets"

# === Ensure required directories exist ===
os.makedirs(os.path.dirname(ROUTER_LOG_FILE), exist_ok=True)
os.makedirs(os.path.dirname(BOT_PIPELINE_FILE), exist_ok=True)
os.makedirs(ROUTING_DIR, exist_ok=True)


# === PACKET LOGGING ===

def log_router_event(source, destination, payload_type, status, notes=""):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "destination": destination,
        "type": payload_type,
        "status": status,
        "notes": notes
    }

    if os.path.exists(ROUTER_LOG_FILE):
        with open(ROUTER_LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(event)

    with open(ROUTER_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)


# === PACKET ROUTING ===

def route_packet(source, destination, payload):
    """
    Routes a packet between bots using memory and disk.
    Appends the packet to the destination's queue in bot_pipeline.json.
    """
    if not isinstance(payload, dict):
        log_router_event(source, destination, "invalid", "failed", "Payload must be a dictionary.")
        return {"success": False, "error": "Invalid payload format"}

    try:
        packet = {
            "from": source,
            "to": destination,
            "timestamp": datetime.utcnow().isoformat(),
            "payload": payload
        }

        # Load existing pipeline
        if os.path.exists(BOT_PIPELINE_FILE):
            with open(BOT_PIPELINE_FILE, "r") as f:
                pipeline = json.load(f)
        else:
            pipeline = {}

        if destination not in pipeline:
            pipeline[destination] = []

        pipeline[destination].append(packet)

        with open(BOT_PIPELINE_FILE, "w") as f:
            json.dump(pipeline, f, indent=2)

        log_router_event(source, destination, payload.get("type", "unknown"), "routed", "Packet successfully routed.")
        return {"success": True, "message": "Packet routed successfully."}

    except Exception as e:
        log_router_event(source, destination, "exception", "failed", str(e))
        return {"success": False, "error": str(e)}


def broadcast_packet(source, payload):
    """
    Broadcasts a packet to all known bots listed in the pipeline file.
    """
    if os.path.exists(BOT_PIPELINE_FILE):
        with open(BOT_PIPELINE_FILE, "r") as f:
            pipeline = json.load(f)
        all_bots = list(pipeline.keys())
    else:
        all_bots = []

    results = []
    for bot in all_bots:
        result = route_packet(source, bot, payload)
        results.append((bot, result))

    return results


def fetch_packets(bot_name):
    """
    Fetches all packets for a specific bot, clearing the bot's queue after reading.
    """
    if not os.path.exists(BOT_PIPELINE_FILE):
        return []

    with open(BOT_PIPELINE_FILE, "r") as f:
        pipeline = json.load(f)

    messages = pipeline.get(bot_name, [])
    pipeline[bot_name] = []  # Clear queue after reading

    with open(BOT_PIPELINE_FILE, "w") as f:
        json.dump(pipeline, f, indent=2)

    return messages


# === CODE TRANSFER SYSTEM ===

def save_code_drop(packet):
    """
    Saves code dropped from one bot to another into the /drops directory.
    Expected payload:
    {
        "type": "code_drop",
        "filename": "utils/strategy_tester.py",
        "content": "def run_backtest(): ..."
    }
    """
    payload = packet.get("payload", {})
    filename = payload.get("filename")
    content = payload.get("content")

    if not filename or not content:
        return {"success": False, "error": "Missing filename or content."}

    save_path = os.path.join("drops", filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "w") as f:
        f.write(content)

    return {"success": True, "saved_to": save_path}