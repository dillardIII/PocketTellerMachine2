from ghost_env import INFURA_KEY, VAULT_ADDRESS
# site_map_discovery.py – Discovers all available links on a target webpage for deep crawling

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def discover_links(url):
    print(f"[SiteMap] 🌐 Discovering links on: {url}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"[SiteMap] ❌ Failed to fetch {url}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        base_url = response.url
        links = set()

        for anchor in soup.find_all('a', href=True):
            full_url = urljoin(base_url, anchor['href'])
            links.add(full_url)

        print(f"[SiteMap] ✅ Found {len(links)} links.")
        return list(links)

    except Exception as e:
        print(f"[SiteMap] ❌ Error during link discovery: {e}")
        return []

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():