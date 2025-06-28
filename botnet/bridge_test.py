"""
Bridge Test:
Simulates multi-bot interaction using the bridge_relay router.
Verifies message delivery, handler responses, and shared context memory.
"""

from botnet.bridge_relay import relay_message

# Shared memory (could be expanded to simulate a knowledge base)
context = {
    "mission": "Build and launch PTM AI swarm",
    "status": "initializing",
    "logs": []
}

# Simulate PTMBot requesting assistance from ChatGPTBot
msg1 = relay_message("ChatGPTBot", "What's our next task?", sender="PTMBot", context=context)
print(f"[ChatGPTBot → PTMBot] {msg1['response']}")

# Simulate PTMBot updating RefluxBot with context
msg2 = relay_message("RefluxBot", "Sync with latest bridge logic.", sender="PTMBot", context=context)
print(f"[RefluxBot → PTMBot] {msg2['response']}")

# Simulate RefluxBot sending a status check to PTMBot
msg3 = relay_message("PTMBot", "Status update requested.", sender="RefluxBot", context=context)
print(f"[PTMBot → RefluxBot] {msg3['response']}")