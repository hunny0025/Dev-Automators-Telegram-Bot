import os
import time
import threading
import random
import requests
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("7588095044:AAEOLaldcxU8-hen5QTFp8iKuVuuvqKMGUo")
BASE_URL = "https://api.telegram.org/bot" + "7588095044:AAEOLaldcxU8-hen5QTFp8iKuVuuvqKMGUo/"



greetings = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Salutations!",
    "Howdy!"
]

questions = [
    {"question": "What comes next in the sequence? 2, 4, 8, 16, ...", "answer": "32"},
    {"question": "Which word doesn’t belong? Apple, Banana, Carrot, Mango", "answer": "Carrot"},
    {"question": "What is 15 + 28?", "answer": "43"}
]

user_scores = {}
user_progress = {}

def get_updates(offset=None):
    url = BASE_URL + "getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params).json()
    return response

def send_message(chat_id, text):
    url = BASE_URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

def ask_question(chat_id, user_id):
    index = user_progress.get(user_id, 0)
    if index < len(questions):
        send_message(chat_id, questions[index]['question'])
    else:
        score = user_scores.get(user_id, 0)
        send_message(chat_id, f"✅ Test completed! Your score: {score}/{len(questions)} 🎉")

def handle_answer(chat_id, user_id, text):
    index = user_progress.get(user_id, 0)
    if index < len(questions):
        correct_answer = questions[index]['answer']
        if text.lower() == correct_answer.lower():
            user_scores[user_id] = user_scores.get(user_id, 0) + 1
            send_message(chat_id, "✅ Correct!")
        else:
            send_message(chat_id, f"❌ Incorrect. The right answer was: {correct_answer}")
        user_progress[user_id] = index + 1
        ask_question(chat_id, user_id)

def main():
    update_id = None
    print("Bot started...")
    while True:
        updates = get_updates(offset=update_id)
        for update in updates.get("result", []):
            update_id = update["update_id"] + 1
            message = update.get("message")
            chat_id = message.get("chat", {}).get("id", None)
            text = message.get("text", "").strip().lower()
            user_id = chat_id

            if text == "/start":
                greeting = random.choice(greetings)
                user_progress[user_id] = 0
                user_scores[user_id] = 0
                send_message(chat_id, greeting + " Let's begin the IQ test!")
                ask_question(chat_id, user_id)
            elif text == "/joke":
                joke = get_joke()
                send_message(chat_id, joke)
            else:
                handle_answer(chat_id, user_id, text)

        time.sleep(0.5)


if __name__ == "__main__":
    polling_thread = threading.Thread(target=main)
    polling_thread.start()
