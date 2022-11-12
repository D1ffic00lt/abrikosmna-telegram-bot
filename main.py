import telebot
from telebot import types
from token import token_bot


# @token_bot.message_handler(content_types=['text']) # я конечно, не эксперт, но это вроде не нужно
@token_bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Привет" or message.txt == "Hello":
        token_bot.send_message(message.from_user.id, "Привет, чему хочешь научится?")


class Subjects(object):
    def __init__(self) -> None:
        self.token_bot = telebot.TeleBot(token_bot)
        self.markup: types.InlineKeyboardMarkup = types.InlineKeyboardMarkup()

    def subject_Rus_lenguage(self, message: types.Message):
        # по правилам pep8 функции должны быть только строчными буквами
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(types.InlineKeyboardButton("Математика", url='https://habr.com/ru/all/'))
        token_bot.send_message(
            message.chat.id,
            "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
            reply_markup=self.markup
        )
        token_bot.polling(none_stop=True)

    def subject_Math(self, message: types.Message) -> None:
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(types.InlineKeyboardButton("Математика", url='https://habr.com/ru/all/'))
        token_bot.send_message(
            message.chat.id,
            "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
            reply_markup=self.markup
        )
        token_bot.polling(none_stop=True)

    def subject_phisic(self, message: types.Message) -> None:
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(
            types.InlineKeyboardButton("Математика", url='https://habr.com/ru/all/')
        )
        token_bot.send_message(
            message.chat.id,
            "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
            reply_markup=self.markup
        )
        token_bot.polling(none_stop=True)

    def subject_proraming(self, message: types.Message) -> None:
        self.markup = types.InlineKeyboardMarkup()
        self.markup.add(
            types.InlineKeyboardButton("Математика", url='https://habr.com/ru/all/')
        )
        token_bot.send_message(
            message.chat.id,
            "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
            reply_markup=self.markup
        )
        token_bot.polling(none_stop=True)
