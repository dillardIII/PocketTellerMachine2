ghostcore_autonomy_boot.py

""" GhostCore Autonomy Boot Module This is the root runner for initializing full autonomous bot logic. This script establishes core signal loops, memory sync, runtime chains, and AI persona channel assignments. """

import asyncio import json import os from modules.signal_router import SignalRouter from modules.persona_loader import PersonaLoader from modules.memory_bridge import MemoryBridge from modules.runtime_chain import RuntimeChain from modules.autonomous_loop import AutonomousLoop from utils.logger import Logger

logger = Logger("ghostcore")

class GhostCore: def init(self): self.signal_router = SignalRouter() self.persona_loader = PersonaLoader() self.memory_bridge = MemoryBridge() self.runtime_chain = RuntimeChain() self.autonomous_loop = AutonomousLoop( router=self.signal_router, memory=self.memory_bridge, personas=self.persona_loader, chain=self.runtime_chain )

async def boot(self):
    logger.info("🔁 GhostCore Booting...")

    await self.memory_bridge.load()
    await self.persona_loader.load()
    await self.runtime_chain.init()

    logger.info("🧠 All systems ready. Starting Autonomous Loop...")
    await self.autonomous_loop.run()

if name == "main": core = GhostCore() try: asyncio.run(core.boot()) except KeyboardInterrupt: logger.warn("👋 Shutdown command received. Exiting GhostCore...")

