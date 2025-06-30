# === FILE: uplink_controller.py ===
# 🔌 Uplink Controller – Master switch for AI integrations (Whisper, OpenAI, Perplexity, ElevenLabs, MetaMask)

from uplinks.whisper_transcriber import listen_and_transcribe
from uplinks.openai_sync import sync_openai
from uplinks.perplexity_feed import fetch_intel
from uplinks.elevenlabs_voice import speak_response
from uplinks.metamask_sync import pull_wallet_balances

def initialize_uplink():
    print("[Uplink] 🔌 Initializing Phase 6 AI connections...")
    
    # === Voice to Text ===
    listen_and_transcribe()

    # === Language Intelligence ===
    sync_openai()

    # === Market Intel ===
    fetch_intel()

    # === AI Persona Speech ===
    speak_response("All AI uplinks are now online. Let's dominate, Boo.")

    # === Crypto Wallet Sync ===
    pull_wallet_balances()

    print("[Uplink] ✅ All AI uplinks active.")