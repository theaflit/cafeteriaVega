import telebot
from telebot import types

from config import Config
admin_id = Config.admin_id
bot = telebot.TeleBot(token = Config.token)

inten = 1
porth = 15
@bot.message_handler(commands=['start'])
def indification(message):
    bot.send_message(message.chat.id,
                     'Приветствую вас! 👋 Я ваш надежный помощник в управлении потоком посетителей и обеспечении комфортного обслуживания в ресторане "Вега"🌌.\n')
    vibor(message)
@bot.message_handler()
def info(message):

    if message.text.lower() == '◀ назад':
        vibor(message)
    if message.text.lower() == 'аналитика 📊':
        analitic(message)
    if message.text.lower() == 'изменение информации 📑':
        edit(message)
    if message.text.lower() == 'интенсивность потока ☄':
        intens(message)
    if message.text.lower() == 'сейчас ⏰':
        now(message)
@bot.message_handler()
def vibor(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Интенсивность потока ☄')
    btn2 = types.KeyboardButton('Изменение информации 📑')

    btn3 = types.KeyboardButton('Аналитика 📊')

    markup.add(btn1, btn2)
    markup.add(btn3)

    bot.send_message(message.chat.id, 'Вы находитесь в главном меню', reply_markup=markup)

def analitic(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Сейчас ⏰')
    btn2 = types.KeyboardButton('День ☀')

    btn3 = types.KeyboardButton('Неделя 📅')
    btn5 = types.KeyboardButton('◀ Назад')

    markup.add(btn1, btn2, btn3)
    markup.add(btn5)

    bot.send_message(message.chat.id, 'В этом разделе вы можете посмотреть аналитику посетителей за определенный период', reply_markup=markup)

def edit(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn5 = types.KeyboardButton('◀ Назад')

    markup.add(btn5)

    bot.send_message(message.chat.id, 'В этом разделе вы можете просмтреть инфомацию о времени работы ресторана', reply_markup=markup)
def intens(message):
    global inten
    if inten == 1:
        photo = open('inten\one.png', 'rb')
    if inten == 2:
        photo = open('inten\small.png', 'rb')
    if inten == 3:
        photo = open('inten\cramped.png', 'rb')
    if inten == 4:
        photo = open('inten\inten_impossible.JPEG', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    pass
def now(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn5 = types.KeyboardButton('◀ Назад')

    markup.add(btn5)

    bot.send_message(message.chat.id, f'На данный момент в столовой находится {porth} человек, поэтому стоит немного подождать', reply_markup=markup)
bot.infinity_polling()