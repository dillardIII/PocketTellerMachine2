const { chromium } = require('playwright');
require('dotenv').config();

(async () => {
  const browser = await chromium.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-gpu']
  });

  const page = await browser.newPage();

  const username = process.env.SCREEPS_USERNAME;
  const password = process.env.SCREEPS_PASSWORD;

  if (!username || !password) {
    console.error("❌ Missing SCREEPS_USERNAME or SCREEPS_PASSWORD");
    process.exit(1);
  }

  try {
    await page.goto("https://screeps.com/a/#/auth/signin", { waitUntil: 'networkidle' });

    await page.waitForSelector("input[name='username']", { timeout: 5000 });
    await page.fill("input[name='username']", username);
    await page.fill("input[name='password']", password);

    await page.click("button[type='submit']");
    await page.waitForTimeout(5000);

    await page.screenshot({ path: "screeps_login_success.png" });
    console.log("✅ Playwright: Screeps login complete. Screenshot saved.");
  } catch (err) {
    console.error("❌ Login script failed:", err);
    await page.screenshot({ path: "screeps_login_failed.png" });
  }

  await browser.close();
})();