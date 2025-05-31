# === FILE: selenium_test.py ===

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# === Setup Chrome options ===
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# === Launch WebDriver with correct Service structure ===
print("🚀 Launching headless Chrome via WebDriverManager...")

driver = None

try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://screeps.com/a/#!/sim")
    print("🛰️ Navigated to Screeps Simulation.")

    time.sleep(15)

    try:
        sim_button = driver.find_element(By.CSS_SELECTOR, "button.sim-button")
        sim_button.click()
        print("✅ Simulation start button clicked.")
    except Exception as e:
        print("⚠️ Could not click sim button:", str(e))

    time.sleep(10)

except Exception as e:
    print("❌ Selenium error:", str(e))

finally:
    if driver:
        driver.quit()
        print("✅ Test complete. Browser closed.")
    else:
        print("⚠️ Skipped driver.quit() — driver never launched.")