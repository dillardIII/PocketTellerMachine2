from ghost_env import INFURA_KEY, VAULT_ADDRESS
# multilingual_switcher.py
# Enables dynamic language switching across all bot responses

from langdetect import detect
from googletrans import Translator

class MultilingualSwitcher:
    def __init__(self, default_language="en"):
        self.default_language = default_language
        self.translator = Translator()

    def detect_language(self, text):
        try:
            return detect(text)
        except Exception as e:
            print(f"[ERROR] Language detection failed: {e}")
            return self.default_language

    def translate_to_user(self, text, user_lang=None):
        if not user_lang:
            user_lang = self.default_language
        try:
            if detect(text) == user_lang:
                return text
            translated = self.translator.translate(text, dest=user_lang)
            return translated.text
        except Exception as e:
            return f"[ERROR] Translation failed: {e}"

    def translate_from_user(self, text):
        try:
            lang = detect(text)
            if lang != self.default_language:
                return self.translator.translate(text, dest=self.default_language).text
            return text
        except Exception as e:
            return f"[ERROR] Input translation failed: {e}"

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():