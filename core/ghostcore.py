# === FILE: core/ghostcore.py ===

# 👻 GhostCore – Core flag logic for PTM's AI systems, phase toggles, and takeover verification

GHOST_ACTIVE = True
GHOST_PHASE = "Phase 7 – GhostNet Online"
GHOST_UPLINK = {
    "perplexity": True,
    "openai": True,
    "elevenlabs": True,
    "whisper": True,
    "metamask": True
}

def ghost_status():
    return {
        "status": "active" if GHOST_ACTIVE else "inactive",
        "phase": GHOST_PHASE,
        "uplinks": GHOST_UPLINK
    }

def display_ghost_banner():
    print(r"""
     ██████╗  ██████╗  ██████╗ ███████╗████████╗
    ██╔═══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝
    ██║   ██║██║   ██║██║   ██║███████╗   ██║   
    ██║   ██║██║   ██║██║   ██║╚════██║   ██║   
    ╚██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   
     ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   
    """)

    print(f"[GhostCore] 👻 STATUS: {ghost_status()['status']}")
    print(f"[GhostCore] 🔮 Phase: {GHOST_PHASE}")
    print(f"[GhostCore] 🔗 AI Uplinks: {', '.join([k for k, v in GHOST_UPLINK.items() if v])}")

if __name__ == "__main__":
    display_ghost_banner()