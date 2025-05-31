// === FILE: recon_puppeteer_agent.js ===

const puppeteer = require("puppeteer");

(async () => {
  const HEADLESS_MODE = false; // Toggle true for headless (invisible) mode

  console.log("🛰️ Launching Cole + Shadow via Puppeteer...");

  const launchOptions = HEADLESS_MODE
    ? {
        headless: true,
        args: [
          "--no-sandbox",
          "--disable-setuid-sandbox",
          "--disable-dev-shm-usage",
          "--disable-gpu"
        ]
      }
    : {
        headless: false,
        defaultViewport: null,
        args: ["--start-maximized"]
      };

  try {
    const browser = await puppeteer.launch(launchOptions);
    const page = await browser.newPage();

    const targetUrl = HEADLESS_MODE
      ? "https://screeps.com/a/#!/sim"
      : "https://screeps.com/a/";

    await page.goto(targetUrl, { waitUntil: "domcontentloaded" });

    if (HEADLESS_MODE) {
      console.log("✅ Screeps simulation loaded (headless mode).");
    } else {
      console.log("📸 Taking screenshot...");
      await page.screenshot({ path: "screeps_recon_proof.png" });
      console.log("🕒 Waiting 10 seconds for visual confirmation...");
      await page.waitForTimeout(10000);
      console.log("✅ Recon mission complete. Browser closed.");
    }

    await browser.close();
  } catch (error) {
    console.error("❌ Puppeteer failed to launch or complete:", error.message);
  }
})();