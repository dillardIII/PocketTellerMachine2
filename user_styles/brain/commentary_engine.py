import random

def generate_persona_comment(trade):
    symbol = trade.get("symbol", "a stock")
    result = trade.get("result", "").lower()
    strategy = trade.get("strategy", "a strategy")

    if result == "win":
        comments = [
            f"Clean win on {symbol} using {strategy}. Keep that same energy.",
            f"{symbol} came through strong — textbook execution.",
            f"You finessed {symbol} like a pro. Well played."
        ]
        speaker = "Mo Cash"
    elif result == "loss":
        comments = [
            f"Took a hit on {symbol}. Don’t sweat it — revise and reload.",
            f"{symbol} didn’t cooperate. Time to tighten the playbook.",
            f"That one stung, but you’re learning. Push forward."
        ]
        speaker = "Drill Instructor"
    elif result == "break-even":
        comments = [
            f"{symbol} flatlined. No loss is still a win in some plays.",
            f"Breakeven on {symbol}. Watch for stronger setups next time.",
            f"{strategy} neutralized risk. Nice defense."
        ]
        speaker = "Mentor"
    else:
        comments = [f"Still analyzing the result for {symbol}."]
        speaker = "Analyst"

    return {
        "speaker": speaker,
        "quote": random.choice(comments)
    }