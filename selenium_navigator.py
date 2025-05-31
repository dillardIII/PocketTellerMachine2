from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def open_browser_and_visit(url):
    options = Options()
    options.add_argument("--headless")  # Runs browser in background
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    print(f"[PTM Selenium] Navigated to {url}")
    return driver

def click_element_by_text(driver, text):
    try:
        element = driver.find_element(By.LINK_TEXT, text)
        element.click()
        print(f"[PTM Selenium] Clicked element with text: {text}")
    except Exception as e:
        print(f"[PTM Selenium] Error clicking: {e}")