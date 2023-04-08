# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


date_users = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('На 3 дня'),
    KeyboardButton('На неделю')
).add(
    KeyboardButton('На месяц'),
    KeyboardButton('На 3 месяца')
)

budget_expenses = InlineKeyboardMarkup().add(
    InlineKeyboardButton('Увеличить бюджет', callback_data='budget_add'),
    InlineKeyboardButton('Записать расходы', callback_data='expenses')
).add(
    InlineKeyboardButton('Изменить каталог', callback_data='edit_user'),

)

list_categories_expenses = ['Одежда', 'Бытовая химия', 'Продукты', 'Счета', 'Транспорт', 'Шопинг', 'Расходы по работе', 'Прочие']
users_list = []

reply_markup = InlineKeyboardMarkup()

for i in list_categories_expenses:
    users_list.append(i)

for i in users_list:
    reply_markup.add(InlineKeyboardButton(i, callback_data=i))

# edit_dir = InlineKeyboardMarkup().add(
#
# )

change_list = ['Добавить каталог', 'Удалить каталог']
users_change = InlineKeyboardMarkup()

for i in change_list:
    users_change.add(InlineKeyboardButton(i, callback_data=i))
