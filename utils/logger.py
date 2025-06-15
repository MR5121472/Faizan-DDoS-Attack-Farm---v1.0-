# utils/logger.py
from datetime import datetime

def log_event(event):
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] {event}\n")
