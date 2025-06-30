from ghost_env import INFURA_KEY, VAULT_ADDRESS
import speech_recognition as sr
from cole_command_interpreter import cole_interpret_command

def listen_and_execute():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("[Voice] Listening... Speak your command.")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"[Voice Command] You said: {command}")
        reply = cole_interpret_command(command)
        print(f"[Cole]: {reply}")
    except sr.UnknownValueError:
        print("[Voice Error] Could not understand audio.")
    except sr.RequestError as e:
        print(f"[Voice Error] API unavailable: {e}")

if __name__ == "__main__":
    while True:
        listen_and_execute()

def log_event():ef drop_files_to_bridge():