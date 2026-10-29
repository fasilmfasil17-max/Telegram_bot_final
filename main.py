import os, random, threading
import telebot
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

PHOTOS = [
 "https://picsum.photos/800/600?random=1",
 "https://picsum.photos/800/600?random=2",
 "https://picsum.photos/800/600?random=3"
]

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "Bot Online hai Fahad Boss /pic likho")

@bot.message_handler(commands=['pic'])
def pic(m):
    bot.send_photo(m.chat.id, random.choice(PHOTOS))

@app.route('/')
def home():
    return "Bot is Running!"

def run_bot():
    print("Bot starting...")
    bot.infinity_polling(skip_pending=True)

threading.Thread(target=run_bot).start()
