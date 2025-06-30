# signal_router.py

import asyncio
from ghostcore.memory import SharedMemory
from ghostcore.persona_loader import load_persona_by_role
from ghostcore.signal_definitions import SignalType, CommandSignal, SystemSignal

class SignalRouter:
    def __init__(self, memory: SharedMemory):
        self.memory = memory
        self.handlers = {}

    def register_handler(self, signal_type, handler):
        if signal_type not in self.handlers:
            self.handlers[signal_type] = []
        self.handlers[signal_type].append(handler)

    async def route(self, signal):
        signal_type = signal.get('type')
        if not signal_type or signal_type not in self.handlers:
            print(f"[SignalRouter] ⚠️ Unknown or missing signal type: {signal}")
            return

        handlers = self.handlers[signal_type]
        for handler in handlers:
            try:
                await handler(signal)
            except Exception as e:
                print(f"[SignalRouter] ❌ Error in handler for {signal_type}: {e}")

    async def broadcast(self, signal):
        # Broadcast to all registered handlers regardless of type
        for handlers in self.handlers.values():
            for handler in handlers:
                try:
                    await handler(signal)
                except Exception as e:
                    print(f"[SignalRouter] ❌ Broadcast error: {e}")

# Bootstrap router
shared_memory = SharedMemory()
router = SignalRouter(shared_memory)

# Registering system signal handlers
async def system_handler(signal):
    if signal.get('subtype') == 'PING':
        print("[SignalRouter] 🛰️ Received ping, responding...")
    elif signal.get('subtype') == 'RESTART':
        print("[SignalRouter] 🔄 Restarting system...")

router.register_handler(SignalType.SYSTEM, system_handler)

# If you want to test:
# asyncio.run(router.route({'type': 'SYSTEM', 'subtype': 'PING'}))