import os, json
from time import sleep
import asyncio

from dotenv import load_dotenv
import telebot
import webbrowser
from telebot import types
from telebot.async_telebot import AsyncTeleBot


load_dotenv()
bot = telebot.TeleBot(token=os.getenv('TG_ID'))

tg_key = os.getenv("TG_KEY")
@bot.message_handler(commands=[tg_key])
def get_chat_id(message):
    with open(os.getenv("TG_HELLO_MESSAGE"), "r", encoding="utf-8") as file:
        hello_message = file.read()
    with open(os.getenv("TG_REPIT_HELLO_MESSAGE"), "r", encoding="utf-8") as file:
        repit_hello_message = file.read()  
    with open(os.getenv("TG_CHAT_IDS"), "r", encoding="utf-8") as file:
        chatids = json.load(file)
    text_message = repit_hello_message if str(message.chat.id) in chatids else hello_message
    bot.send_message(message.chat.id, text=text_message.format(name=message.from_user.first_name))
    
    if str(message.chat.id) not in chatids:
        chatids[str(message.chat.id)] = message.chat.username
    with open(os.getenv("TG_CHAT_IDS"), "w", encoding="utf-8") as file:
        chatids = json.dump(chatids, file, indent=4, ensure_ascii=False)

def send_message():
    with open(os.getenv("TG_CHAT_IDS"), "r", encoding="utf-8") as file:
        chatids = json.load(file)
    for chat_id, username in chatids.items():
        print(chat_id)
        bot.send_message(int(chat_id), text="Проверка отправки сообщения")


@bot.message_handler(commands=['chat'])
def get_chat(message):
    bot.reply_to(message, message.chat)


# TODO: main func for sending entry
# TODO: fix first message
# TODO: fix json chatids
# TODO: fix front message and show format of TG_KEY

def main():
    with open(os.getenv("TG_CHAT_IDS"), "r", encoding="utf-8") as file:
        chatids = json.load(file)
    for chat_id, username in chatids.items():
        bot.send_message(int(chat_id), text="Проверка отправки сообщения")
    # bot.infinity_polling()


if __name__ == "__main__":
    main()