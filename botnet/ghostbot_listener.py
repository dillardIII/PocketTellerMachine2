"""
GhostBot Listener – Handles code drops, imports modules, and optionally executes them.
Supports hybrid mode: auto-run only if `run_immediately: true` is in the payload.
"""

from autonomy_router import fetch_packets, save_code_drop
from cole_logger import log_event
from ghost_memory_core import log_memory_event
import importlib.util
import os

BOT_NAME = "GhostBot"


def ghostbot_listener():
    log_event(BOT_NAME, "👂 Listening for routed packets...", "info")
    packets = fetch_packets(BOT_NAME)

    if not packets:
        log_event(BOT_NAME, "No packets this round.", "neutral")
        return

    for packet in packets:
        payload = packet.get("payload", {})
        packet_type = payload.get("type")

        if packet_type == "code_drop":
            result = save_code_drop(packet)
            if result["success"]:
                module_path = result["saved_to"]
                log_event(BOT_NAME, f"💾 Code file saved: {module_path}", "success")
                log_memory_event(BOT_NAME, "code_received", payload)

                # === Hybrid Mode Execution Check ===
                run_immediately = payload.get("run_immediately", False)

                if run_immediately:
                    try:
                        module_name = os.path.splitext(os.path.basename(module_path))[0]
                        spec = importlib.util.spec_from_file_location(module_name, module_path)
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)

                        # Find any callable starting with "run_"
                        run_func = next(
                            (getattr(module, f) for f in dir(module)
                             if callable(getattr(module, f)) and f.startswith("run_")),
                            None
                        )

                        if run_func:
                            log_event(BOT_NAME, f"⚙️ Auto-running function: {run_func.__name__}", "info")
                            output = run_func(data=[1, 2, 3, 4, 5])
                            log_event(BOT_NAME, f"🧠 Execution Output: {output}", "success")
                            log_memory_event(BOT_NAME, "strategy_execution", output)
                        else:
                            log_event(BOT_NAME, "❌ No run_* function found in module.", "warn")

                    except Exception as e:
                        log_event(BOT_NAME, f"🔥 Failed to execute dropped module: {e}", "error")
                else:
                    log_event(BOT_NAME, "🗂️ Module saved but queued for later execution.", "info")

            else:
                log_event(BOT_NAME, f"❌ Code drop failed: {result['error']}", "error")

        elif packet_type == "memory_share":
            log_event(BOT_NAME, "🧠 Received shared memory event", "info")
            log_memory_event(BOT_NAME, "shared_memory", payload)

        else:
            log_event(BOT_NAME, f"🤷 Unknown packet type: {packet_type}", "warn")