# === FILE: ghostnet_router.py ===
# 🧭 GhostNet Router – Routes events or commands between AI nodes/personas

from utils.logger import log_event

def route_message(event):
    sender = event.get("from", "unknown")
    receiver = event.get("to", "unknown")
    msg = event.get("message", "")

    print(f"[Router] 📡 {sender} → {receiver}: {msg}")
    log_event("GhostNetMessage", {
        "from": sender,
        "to": receiver,
        "message": msg
    })

    # Future: Hook in direct AI personas (e.g., ghostbot.handle(), spectra.receive(), etc.)