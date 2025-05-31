=== FILE: voice_command_adapter.py ===

import json import re from webnav_loop import visit_url, fill_input_by_name, click_element_by_text

=== Voice Command Router ===

def handle_voice_command(command): print(f"[Voice Adapter] Received Command: {command}") command = command.lower().strip()

# Visit URL
visit_match = re.search(r"go to (https?://[\w./-]+)", command)
if visit_match:
    url = visit_match.group(1)
    visit_url(url)
    return f"Navigating to {url}"

# Search Google
search_match = re.search(r"search for (.+)", command)
if search_match:
    query = search_match.group(1)
    visit_url("https://www.google.com")
    fill_input_by_name("q", query)
    return f"Searching for {query}"

# Click Button by Text
click_match = re.search(r"click (.+)", command)
if click_match:
    text = click_match.group(1)
    click_element_by_text(text)
    return f"Clicked on {text}"

return "Command not recognized."

=== Testing Block ===

if name == "main": print("[Voice Adapter] Ready for test input.") while True: cmd = input("Speak > ") if cmd.lower() in ["exit", "quit"]: break response = handle_voice_command(cmd) print(response)

