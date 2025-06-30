from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
from datetime import datetime

INPUT_FILE = "data/trades.json"
REVIEW_OUTPUT_FILE = "data/trade_review_report.json"
VOICE_SUMMARY_OUTPUT_FILE = "data/trade_voice_summary.json"

def analyze_trades_for_review(trade_file):
    try:
        with open(trade_file, "r") as f:
            trades = json.load(f)
    except Exception as e:
        print(f"[REVIEW ERROR]: Cannot load trade file. {e}")
        return [], []

    review_report = []
    voice_summaries = []

    for trade in trades:
        review = {}
        review["id"] = trade.get("id")
        review["symbol"] = trade.get("symbol")
        review["strategy"] = trade.get("strategy")
        review["result"] = trade.get("result")
        review["grade"] = trade.get("grade", "N/A")
        review["timestamp"] = trade.get("timestamp")

        # --- AI review logic ---
        result = trade.get("result", 0)
        if isinstance(result, str):
            try:
                result = float(result)
            except:
                result = 0

        if result > 10:
            review["review"] = "Good trade. Profit exceeded expectations."
        elif result < -10:
            review["review"] = "Warning: High loss. Review strategy and market conditions."
        else:
            review["review"] = "Neutral trade. Small gain or acceptable loss."

        review_report.append(review)

        # --- Voice-ready summary ---
        voice_summaries.append({
            "voice_summary": f"Trade on {trade.get('symbol')} using {trade.get('strategy')} resulted in {result} dollars.",
            "result": result,
            "grade": trade.get("grade", "N/A"),
            "timestamp": trade.get("timestamp")
        })

    return review_report, voice_summaries

def save_review_reports(reviews, voice_summaries):
    with open(REVIEW_OUTPUT_FILE, "w") as f:
        json.dump(reviews, f, indent=2)
    with open(VOICE_SUMMARY_OUTPUT_FILE, "w") as f:
        json.dump(voice_summaries, f, indent=2)
    print(f"[REVIEW COMPLETE]: Reports saved to {REVIEW_OUTPUT_FILE} and {VOICE_SUMMARY_OUTPUT_FILE}")

# === Run Review Process ===
if __name__ == "__main__":
    reviews, voice_summaries = analyze_trades_for_review(INPUT_FILE)
    save_review_reports(reviews, voice_summaries)

def log_event():ef drop_files_to_bridge():