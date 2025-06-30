# ai_openai.py

import openai

class OpenAIResearch:
    def __init__(self, api_key):
        openai.api_key = api_key  # Corrected
        self.client = openai

    def get_summary(self, ticker):
        prompt = f"Summarize the current market outlook and news for {ticker} stock in three sentences."
        try:
            chat = self.client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a financial research assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.5
            )
            return chat.choices[0].message["content"].strip()
        except Exception as e:
            print(f"OpenAI error: {e}")
            return None

    def get_custom_explanation(self, prompt):
        try:
            chat = self.client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a financial research assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.5
            )
            return chat.choices[0].message["content"].strip()
        except Exception as e:
            print(f"OpenAI error: {e}")
            return None