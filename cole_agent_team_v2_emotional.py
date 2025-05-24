from assistants.malik import malik_report
import random
from cole_agent_competition import record_trade_result, agent_brag_or_panic

# === Emotion & Personality Enhanced Strategist Proposal ===
def strategist_propose(symbol):
    emotion = random.choice(["confident", "neutral", "hesitant"])
    result = round(random.uniform(-50, 100), 2)
    print(f"[STRATEGIST-{emotion.upper()}]: Suggests SMA_Cross for {symbol} → Simulated result: {result}")
    record_trade_result("Strategist", result)
    agent_brag_or_panic("Strategist")
    return {"symbol": symbol, "strategy": "SMA_Cross", "reason": "Technical Analysis", "emotion": emotion, "result": result}

# === Emotion & Personality Enhanced Hustler Push ===
def hustler_push(symbol):
    hype_level = random.choice(["overhyped", "hyped", "neutral", "skeptical"])
    result = round(random.uniform(-100, 150), 2)
    print(f"[HUSTLER-{hype_level.upper()}]: Pushing RSI_Reversal on {symbol} → Simulated result: {result}")
    record_trade_result("Hustler", result)
    agent_brag_or_panic("Hustler")
    return {"symbol": symbol, "strategy": "RSI_Reversal", "reason": "Social Media Hype", "emotion": hype_level, "result": result}

# === Mentor Validates with Mood ===
def mentor_validate(proposal):
    caution_level = random.choice(["strict", "neutral", "lenient"])
    print(f"[MENTOR-{caution_level.upper()}]: Reviewing {proposal['strategy']} on {proposal['symbol']} with result {proposal['result']}.")
    if caution_level == "strict" and proposal["emotion"] in ["overhyped", "confident"]:
        print(f"[MENTOR]: Rejected due to excessive optimism or hype.")
        return False
    print(f"[MENTOR]: Approved.")
    return True

# === Shadow Oversees and Forces Decision if Conflict ===
def shadow_monitor(actions):
    print(f"[SHADOW]: Overseeing team debate...")
    strategies = [a["strategy"] for a in actions]
    if len(set(strategies)) != len(actions):
        print("[SHADOW]: Conflict detected! Forcing team to vote.")
        chosen = random.choice(actions)
        print(f"[SHADOW]: Majority forced agreement on: {chosen['strategy']}")
        return chosen
    else:
        print("[SHADOW]: No conflicts. Proceeding with harmony.")
        return actions[0]

# === Team Debate & Execution (With Emotions + Performance) ===
def ai_team_debate(symbol):
    proposals = []
    strat = strategist_propose(symbol)
    hustle = hustler_push(symbol)
    proposals.append(strat)
    proposals.append(hustle)

    decision = shadow_monitor(proposals)

    if mentor_validate(decision):
        malik_report(f"Team finalized: {decision['strategy']} for {decision['symbol']} ({decision['emotion']}) → {decision['result']}.")
    else:
        print("[AI TEAM]: Trade vetoed by Mentor.")

# === Simplified Competition Mode ===
def ai_team_competition(symbol):
    strat = strategist_propose(symbol)
    hustle = hustler_push(symbol)
    
    # Judge the round winner based on result only
    if strat["result"] > hustle["result"]:
        print("[ROUND RESULT]: Strategist wins the round.")
    elif hustle["result"] > strat["result"]:
        print("[ROUND RESULT]: Hustler wins the round.")
    else:
        print("[ROUND RESULT]: It's a draw.")

# === Example ===
if __name__ == "__main__":
    print("\n[EMOTIONAL TEAM DEBATE MODE]:")
    ai_team_debate("TSLA")

    print("\n[COMPETITION MODE]:")
    ai_team_competition("TSLA")