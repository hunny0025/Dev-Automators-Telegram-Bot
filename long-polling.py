import os
import time
import threading
import random
import requests
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

greetings = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Salutations!",
    "Howdy!"
]

def get_updates(offset=None):
    url = BASE_URL + "getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params).json()
    return response

def send_message(chat_id, text):
    url = BASE_URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

def main():
    update_id = None
    print("Bot started...")
    while True:
        updates = get_updates(offset=update_id)
        for update in updates.get("result", []):
            update_id = update["update_id"] + 1
            message = update.get("message")
            chat_id = message.get("chat", {}).get("id", None)

            # Add your command in this block by using elif
            if message and message.get("text", "").strip() == "/start":
                greeting = random.choice(greetings)
                send_message(chat_id, greeting)
            else:
                send_message(chat_id, "Invalid message")

        time.sleep(0.5)

if __name__ == "__main__":
    polling_thread = threading.Thread(target=main)
    polling_thread.start()
