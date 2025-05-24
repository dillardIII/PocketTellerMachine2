# brain/ai_selector.py

import openai

# Later you can switch models like Claude, Perplexity, etc.
DEFAULT_MODEL = "gpt-4"

def get_ai_response(prompt):
    """
    Sends the prompt to OpenAI and returns a response.
    You can later upgrade this to route to Claude, Perplexity, or custom models.
    """

    try:
        response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": "You are a smart trading assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=200
        )
        return response['choices'][0]['message']['content']

    except Exception as e:
        return f"[AI ERROR] {str(e)}"