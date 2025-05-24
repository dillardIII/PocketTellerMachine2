# === Voice Mood Mapping System ===

def get_voice_mood_by_trade(trade):
    result = trade.get("result", "pending")
    profit = trade.get("profit", 0)

    if result == "win":
        if profit > 75:
            return "hype"         # Big win
        else:
            return "happy"        # Modest win

    elif result == "loss":
        if abs(profit) > 75:
            return "disappointed" # Big loss
        else:
            return "concerned"    # Light loss

    return "neutral"