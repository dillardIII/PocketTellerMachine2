from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: selenium_click_engine.py ===

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def init_browser(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def open_page(driver, url):
    try:
        driver.get(url)
        print(f"[PTM Click Engine] Opened page: {url}")
    except Exception as e:
        print(f"[PTM Click Engine] Failed to open page: {e}")

def click_element(driver, selector, by=By.CSS_SELECTOR):
    try:
        element = driver.find_element(by, selector)
        element.click()
        print(f"[PTM Click Engine] Clicked: {selector}")
    except Exception as e:
        print(f"[PTM Click Engine] Click failed: {e}")

def type_into_field(driver, selector, text, by=By.CSS_SELECTOR):
    try:
        element = driver.find_element(by, selector)
        element.clear()
        element.send_keys(text)
        print(f"[PTM Click Engine] Typed '{text}' into {selector}")
    except Exception as e:
        print(f"[PTM Click Engine] Typing failed: {e}")

def close_browser(driver):
    driver.quit()
    print("[PTM Click Engine] Browser closed.")

def log_event():ef drop_files_to_bridge():