import time

# === TRY SELENIUM-WIRE FIRST ===
try:
    print(">> Trying Selenium Wire with ChromeDriver...")
    from seleniumwire import webdriver  # Replaces standard selenium.webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    print(">> Loading https://example.com")
    driver.get("https://example.com")
    print("✅ Title from example.com:", driver.title)

    time.sleep(2)

    print(">> Loading https://screeps.com")
    driver.get("https://screeps.com")
    print("✅ Screeps website loaded (headless mode)")

    print(">> Network traffic from Screeps.com:")
    for request in driver.requests:
        if request.response:
            print(f"{request.method} {request.url} - {request.response.status_code}")

    time.sleep(5)
    driver.quit()
    print("✅ Selenium-wire recon complete. Browser closed.")

# === FALLBACK TO UNDETECTED CHROMEDRIVER ===
except Exception as e:
    print(f"⚠️ Selenium-wire failed. Falling back to undetected-chromedriver...\nReason: {e}")

    try:
        import undetected_chromedriver as uc
        from undetected_chromedriver.options import ChromeOptions

        print(">> Starting undetected Chrome with binary path override...")
        opts = ChromeOptions()
        opts.binary_location = "/usr/bin/chromium-browser"  # or "/usr/bin/chromium" if needed
        opts.add_argument("--headless")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--disable-dev-shm-usage")

        driver = uc.Chrome(options=opts, headless=True)

        print(">> Loading https://example.com")
        driver.get("https://example.com")
        print("✅ Title from example.com:", driver.title)

        time.sleep(2)

        print(">> Loading https://screeps.com")
        driver.get("https://screeps.com")
        print("✅ Screeps website loaded successfully.")

        time.sleep(5)
        driver.quit()
        print("✅ UC recon complete. Browser closed.")
    except Exception as uc_error:
        print(f"❌ Fallback also failed. Error: {uc_error}")