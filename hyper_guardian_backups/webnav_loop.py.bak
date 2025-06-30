# === FILE: webnav_loop.py ===

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# === Setup Chrome WebDriver options ===
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start the browser
driver = webdriver.Chrome(options=chrome_options)

# === Modular Functions ===

def visit_url(url):
    print(f"[PTM WebNav] Visiting: {url}")
    driver.get(url)
    time.sleep(2)

def click_element_by_text(text):
    try:
        print(f"[PTM WebNav] Looking for element with text: {text}")
        elem = driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
        elem.click()
        print(f"[PTM WebNav] Clicked on: {text}")
        time.sleep(2)
    except Exception as e:
        print(f"[PTM WebNav] Error clicking element: {e}")

def fill_input_by_name(name, input_text):
    try:
        print(f"[PTM WebNav] Typing into input with name: {name}")
        input_field = driver.find_element(By.NAME, name)
        input_field.clear()
        input_field.send_keys(input_text)
        input_field.send_keys(Keys.RETURN)
        time.sleep(2)
    except Exception as e:
        print(f"[PTM WebNav] Error typing input: {e}")

def shutdown_browser():
    print("[PTM WebNav] Closing browser.")
    driver.quit()

# === Combined Example Usage ===

def run_webnav():
    visit_url("https://www.google.com")
    fill_input_by_name("q", "PTM Web Control Test")
    click_element_by_text("PTM")
    shutdown_browser()

if __name__ == "__main__":
    run_webnav()