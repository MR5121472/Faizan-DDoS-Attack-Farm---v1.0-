# proxies/tor_rotator.py
import os

def rotate_ip():
    os.system("service tor reload")
    print("[+] Tor IP rotated.")
