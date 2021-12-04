import random
import sqlite3

import telebot
from telebot import types

token = '2105702284:AAHioH7QOuH3eWOUcX3uvDjAIPJD-4FyncE'

bot = telebot.TeleBot(token)

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            userId INT PRIMARY KEY
                )""")

connection.commit()

win = 0
lose = 0
state = 0


def get_state():
    return state


@bot.message_handler(commands=['start'])
def ask_name(message):
    bot.send_message(message.chat.id, "Привет! Как тебя зовут?")
    global state
    state = 1


@bot.message_handler(func=lambda message: state == 1)
def start_message(message):
    user_name = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('/game', 'cats')
    bot.send_message(message.chat.id,
                     user_name + ', ты можешь сыграть в Камень-Ножницы-Бумага(/game) или получить фотографии котов(/cats)',
                     reply_markup=markup)
    global state
    state = 2


@bot.message_handler(commands=['cats'])
def send_cat_photo(message):
    base_url = 'https://aws.random.cat/view/'
    number = random.randint(1, 1000)
    bot.send_photo(message.chat.id, base_url + str(number))


@bot.message_handler(commands=['game'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # keyboard
    markup.add('Камень', 'Бумага', 'Ножницы', '/back')
    bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)


@bot.message_handler(commands=['back'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton('/start')
    game = types.KeyboardButton('/game')
    cat = types.KeyboardButton('/cats')
    markup.add(start, game, cat)
    bot.send_message(message.chat.id, 'Выбирай функцию:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def game1(message):
    if message.text == 'Камень':
        if random.randint(1, 3) == 1:
            bot.send_message(message.chat.id, "Камень.")
            bot.send_message(message.chat.id, 'Ничья')
        elif random.randint(1, 3) == 2:
            bot.send_message(message.chat.id, 'Ножницы.')
            bot.send_message(message.chat.id, 'Ты победил')
        elif random.randint(1, 3) == 3:
            bot.send_message(message.chat.id, 'Бумага.')
            bot.send_message(message.chat.id, 'Ты проиграл')
    elif message.text == 'Ножницы':
        if random.randint(1, 3) == 1:
            bot.send_message(message.chat.id, 'Камень.')
            bot.send_message(message.chat.id, 'Ты проиграл')
        elif random.randint(1, 3) == 2:
            bot.send_message(message.chat.id, 'Ножницы.')
            bot.send_message(message.chat.id, 'Ничья')
        elif random.randint(1, 3) == 3:
            bot.send_message(message.chat.id, 'Бумага.')
            bot.send_message(message.chat.id, 'Ты победил')
    elif message.text == 'Бумага':
        if random.randint(1, 3) == 1:
            bot.send_message(message.chat.id, 'Камень.')
            bot.send_message(message.chat.id, 'Ты победил')
        elif random.randint(1, 3) == 2:
            bot.send_message(message.chat.id, 'Ножницы.')
            bot.send_message(message.chat.id, 'Ты проиграл')
        elif random.randint(1, 3) == 3:
            bot.send_message(message.chat.id, 'Бумага.')
            bot.send_message(message.chat.id, 'Ничья')
    global state
    state = 3

@bot.message_handler(func=lambda message: state == 3)
def results(message):
    global lose
    global win
    result = message.text
    if result == 'Ты проиграл':
        lose = lose + 1
        bot.send_message(message.chat.id, 'Побед:' + win + ' Поражений:' + lose)
    if result == 'Ты победил':
        win = win + 1
        bot.send_message(message.chat.id, 'Побед:' + win + ' Поражений:' + lose)
    if result == 'Ничья':
        bot.send_message(message.chat.id, 'Побед:' + win + ' Поражений:' + lose)


if __name__ == '__main__':
    bot.infinity_polling()

bot.polling(none_stop=True, interval=0)
