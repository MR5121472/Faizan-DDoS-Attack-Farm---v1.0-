# proxies/proxy_handler.py
def load_proxies(file="proxies.txt"):
    with open(file, "r") as f:
        return [x.strip() for x in f.readlines()]
