# -*- coding: utf-8 -*-

import random

from aiogram import types

from New_life_3.mini_game.buttons import *

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext


heads_tails_list = ['Орёл', 'Решка']


class HeadsTails(StatesGroup):
    user_coin = State()


async def start_heads_tails(message: types.Message, state: FSMContext):
    coin = random.choice(heads_tails_list)

    if coin == message.text:
        await message.answer('Вы угадали🎊🎉', reply_markup=user_game)

    else:
        await message.answer(f'Вы не угадали😟: {coin}', reply_markup=user_game)

    await state.finish()

