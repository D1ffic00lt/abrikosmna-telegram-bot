import telebot
from telebot import types
import token
from token import token_bot

@token_bot.message_handler(content_types=['text'])
@token_bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Привет" or message.txt == "Hello":
        token_bot.send_message(message.from_user.id, "Привет, чему хочешь научится?")

class Subjects:
    def __init__(self):
        self.token_bot = telebot.TeleBot(token_bot)

    def subject_Rus_lenguage(self, message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Математика", url='https://habr.com/ru/all/')
        markup.add(button1)
        token_bot.send_message(message.chat.id,
                        "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
                        reply_markup=markup)
        token_bot.polling(none_stop=True)

    def subject_Math(self, message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Математика", url='https://habr.com/ru/all/')
        markup.add(button1)
        token_bot.send_message(message.chat.id,
                        "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
                        reply_markup=markup)
        token_bot.polling(none_stop=True)

    def subject_phisic(self, message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Математика", url='https://habr.com/ru/all/')
        markup.add(button1)
        token_bot.send_message(message.chat.id,
                        "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
                        reply_markup=markup)
        token_bot.polling(none_stop=True)

    def subject_proraming(self, message):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Математика", url='https://habr.com/ru/all/')
        markup.add(button1)
        token_bot.send_message(message.chat.id,
                        "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
                        reply_markup=markup)
        token_bot.polling(none_stop=True)
