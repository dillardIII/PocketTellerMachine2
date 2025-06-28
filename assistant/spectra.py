"""
Spectra Assistant Alert System
Used to notify PTM personas (Mentor, Mo Cash, etc.) during critical system states.
Activated by council_alert_reflex or voice commands.
"""

import datetime

PERSONA_REGISTRY = {
    "spectra": "💠",
    "mentor": "🧓",
    "mo_cash": "💸",
    "strategist": "📊",
    "drill_instructor": "🪖",
    "shadow": "🌑",
    "optimist": "🌞"
}

def alert_personas(reason="unspecified"):
    timestamp = datetime.datetime.utcnow().isoformat()
    print(f"\n🔔 [Spectra Alert System @ {timestamp}] Reason: {reason}")
    
    for name, emoji in PERSONA_REGISTRY.items():
        alert_msg = generate_alert_message(name, reason)
        print(f"{emoji} {name.title()} ALERT: {alert_msg}")

def generate_alert_message(persona, reason):
    responses = {
        "drift": {
            "spectra": "System drift detected. Initiating stabilization protocols.",
            "mentor": "The AI is veering off course. I'll analyze and advise.",
            "mo_cash": "Yo, something ain’t right with the data. I'm watching it.",
            "strategist": "Drift observed. Calculating fallback options.",
            "drill_instructor": "The bot is off mission. Recalibrating now!",
            "shadow": "The system's essence is flickering. I’m already inside it.",
            "optimist": "No worries—just a hiccup. We'll fix it together!"
        },
        "corruption": {
            "spectra": "Integrity compromised. Ghost cells being scanned.",
            "mentor": "That’s not good. Let’s run a full wisdom pass.",
            "mo_cash": "Uh-oh, code rot detected. Gotta clean house.",
            "strategist": "Strategic integrity is at risk. Deploying defenses.",
            "drill_instructor": "Your AI's code just got fragged. Scrub and reload!",
            "shadow": "Whispers say your files are bleeding.",
            "optimist": "Every system gets sick sometimes. Healing initiated!"
        }
    }

    category = "drift" if "drift" in reason else "corruption"
    return responses.get(category, {}).get(persona, "I’m on it. Let’s stabilize PTM.")

# Optional CLI test
if __name__ == "__main__":
    alert_personas("drift_detected")