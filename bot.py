import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

WELCOME_TEXT = (
    "Добро пожаловать в OplataRublem 💳\n\n"
    "Укажите, пожалуйста, с чем именно Вам нужна помощь"
)

CAT_URL = "https://i.imgur.com/placeholder.jpg"

@bot.message_handler(commands=["start"])
def start(message):
    try:
        with open("cat.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption=WELCOME_TEXT)
    except:
        bot.send_message(message.chat.id, WELCOME_TEXT)

@bot.message_handler(func=lambda m: True)
def handle(message):
    bot.send_message(
        message.chat.id,
        "Укажите, пожалуйста, с чем именно Вам нужна помощь"
    )

print("Бот запущен...")
bot.infinity_polling()
