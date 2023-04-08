# -*- coding: utf-8 -*-

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from buttons import *

TOKEN_BOT = '5846191784:AAHRbeVwS5SfmfzgSI0gFDNbOCrushXr6S8'


bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot, storage=MemoryStorage())


class Budget(StatesGroup):
    budget_users = State()
    term_date_users = State()


class Expenses(StatesGroup):
    cost = State()
    end_cost = State()


class CatalogAdd(StatesGroup):
    add_catalog_users = State()


class CatalogDelete(StatesGroup):
    delete_catalog_users = State()


@dp.message_handler(commands='start', state='*')
async def start_bot(message: types.Message):
    await message.answer(f'Привет {message.from_user.username}, я бот который подсчитывает расходы')

    await message.answer('Укажите бюджет')
    await Budget.budget_users.set()


@dp.message_handler(state=Budget.budget_users)
async def budget(message: types.Message, state: FSMContext):
    await message.answer('Укажите на какой срок вы хотите рассчитать ваш бюджет', reply_markup=date_users)

    await Budget.term_date_users.set()


@dp.message_handler(state=Budget.term_date_users)
async def term_date(message: types.Message, state: FSMContext):
    await message.answer('Отлично бюджет записан, на что рассчитываешь тратить свой бюджет?', reply_markup=budget_expenses)
    await state.finish()


@dp.callback_query_handler(text='expenses')
async def expenses_users(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'На что вы потратили бюджет?', reply_markup=reply_markup)

    await Expenses.cost.set()


@dp.callback_query_handler(lambda call: True, state=Expenses.cost)
async def categories_expenses_users(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    await bot.send_message(callback_query.from_user.id, f'Какую стоимость вы потратили на {store_buttons_clicked} ?')

    await Expenses.end_cost.set()


@dp.message_handler(state=Expenses.end_cost)
async def expenses_cost_users(message: types.Message, state: FSMContext):
    cost_users = message.text
    print(cost_users)
    await message.answer('Расчёт посчитан, что дальше?', reply_markup=budget_expenses)

    await state.finish()


# @dp.callback_query_handler(text='edit_user')
# async def change_dir(callback_query: types.CallbackQuery):
#     await bot.send_message(callback_query.from_user.id, 'Что вы хотите сделать?', reply_markup=users_change)
#
#
# @dp.callback_query_handler(text='Добавить каталог')
# async def catalog(callback_query: types.CallbackQuery):
#     await bot.send_message(callback_query.from_user.id, 'Напишите название каталога')
#
#     await CatalogAdd.add_catalog_users.set()
#
#
# @dp.message_handler(state=CatalogAdd.add_catalog_users)
# async def add_catalog(message: types.Message, state: FSMContext):
#     text_catalog = message.text
#
#     users_list.append(text_catalog)
#
#     await message.answer('Каталог успешно добавлен)', reply_markup=budget_expenses)
#
#     await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
