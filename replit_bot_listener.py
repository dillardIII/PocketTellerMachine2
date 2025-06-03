# === FILE: replit_bot_listener.py ===
# Listens for GPT commands via WebSocket and triggers AutoFix on demand.

import asyncio
import websockets
import subprocess

PORT = 8765  # You can change this if needed

TRIGGER_COMMAND = "run_autofix"
RESPONSE_OK = "✅ AutoFix triggered."
RESPONSE_ERR = "❌ AutoFix failed."

async def handler(websocket):
    async for message in websocket:
        print(f"[ReplitBot] 📥 Received message: {message}")

        if message == TRIGGER_COMMAND:
            try:
                print("[ReplitBot] 🔧 Running AutoFix Engine...")
                subprocess.run(["python3", "autofix_engine.py"], check=True)
                await websocket.send(RESPONSE_OK)
                print("[ReplitBot] ✅ AutoFix completed.")
            except subprocess.CalledProcessError as e:
                await websocket.send(RESPONSE_ERR)
                print(f"[ReplitBot] ❌ AutoFix failed: {e}")
        else:
            await websocket.send("🤖 Unknown command.")

# === Launch Server ===
async def main():
    print(f"[ReplitBot] 🚀 WebSocket server starting on port {PORT}...")
    async with websockets.serve(handler, "localhost", PORT):
        print("[ReplitBot] 🎧 Listening for incoming messages...")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())