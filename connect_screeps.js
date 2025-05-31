const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
    args: ['--start-maximized']
  });

  const page = await browser.newPage();
  await page.goto('https://screeps.com/a/#!/sim');

  console.log('🖤 Shadow entering Screeps simulation...');
  await page.waitForTimeout(15000); // Wait for simulation to load

  // Shadow's stealth creep spawn script
  const shadowScript = `Game.spawns['Spawn1'].spawnCreep([MOVE, MOVE, CARRY], 'Shadow_' + Game.time, { memory: { role: 'shadow' } });`;

  await page.keyboard.press('Escape');
  await page.keyboard.down('Control');
  await page.keyboard.press('`'); // Toggle console
  await page.keyboard.up('Control');
  await page.waitForTimeout(1000);

  for (const char of shadowScript) {
    await page.keyboard.press(char);
  }
  await page.keyboard.press('Enter');

  console.log('✅ Shadow deployed to Screeps.');
})();