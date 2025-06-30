from ghost_env import INFURA_KEY, VAULT_ADDRESS
from openai import OpenAI
client = OpenAI()

def generate_ai_code(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        code = response.choices[0].message.content
        print("[GPT] 🧠 Mutation complete.")
        return code
    except Exception as e:
        print(f"[GPT] ❌ Failed: {e}")
        return "# Failed to generate new code"

def log_event():ef drop_files_to_bridge():