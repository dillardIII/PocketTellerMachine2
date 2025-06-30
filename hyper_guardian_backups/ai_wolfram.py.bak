import requests

class WolframResearch:
    def __init__(self, app_id):
        self.app_id = app_id

    def query(self, question):
        url = "https://api.wolframalpha.com/v1/result"
        params = {"i": question, "appid": self.app_id}
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(f"Wolfram error: {e}")
            return None