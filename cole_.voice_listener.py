from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_listener.py

import speech_recognition as sr
from cole_command_interpreter import cole_interpret_command
from assistants.malik import malik_report

# === Voice Listener ===
def start_voice_listener():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    malik_report("Voice Listener activated. Say 'Cole' followed by your command.", level="info")

    while True:
        try:
            with mic as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)

            # Recognize speech using Google Speech (or use Whisper if installed):
            command_text = recognizer.recognize_google(audio)
            command_text = command_text.strip()

            print(f"You said: {command_text}")
            malik_report(f"Voice command received: {command_text}")

            # Pass the command to Cole's interpreter
            response = cole_interpret_command(command_text)
            print(f"Cole: {response}")
            malik_report(f"Cole replied: {response}")

        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
        except KeyboardInterrupt:
            print("Voice Listener stopped by user.")
            break

# === CLI Direct Run ===
if __name__ == "__main__":
    start_voice_listener()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():