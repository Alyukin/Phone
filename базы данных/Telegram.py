import random
import sqlite3
import telebot

token = '2105702284:AAHioH7QOuH3eWOUcX3uvDjAIPJD-4FyncE'

bot = telebot.TeleBot(token)

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            userId INT PRIMARY KEY
                )""")

connection.commit()

state = 0


def get_state():
    return state


@bot.message_handler(commands=['start'])
def ask_name(message):
    bot.send_message(message.chat.id, "Как вас зовут?")
    global state
    state = 1


@bot.message_handler(func=lambda message: state == 1)
def ask_preferencies(message):
    user_name = message.text

    bot.send_message(message.chat.id,
                     user_name + ", фотографии кого вы хотите получить? Доступные опции: коты / собаки ")

    global state
    state = 2

@bot.message_handler(commands = ['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
    markup.add(switch_button)
    bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)

@bot.message_handler(func=lambda message: get_state() == 2)
def give_preferencies_answer(message):
    if message.text.lower() == 'коты' or message.text.lower() == 'собаки':
        bot.send_message(message.chat.id, "Принято!")

        global state
        state = 3
    else:
        bot.send_message(message.chat.id, "Введите ответ ещё раз")


@bot.message_handler(commands=['get_cat'])
def send_cat_photo(message):
    base_url = 'https://aws.random.cat/view/'
    number = random.randint(1, 1000)
    bot.send_photo(message.chat.id, base_url + str(number))

@bot.message_handler(commands=['get_dog'])
def send_dog_photo(message):
    base_url = ''
    number = random.randint(1, 1000)
    bot.send_photo(message.chat.id, base_url + str(number))


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    # message.chat.id -> bd
    try:
        local_connection = sqlite3.connect('users.db')
        local_cursor = local_connection.cursor()
        local_cursor.execute("INSERT INTO users VALUES(?);", (message.chat.id,))
        local_connection.commit()
        bot.send_message(message.chat.id, "you have subscribed")
    except Exception:
        bot.send_message(message.chat.id, "you have subscribed earlier")


@bot.message_handler(commands=['get_subscribers'])
def get_subscribers(message):
    local_connection = sqlite3.connect('users.db')
    local_cursor = local_connection.cursor()
    local_cursor.execute("SELECT * from users;")
    all_results = local_cursor.fetchall()
    bot.send_message(message.chat.id, str(all_results))


bot.polling(none_stop=True, interval=0)
