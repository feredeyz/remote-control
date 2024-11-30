import os
import pyautogui as pg
from telebot import *
from datetime import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def greet():
    day_part = ''
    hour = datetime.now().hour
    if 0 <= hour <= 12:
        day_part = 'утро'
    elif 13 <= hour <= 16:
        day_part = 'день'
    elif 17 <= hour <= 22:
        day_part = 'вечер'
    else:
        day_part = "ночь"
    return f"Добрый {day_part}! Выберите команду:"

commands_buttons = [
    InlineKeyboardButton('Скриншот', callback_data='screenshot'),
    InlineKeyboardButton('Свернуть все окна', callback_data='windows'),
    InlineKeyboardButton('Выключить', callback_data='shutdown'),
    InlineKeyboardButton('Перезагрузка', callback_data='reboot'),
    InlineKeyboardButton('Сменить язык', callback_data='language'),
    InlineKeyboardButton('Начать запись экрана', callback_data='video_start'),
    InlineKeyboardButton('Остановить запись экрана', callback_data='video_end'),
    InlineKeyboardButton('Открыть программу', callback_data='app'),
]

def commands():
    command = InlineKeyboardMarkup()
    for button in commands_buttons:
        command.add(button)
    return command


apps_buttons = [
    InlineKeyboardButton('Firefox', callback_data='firefox'),
    InlineKeyboardButton('Discord', callback_data='discord'),
    InlineKeyboardButton('VSCode', callback_data='vscode'),
    InlineKeyboardButton('Telegram', callback_data='telegram'),
    InlineKeyboardButton('Проводник', callback_data='explorer'),
    InlineKeyboardButton('Dota 2', callback_data='dota')
]

def apps():
    app = InlineKeyboardMarkup()
    for button in apps_buttons:
        app.add(button)
    return app
    

token = ''
bot = TeleBot(token)
host = 0

@bot.message_handler(commands=['start'], func=lambda msg: msg.chat.id == host)
def welcome(msg):
    bot.send_message(msg.chat.id, greet(), reply_markup=commands())

@bot.callback_query_handler(func=lambda call: call.message.chat.id == host)
def command(call):
    if call.data == 'screenshot':
        screenshot = pg.screenshot()
        bot.send_photo(call.message.chat.id, screenshot)
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'windows':
        pg.hotkey('winleft', 'm')
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'shutdown':
        os.system('shutdown /s 30')
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'reboot':
        os.system('shutdown /r 30')
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'language':
        pg.hotkey('shift', 'alt')
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'video_start':
        pg.hotkey('alt', 'f9')
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'video_end':
        pg.hotkey('alt', 'f9')
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'app':
        bot.send_message(call.message.chat.id, 'Выберите программу для запуска:', reply_markup=apps())
    
    elif call.data == 'discord':
        os.startfile()
        bot.send_message(call.message.chat.id, 'Сделано')
    
    elif call.data == 'firefox':
        os.startfile()
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'vscode':
        os.startfile()
        bot.send_message(call.message.chat.id, 'Сделано')
    
    elif call.data == 'telegram':
        os.startfile()
        bot.send_message(call.message.chat.id, 'Сделано')
    
    elif call.data == 'explorer':
        os.system('explorer')
        bot.send_message(call.message.chat.id, 'Сделано')
        
    elif call.data == 'dota':
        os.startfile()
        bot.send_message(call.message.chat.id, 'Сделано')
    
        
bot.polling(non_stop=True)