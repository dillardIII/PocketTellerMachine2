# ghostbot/malik_voice_response.py

def style_as_malik(intel_text, ticker=""):
    # Simple tone wrapper for Malik’s smooth intel delivery
    intro = f"Alright partner, here's what I found on {ticker.upper()}..." if ticker else "Alright partner, here’s what I picked up..."

    outro = "Let me know if you want to dig deeper or break it down by sector."

    return f"{intro}\n\n{intel_text}\n\n{outro}"