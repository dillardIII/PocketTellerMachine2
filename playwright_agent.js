// playwright_agent.js

const { chromium } = require('playwright'); // Ensure installed via: npx playwright install
const fs = require('fs');
const path = require('path');

(async () => {
  console.log("[PLAYWRIGHT AGENT] Starting Screeps recon...");

  const screenshotDir = "screenshots";
  const screenshotPath = path.join(screenshotDir, "dashboard_capture.png");

  if (!fs.existsSync(screenshotDir)) {
    fs.mkdirSync(screenshotDir);
  }

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  try {
    await page.goto('https://screeps.com/a/', { timeout: 20000 });
    console.log("[PLAYWRIGHT AGENT] Page loaded.");

    // Grab login envs (injected into Node env at runtime)
    const email = process.env.SCREEPS_EMAIL;
    const password = process.env.SCREEPS_PASSWORD;

    await page.fill('input[name="username"]', email);
    await page.fill('input[name="password"]', password);
    await page.press('input[name="password"]', 'Enter');

    console.log("[PLAYWRIGHT AGENT] Login submitted. Waiting...");
    await page.waitForTimeout(5000);

    await page.screenshot({ path: screenshotPath });
    console.log("[PLAYWRIGHT AGENT] Screenshot saved:", screenshotPath);

    console.log(JSON.stringify({
      status: "success",
      tool_used: "playwright",
      screenshot: screenshotPath,
      message: "Login successful, dashboard captured"
    }));

  } catch (error) {
    console.error("[PLAYWRIGHT AGENT ERROR]", error.message);
    console.log(JSON.stringify({
      status: "fail",
      tool_used: "playwright",
      message: error.message
    }));
  } finally {
    await browser.close();
  }
})();