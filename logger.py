from datetime import datetime
from config import LOG_FILE
import os

os.makedirs('outputs/logs', exist_ok=True)

def log_message(msg):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now()}] {msg}\n")
