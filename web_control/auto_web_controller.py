# === FILE: web_control/auto_web_controller.py ===

import threading
from web_control.selenium_navigator import open_page, search_google, click_element_by_text, close_browser

# === Web Task Runner ===
class WebController:
    def __init__(self):
        self.browser = None

    def go_to_url(self, url):
        if self.browser:
            close_browser(self.browser)
        self.browser = open_page(url)

    def run_google_search(self, query):
        if self.browser:
            close_browser(self.browser)
        self.browser = search_google(query)

    def click_link(self, link_text):
        if not self.browser:
            print("[WebController] No browser session active.")
            return
        click_element_by_text(self.browser, link_text)

    def shutdown(self):
        if self.browser:
            close_browser(self.browser)
            self.browser = None

# === Voice or AI Trigger ===
def execute_web_command(command_type, payload):
    controller = WebController()

    def task():
        if command_type == "visit":
            controller.go_to_url(payload)
        elif command_type == "search":
            controller.run_google_search(payload)
        elif command_type == "click":
            controller.click_link(payload)
        elif command_type == "shutdown":
            controller.shutdown()
        else:
            print(f"[WebController] Unknown command: {command_type}")

    thread = threading.Thread(target=task)
    thread.start()

# === Example ===
if __name__ == "__main__":
    # Sample test
    execute_web_command("search", "PTM Screeps bot setup")