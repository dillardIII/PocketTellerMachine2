# Voice Engine (Basic Trigger Logic)
def speak(text):
    try:
        from output_mp3_fallback import play_audio
        print(f"[VoiceEngine] 🔊 Speaking: {text}")
        play_audio("static/audio/output.mp3")  # Placeholder
    except Exception as e:
        print(f"[VoiceEngine] ❌ Error playing voice: {e}")