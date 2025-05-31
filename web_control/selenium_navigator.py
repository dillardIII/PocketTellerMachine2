# === FILE: web_control/selenium_navigator.py ===

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# === Setup Chrome Driver ===
def start_browser(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Replace this with your actual path to chromedriver
    service = Service(executable_path="chromedriver.exe")
    browser = webdriver.Chrome(service=service, options=chrome_options)
    return browser

# === Load and Navigate to URL ===
def open_page(url):
    browser = start_browser(headless=False)
    print(f"[SeleniumNav] Opening: {url}")
    browser.get(url)
    return browser

# === Perform Search ===
def search_google(query):
    browser = open_page("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.submit()
    print(f"[SeleniumNav] Searched: {query}")
    time.sleep(3)
    return browser

# === Click Element by Text ===
def click_element_by_text(browser, text):
    try:
        element = browser.find_element(By.LINK_TEXT, text)
        element.click()
        print(f"[SeleniumNav] Clicked element with text: {text}")
    except Exception as e:
        print(f"[SeleniumNav] Error clicking element: {e}")

# === Close Browser ===
def close_browser(browser):
    browser.quit()
    print("[SeleniumNav] Browser closed.")