from ghost_env import INFURA_KEY, VAULT_ADDRESS
# webpage_scraper.py – Scrapes title, text, and links from a webpage

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_page(url):
    print(f"[Scraper] 🕷️ Scraping: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"[Scraper] ❌ Error: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "No title found":
        text = soup.get_text(separator="\n", strip=True)
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

        print(f"[Scraper] ✅ Scraped {len(links)} links from: {url}")
        return {
            "url": url,
            "title": title,
            "text": text[:1000],  # Trim long pages
            "links": links
        }

    except Exception as e:
        print(f"[Scraper] ❌ Failed to scrape {url}: {e}")
        return None

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():