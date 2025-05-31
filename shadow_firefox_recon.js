const { firefox } = require('playwright');

(async () => {
  console.log('🛰️ Launching Shadow via Firefox...');

  const browser = await firefox.launch({
    headless: false, // Runs in visible window
    slowMo: 500,      // Slows actions down for visual tracking
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://screeps.com/a/#!/sim');

  console.log('✅ Shadow has entered the simulation zone.');

  await page.waitForTimeout(30000); // Keep browser open for 30 seconds

  // Optional: Comment this line to keep it open forever
  await browser.close();
})();