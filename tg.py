import os, json

from dotenv import load_dotenv
import telebot
import webbrowser
from telebot import types

load_dotenv()
bot = telebot.TeleBot(os.getenv('TG_ID'))

tg_key = os.getenv("TG_KEY")
@bot.message_handler(commands=[tg_key])
def get_chat_id(message):
    with open(os.getenv("TG_HELLO_MESSAGE"), "r", encoding="utf-8") as file:
        text_message = file.read()
    bot.send_message(message.chat.id, text=text_message.format(name=message.from_user.first_name))

    with open(os.getenv("TG_CHAT_IDS"), "r", encoding="utf-8") as file:
        chatids = json.load(file)
    if message.chat.id not in chatids:
        chatids.append(message.chat.id)
    with open(os.getenv("TG_CHAT_IDS"), "w", encoding="utf-8") as file:
        chatids = json.dump(chatids, file, indent=4, ensure_ascii=False)

# TODO: main func for sending entry
# TODO: fix first message
# TODO: fix json chatids
# TODO: fix front message and show format of TG_KEY

def main():
    bot.infinity_polling()

if __name__ == "__main__":
    main()