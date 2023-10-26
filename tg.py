import os, json
from time import sleep
import asyncio
from datetime import datetime

from dotenv import load_dotenv
import telebot
import webbrowser
from telebot import types
from telebot.async_telebot import AsyncTeleBot

from utils import *


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


def send_message(city:str, visa_center:str, time=get_current_time(), entry=False) -> None:
    bot = telebot.TeleBot(token=os.getenv('TG_ID'))
    with open(os.getenv("TG_MESS_ENTRY_SUCCESS"), "r", encoding="utf-8") as file:
        message_success = file.read().format(city=city, visa_center=visa_center, datetime=time)
    with open(os.getenv("TG_MESS_ENTRY_FAIL"), "r", encoding="utf-8") as file:
        message_fail = file.read().format(city=city, visa_center=visa_center, datetime=time)
    text = message_success if entry else message_fail
    with open(os.getenv("TG_CHAT_IDS"), "r", encoding="utf-8") as file:
        chatids = json.load(file)
    for chat_id, username in chatids.items():
        bot.send_message(int(chat_id), text=text)

def send_mess_text(path_to_message:str) -> None:
    with open(path_to_message, "r", encoding="utf-8") as file:
        text = file.read()
    with open(os.getenv("TG_CHAT_IDS"), "r", encoding="utf-8") as file:
        chatids = json.load(file)
    for chat_id, username in chatids.items():
        bot.send_message(int(chat_id), text=text)


@bot.message_handler(commands=['chat'])
def get_chat(message):
    bot.reply_to(message, message.chat)


# TODO: fix front message and show format of TG_KEY

def main():
    send_message(city="Minsk", visa_center="Visa Center Mins")


if __name__ == "__main__":
    main()