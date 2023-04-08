# -*- coding: utf-8 -*-

from aiogram import types

from New_life_3.mini_game.buttons import *

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State


import random

number = random.randint(1, 20)
count_of_attempts = 1


class DataGame(StatesGroup):
    Offer_game = State()


async def game(message: types.Message):
    global count_of_attempts, number

    if count_of_attempts == 1:
        await message.answer(f'Отгадай число \nя загадал число от 1 до 20, попробуй его угадать😉', reply_markup=exit_game)
    else:
        await message.answer(f'Введите число🧐')

    await DataGame.Offer_game.set()


async def info_game(message: types.Message, state: FSMContext):
    global number, count_of_attempts

    async with state.proxy() as data:
        data["answer2"] = count_of_attempts

    await state.finish()

    try:
        if int(message.text) == number:
            await message.answer(f'Вы угадали!🎉\nКоличество попыток: {count_of_attempts}', reply_markup=user_game)
            restart_game = count_of_attempts - 1
            count_of_attempts -= restart_game
            number = random.randint(1, 20)

        elif int(message.text) < number:
            await message.answer(f'Попробуйте ещё раз🙃 \nЗагаданное число больше')
            count_of_attempts += 1
            await game(message)

        else:
            await message.answer(f'Попробуйте ещё раз🙃 \nЗагаданное число меньше')
            count_of_attempts += 1
            await game(message)
    except ValueError:
        await message.answer(f'Ошибка❗\nДанные должны иметь числовой тип')
        await game(message)
