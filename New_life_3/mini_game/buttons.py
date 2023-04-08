# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

empty_field = " "
empty_field_dict = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}


def update_menu(dict_user: dict):
    tic_tac_toe = InlineKeyboardMarkup().add(
        InlineKeyboardButton(dict_user.get(1), callback_data='1'),
        InlineKeyboardButton(dict_user.get(2), callback_data='2'),
        InlineKeyboardButton(dict_user.get(3), callback_data='3')

    ).add(
        InlineKeyboardButton(dict_user.get(4), callback_data='4'),
        InlineKeyboardButton(dict_user.get(5), callback_data='5'),
        InlineKeyboardButton(dict_user.get(6), callback_data='6')

    ).add(
        InlineKeyboardButton(dict_user.get(7), callback_data='7'),
        InlineKeyboardButton(dict_user.get(8), callback_data='8'),
        InlineKeyboardButton(dict_user.get(9), callback_data='9')
    )
    return tic_tac_toe


user_game = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Русская рулетка☠️'),
    KeyboardButton('Больше-меньше🔮')
).add(
    KeyboardButton('Орёл-решка🪙'),
    KeyboardButton('BlackJack♠️♣️♥️♦️')
).add(
    KeyboardButton('Крестики-Нолики❌⭕️')
)

black_jack_game = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Взять карту♣️♥️'),
    KeyboardButton('Хватит⛔️'),
    KeyboardButton('Другие игры🎲🕹🎰')

)

russian_game = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Продолжить☠️💀'),
    KeyboardButton('Уйти🫣')
)

shoot_twist = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('крутить🔫'),
    KeyboardButton('выстрелить😈')
)

number_bullets = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('1'),
    KeyboardButton('2'),
    KeyboardButton('3')
).add(
    KeyboardButton('4'),
    KeyboardButton('5')
)

coin_heads_tails = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Орёл'),
    KeyboardButton('Решка')
).row(
    KeyboardButton('Выйти в главное меню📋')
)

exit_game = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Выйти в главное меню📋')
)
