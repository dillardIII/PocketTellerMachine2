from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Persona Router
Directs commands and alerts to the appropriate assistant based on:
- Task type (e.g., education, risk, alerts)
- Mood or system state
- User preference or override
"""

from assistants.spectra import alert_personas

PERSONA_TASKS = {
    "mentor": ["teach", "explain", "lesson", "review"],
    "mo_cash": ["profit", "hustle", "fast money", "risk"],
    "strategist": ["plan", "optimize", "spread", "risk check"],
    "drill_instructor": ["train", "discipline", "bootcamp", "command"],
    "shadow": ["analyze", "stealth", "vulnerability", "ghost"],
    "optimist": ["cheer", "encourage", "motivate", "celebrate"]
}

ACTIVE_PERSONA = "mentor"

def route_task(task_description):
    global ACTIVE_PERSONA
    for persona, keywords in PERSONA_TASKS.items():
        if any(kw in task_description.lower() for kw in keywords):
            ACTIVE_PERSONA = persona
            print(f"🔀 Routed to {persona.title()}: handling '{task_description}'")
            return persona
    print(f"⚠️ No clear route for '{task_description}'. Defaulting to Mentor.")
    ACTIVE_PERSONA = "mentor"
    return "mentor"

def handle_alert(alert_type):
    print(f"🚨 Persona Router received alert: {alert_type}")
    alert_personas(reason=alert_type)

def get_active_persona():
    return ACTIVE_PERSONA

# Optional CLI test
if __name__ == "__main__":
    route_task("optimize this risk spread")
    handle_alert("corruption_detected")