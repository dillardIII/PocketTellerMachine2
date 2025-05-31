// === FILE: recon_firefox_agent.js ===

const puppeteer = require("puppeteer");

(async () => {
  console.log("🛰️ Launching ReconBot via Puppeteer with Firefox...");

  const browser = await puppeteer.launch({
    product: "firefox",
    headless: true, // Set to false to visually see it (on desktop, not server)
    args: [
      "--no-sandbox",
      "--disable-setuid-sandbox",
      "--disable-dev-shm-usage"
    ]
  });

  const page = await browser.newPage();
  await page.goto("https://screeps.com/a/", { waitUntil: "domcontentloaded" });

  console.log("📸 Taking screenshot...");
  await page.screenshot({ path: "screeps_firefox_recon.png" });

  console.log("🕒 Waiting 5 seconds before closing...");
  await page.waitForTimeout(5000);

  await browser.close();
  console.log("✅ Recon complete. Browser closed.");
})();