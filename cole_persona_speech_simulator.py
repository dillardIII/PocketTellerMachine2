# cole_persona_speech_simulator.py

import random
from cole_ai_emotional_response_composer import compose_emotional_response

# === Sample Personas and Example Messages ===
PERSONAS = ["MoCash", "Mentor", "DrillInstructor"]
MESSAGES = [
    "Market is heating up, stay alert.",
    "We've analyzed the last 10 trades. Adjustments incoming.",
    "Keep your strategy tight and risk low.",
    "Excellent job team. Let's move forward with confidence."
]

# === Simulate persona dialogue ===
def simulate_persona_speech(persona):
    message = random.choice(MESSAGES)
    response = compose_emotional_response(persona, message)
    return response

# === Simulation Loop ===
def run_simulation(cycles=5):
    print("[PERSONA SPEECH SIMULATION]: Starting...")
    for _ in range(cycles):
        for persona in PERSONAS:
            speech = simulate_persona_speech(persona)
            print(f"[{persona}]: {speech}")

if __name__ == "__main__":
    run_simulation()