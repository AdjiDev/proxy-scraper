import subprocess
try:
    from ProxyScraper import GetProxy
except ImportError:
    subprocess.run(
        ["pip", "install", "ProxyScraper"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
    from ProxyScraper import GetProxy
import sys
import os
import time

reset = '\033[0m'

bl = '\033[30m'
rd = '\033[31m'
gr = '\033[32m'
yell = '\033[33m'
blu = '\033[34m'
mag = '\033[35m'
cy = '\033[36m'
wh = '\033[37m'

def Ngetik(teks, delay=0.0015):
    for i in teks:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def RgbToAnsi(r, g, b):
    if r == g == b:
        return 232 + (r // 10)  
    else:
        return 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)

def RGB_BANNER(banner: str, st=(0, 0, 0), end=(255, 255, 255)):
    len_banner = len(banner)
    r_diff = (end[0] - st[0]) / len_banner
    g_diff = (end[1] - st[1]) / len_banner
    b_diff = (end[2] - st[2]) / len_banner

    result = ""
    
    for i, char in enumerate(banner):
        r = int(st[0] + r_diff * i)
        g = int(st[1] + g_diff * i)
        b = int(st[2] + b_diff * i)
        
        ansi_code = RgbToAnsi(r, g, b)
        
        result += f"\033[38;5;{ansi_code}m{char}\033[0m"
    
    return result

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#main section
def Wizard():
    cls()
    BANNER = """
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗     ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝     ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝█████╗███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝ ╚════╝╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║        ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝\n"""
    print(RGB_BANNER(BANNER, st=(238, 130, 238), end=(255, 255, 0)))
    Ngetik(f'{gr}LICENSE     {reset}: MIT')
    Ngetik(f'{gr}DEVELOPER   {reset}: adjidev')
    Ngetik(f'============================================ {gr}PROXY SCRAPER{reset} ============================================')
    Ngetik(f'[1] {yell}GET ALL PROXIES{reset}')
    Ngetik(f'[2] {yell}GET HTTP PROXY{reset}')
    Ngetik(f'[3] {yell}GET HTTPS PROXY{reset}')
    Ngetik(f'[4] {yell}GET SOCKS4 PROXY{reset}')
    Ngetik(f'[5] {yell}GET SOCKS5 PROXY{reset}')
    Ngetik(f'[6] {rd}EXIT{reset}')
    while True:
        try:
            a = input(f'\n\nroot@{rd}adjidev_#{reset} ')
            if a == '1':
                b = GetProxy(type="all", timeout=5, max_workers=20)
                proxy = b.get()
                print(f'Fetched all {gr}{len(proxy)}{reset} proxies')
                b.save('src/all.txt')

            elif a == '2':
                b = GetProxy(type="http", timeout=5, max_workers=20)
                proxy = b.get()
                print(f'Fetched all http {gr}{len(proxy)}{reset} proxies')
                b.save('src/http.txt')

            elif a == '3':
                b = GetProxy(type="https", timeout=5, max_workers=20)
                proxy = b.get()
                print(f'Fetched all https {gr}{len(proxy)}{reset} proxies')
                b.save('src/https.txt')
            
            elif a == '4':
                b = GetProxy(type="socks4", timeout=5, max_workers=20)
                proxy = b.get()
                print(f'Fetched all socks4 {gr}{len(proxy)}{reset} proxies')
                b.save('src/socks4.txt')

            elif a == '5':
                b = GetProxy(type="socks5", timeout=5, max_workers=20)
                proxy = b.get()
                print(f'Fetched all socks5 {gr}{len(proxy)}{reset} proxies')
                b.save('src/socks5.txt')

            elif a == '6':
                print('\nEXIT')
                sys.exit(1)

        except KeyboardInterrupt:
            print('\nEXIT!')
            sys.exit(1)

if __name__ == "__main__":
    Wizard()