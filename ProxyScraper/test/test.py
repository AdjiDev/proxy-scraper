from ProxyScraper import GetProxy

if __name__ == "__main__":
    #Init
    proxy = GetProxy(type="http", timeout=5, max_workers=20)

    #get
    proxies = proxy.get()
    print(f"Fetched {len(proxies)} proxies.")

    #save
    proxy.save("http.txt")