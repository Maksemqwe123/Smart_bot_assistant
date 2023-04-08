# -*- coding: utf8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

response_to_start = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Привет, знакомы?')
).row(
    KeyboardButton('Что случилось ?'),
    KeyboardButton('Ты чё накурился?')
)
cops_or_plan_B = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Что случилось?')
).row(
    KeyboardButton('Ты похоже ошибся номером')
)

false_or_true = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Нет')
).row(
    KeyboardButton('Да я угараю, рассказывай что случилось')
).row(
    KeyboardButton('Я Дима но я уверен, что я не тот Дима, которого ты ищешь')
)

stranger_help = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Почему ты сам их не вызовишь?')
).row(
    KeyboardButton('Хорошо что за адрес?')
).row(
    KeyboardButton('Что случилось?'),
    KeyboardButton('Зачем вы пошли грабить?')
).row(
    KeyboardButton('Почему ты просто не убежишь?')
)
