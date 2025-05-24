# cole_tools/gpt_advisor.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt, model="gpt-4", temperature=0.7):
    print("[GPT Advisor] Prompting GPT with:", prompt)
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=600
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("[GPT Advisor] Error:", e)
        return f"GPT Error: {str(e)}"