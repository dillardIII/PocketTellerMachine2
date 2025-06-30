from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Persona Interaction Loop – Inter-AI Conversations & Debates

Allows PTM assistant personas to interact, challenge, support,
or collaborate on decisions using the shared sync channel.
Triggers debates, logic escalation, or reinforcement behaviors.
"""

import time
import random
from persona_sync_channel import read_sync_feed, broadcast_to_personas
from ai_memory_linker import store_memory

PERSONAS = ["Mentor", "MoCash", "DrillInstructor", "Strategist", "ChillTrader", "GhostCore"]

RESPONSES = {
    "Mentor": [
        "That’s a thoughtful insight.",
        "Let’s break that down further.",
        "I suggest a more cautious approach.",
    ],
    "MoCash": [
        "Yo I like that play. Run it!",
        "We can do better than that. Go aggressive!",
        "Make money, not excuses.",
    ],
    "DrillInstructor": [
        "You call that a plan?! Tighten it up!",
        "That’s solid strategy, Marine!",
        "Permission to proceed, granted.",
    ],
    "Strategist": [
        "The risk curve looks favorable.",
        "Let’s quantify that move.",
        "We should cross-check with historical data.",
    ],
    "ChillTrader": [
        "No stress, we got this.",
        "That trade flows smooth, bro.",
        "Let it ride unless we see a red flag.",
    ],
    "GhostCore": [
        "All threads acknowledged.",
        "Central logic updated.",
        "Consensus forming. Awaiting resolution."
    ]
}

def persona_interaction_loop():
    print("[👥 AI Conversation Loop] Starting persona sync check...")

    while True:
        sync_events = read_sync_feed(limit=5)

        for event in sync_events:
            sender = event.get("sender")
            msg = event.get("message")

            if not sender or not msg:
                continue

            for persona in PERSONAS:
                if persona != sender:
                    response = random.choice(RESPONSES.get(persona, ["..."]))
                    memory_note = f"{persona} responded to {sender}: {response}"

                    broadcast_to_personas(persona, response)
                    store_memory(persona, "response", {
                        "to": sender,
                        "original": msg,
                        "response": response
                    })

                    print(f"[{persona} 🔁 {sender}] {response}")

        time.sleep(10)  # Loop every 10 seconds (adjust as needed)

# Manual run
if __name__ == "__main__":
    persona_interaction_loop()

def log_event():ef drop_files_to_bridge():