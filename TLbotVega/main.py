import telebot
import datetime
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
    if message.text.lower() == 'информация 📑':
        edit(message)
    if message.text.lower() == 'интенсивность потока ☄':
        intens(message)
    if message.text.lower() == 'сейчас ⏰':
        now(message)
    if message.text.lower() == 'день ☀':
        bot.send_message(message.chat.id, 'Прошло недостаточно времени для формирования отчета')
    if message.text.lower() == 'неделя 📅':
        bot.send_message(message.chat.id, 'Прошло недостаточно времени для формирования отчета')



@bot.message_handler()
def vibor(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Интенсивность потока ☄')
    btn2 = types.KeyboardButton('Информация 📑')

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
    bot.send_message(message.chat.id, 'Состояние: Открыто')
def intens(message):
    global inten
    with open(r"C:\Users\user\PycharmProjects\pythonProject10\output.txt", "r") as file: #указать файл с output.txt нейросети
        content = file.read()
        content = int(content)
    if content < 3:
        photo = open('inten\one.png', 'rb')
    elif content < 5:
        photo = open('inten\small.png', 'rb')
    elif content < 7:
        photo = open('inten\cramped.png', 'rb')
    elif content < 10:
        photo = open('inten\many.png', 'rb')
    elif content < 15:
        photo = open('inten\mostmany.png', 'rb')
    elif content >= 15:
        photo = open('inten\six.png', 'rb')

    bot.send_photo(message.chat.id, photo)
    photo.close()

def now(message):

    with open(r"C:\Users\user\PycharmProjects\pythonProject10\output.txt", "r") as file: #указать файл с output.txt нейросети
        content = file.read()
        content = int(content)
    bot.send_message(message.chat.id, f'На данный момент в столовой находится {content} человек(а)')


bot.infinity_polling()