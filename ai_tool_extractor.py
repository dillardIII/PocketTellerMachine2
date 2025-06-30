from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ai_tool_extractor.py – Extracts AI tool mentions from scraped content

import re

KNOWN_AI_KEYWORDS = [
    "ChatGPT", "Claude", "Bard", "LLaMA", "Whisper", "ElevenLabs", "MidJourney", "DALL·E",
    "OpenAI", "Hugging Face", "LangChain", "AgentGPT", "AutoGPT", "Stability AI",
    "Runway", "Perplexity", "Replit", "Copilot", "DeepL", "Notion AI", "Cohere",
    "Anthropic", "OpenAssistant", "Forefront", "Character AI", "Gamma AI", "Tome AI",
    "Synthesia", "Soundraw", "Descript", "AssemblyAI", "Pinecone", "Vector DB",
    "Nvidia AI", "Google AI", "Microsoft Copilot", "Meta AI", "Stability SDK", "Jan AI"
]

def extract_ai_tools(text):
    print("[AI Extractor] 🧠 Scanning for known AI tools...")
    found = []
    for tool in KNOWN_AI_KEYWORDS:
        if re.search(rf"\b{re.escape(tool)}\b", text, re.IGNORECASE):
            found.append(tool)
    print(f"[AI Extractor] ✅ Found {len(found)} tools: {found}")
    return found

def log_event():ef drop_files_to_bridge():