import puppeteer from 'puppeteer';  // Make sure to install with: npm install puppeteer

const browser = await puppeteer.launch({
  headless: "new",
  executablePath: puppeteer.executablePath(),
  args: [
    '--no-sandbox',
    '--disable-setuid-sandbox',
    '--disable-dev-shm-usage',
    '--disable-accelerated-2d-canvas',
    '--no-first-run',
    '--no-zygote',
    '--single-process',
    '--disable-gpu'
  ]
});

const page = await browser.newPage();
await page.goto('https://example.com');

console.log(await page.title());

await browser.close();