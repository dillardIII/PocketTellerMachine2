# === FILE: assistant_dispatch.py ===
# 📢 Assistant Dispatch – Delivers strategies, summaries, alerts, and feedback to the user or dashboard

class AssistantDispatch:
    def __init__(self):
        print("[AssistantDispatch] Ready to relay strategies and updates.")

    def relay_strategy(self, strategy):
        # Print or route the strategy to UI, voice, or log system
        print(f"[AssistantDispatch] 📣 Strategy Recommendation → {strategy['strategy']} | "
              f"Indicator: {strategy['indicator']} | Confidence: {strategy['confidence']*100:.1f}%")

    def send_alert(self, message):
        print(f"[AssistantDispatch] 🚨 ALERT: {message}")

    def summarize_day(self, summary_data):
        # Could later be expanded to create daily recaps with audio or visual output
        print("[AssistantDispatch] 🧾 Daily Summary:")
        for key, value in summary_data.items():
            print(f"  - {key}: {value}")