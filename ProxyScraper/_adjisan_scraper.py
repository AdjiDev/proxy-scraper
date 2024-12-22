import requests
from concurrent.futures import ThreadPoolExecutor
from typing import List
from ._ProxyList import AllProxyUrl, HttpProxy, HttpsProxy, Socks4Proxy, Socks5Proxy

class GetProxy:
    def __init__(self, type: str = 'all', timeout: int = 10, max_workers: int = 10):
        """
        Initializes the GetProxy class.

        :param type: Proxy type to fetch ('http', 'https', 'socks4', 'socks5', 'all')
        :param timeout: Timeout in seconds for HTTP requests
        :param max_workers: Maximum number of threads for fetching proxies
        """
        self.type = type.lower()
        self.timeout = timeout
        self.max_workers = max_workers
        self.proxies = []

        self.proxy_sources = {
            'all': AllProxyUrl,
            'http': HttpProxy,
            'https': HttpsProxy,
            'socks4': Socks4Proxy,
            'socks5': Socks5Proxy
        }

    def fetch(self, url: str) -> List[str]:
        try:
            response = requests.get(url, timeout=self.timeout)
            if response.status_code == 200:
                proxies = response.text.splitlines()
                return proxies
        except requests.RequestException as e:
            print(f"Failed to fetch from {url}: {e}")
        return []

    def get(self) -> List[str]:
        urls = self.proxy_sources.get(self.type, AllProxyUrl)

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = executor.map(self.fetch, urls)

        self.proxies = list(set(proxy for result in results for proxy in result))
        return self.proxies

    def save(self, filename: str = "proxies.txt"):
        """
        Save the fetched proxies to a file.
        """
        if not self.proxies:
            print("No proxies to save. Fetch proxies first.")
            return

        with open(filename, "w") as file:
            file.write("\n".join(self.proxies))
        print(f"Proxies saved to {filename}")


