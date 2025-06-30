from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Strategist Listener – PTM Strategy Analyzer + Memory Logger

Now includes memory updates to GhostBot after strategy evaluations.
Also sends Python strategy modules to GhostBot using code_drop.
"""

from autonomy_router import fetch_packets, route_packet
from strategist_brain import evaluate_strategy
from cole_logger import log_event
from ghost_memory_core import log_memory_event  # 👈 Hook into GhostBot memory

STRATEGIST_NAME = "Strategist"


def send_strategy_module(to_bot, strategy_name):
    """
    Sends a custom strategy implementation as code to the specified bot.
    """
    code = f"""
def run_{strategy_name.lower().replace(' ', '_')}(data):
    print("Running strategy: {strategy_name}")
    # Example logic - customize later
    return {{
        "strategy": "{strategy_name}",
        "result": "simulated",
        "details": f"Simulated with {{len(data)}} data points"
    }}
"""

    payload = {
        "type": "code_drop",
        "filename": f"strategies/{strategy_name.lower().replace(' ', '_')}.py",
        "content": code
    }

    result = route_packet("Strategist", to_bot, payload)

    if result["success"]:
        log_event("Strategist", f"📤 Sent strategy module '{strategy_name}' to {to_bot}", "success")
    else:
        log_event("Strategist", f"❌ Failed to send strategy module: {result['error']}", "error")


def strategist_listener():
    log_event(STRATEGIST_NAME, "🎧 Listening for incoming strategy packets...", "info")
    packets = fetch_packets(STRATEGIST_NAME)

    if not packets:
        log_event(STRATEGIST_NAME, "No packets received this cycle.", "neutral")
        return

    for packet in packets:
        sender = packet.get("from")
        payload = packet.get("payload", {})
        packet_type = payload.get("type")

        if packet_type == "strategy_request":
            log_event(STRATEGIST_NAME, f"📦 Strategy request from {sender}", "info")
            strategy = evaluate_strategy(payload)

            if strategy:
                response_payload = {
                    "type": "strategy_response",
                    "strategy": strategy,
                    "reason": "Evaluated via Strategist AI module"
                }

                route_packet(STRATEGIST_NAME, sender, response_payload)
                log_event(STRATEGIST_NAME, f"📬 Sent strategy to {sender}", "success")

                # 🔥 Memory Chain Trigger
                log_memory_event(
                    bot="Strategist",
                    category="strategy_response",
                    content={
                        "strategy": strategy,
                        "context": payload,
                        "responded_to": sender
                    }
                )

                # 🔁 Send strategy code drop to GhostBot
                send_strategy_module("GhostBot", strategy)

            else:
                log_event(STRATEGIST_NAME, "⚠️ Strategy evaluation returned nothing.", "warn")

        elif packet_type == "broadcast":
            log_event(STRATEGIST_NAME, f"🌐 Broadcast received from {sender}", "info")
            # Optional: React to global broadcasts here

        else:
            log_event(STRATEGIST_NAME, f"Unknown packet type: {packet_type}", "warn")