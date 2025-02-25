import os
import time
import threading
import requests
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("7588095044:AAEOLaldcxU8-hen5QTFp8iKuVuuvqKMGUo")
BASE_URL = f"https://api.telegram.org/bot{"7588095044:AAEOLaldcxU8-hen5QTFp8iKuVuuvqKMGUo"}/"

def get_updates(offset=None):
    response = requests.get(BASE_URL + "getUpdates", params={"timeout": 100, "offset": offset}).json()
    return response

def send_message(chat_id, text):
    requests.post(BASE_URL + "sendMessage", data={"chat_id": chat_id, "text": text})

def get_exchange_rate(text):
    parts = text.replace("/rate", "").strip().upper().split()
    if len(parts) == 2:
        base, target = parts
        url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"
        response = requests.get(url)
        if response.status_code == 200:
            rates = response.json().get('rates', {})
            rate = rates.get(target)
            if rate:
                return f"💱 1 {base} = {rate} {target}"
            else:
                return "⚡ Invalid currency codes. Example: /rate USD INR"
    return "⚡ Usage: /rate USD INR"

def main():
    update_id = None
    print("🤖 Bot started...")
    while True:
        updates = get_updates(offset=update_id)
        for update in updates.get("result", []):
            update_id = update["update_id"] + 1
            chat_id = update.get("message", {}).get("chat", {}).get("id")
            text = update.get("message", {}).get("text", "").strip().lower()
            if text.startswith("/start"):
                send_message(chat_id, "👋 Welcome! Just type: /rate USD INR to get real-time rates.")
            elif text.startswith("/rate"):
                send_message(chat_id, get_exchange_rate(text))
            else:
                send_message(chat_id, "⚠️ Unknown command. Use: /rate USD INR")
        time.sleep(0.5)

if __name__ == "__main__":
    threading.Thread(target=main).start()