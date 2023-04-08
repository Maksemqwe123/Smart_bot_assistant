# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

db_users = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Просмотреть всех пользователей')
).row(
    KeyboardButton('Удалить всех пользователей')
).row(
    KeyboardButton('Удалить пользователя')
).row(
    KeyboardButton('Сколько пользователей?')
)
