# -*- coding: utf-8 -*-

from aiogram import Bot, Dispatcher
from aiogram.utils import executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

import logging

from roulette.russian_roulette_game import *
from BlackJack_game.my_black_jack import *
from New_life_3.mini_game.tic_tac_toe_game.tic_tac_games import *
from New_life_3.mini_game.little_big.little_big_game import *
from New_life_3.mini_game.heads_tails.game_heads_tails import *

from buttons import *

TOKEN = '6183644433:AAF_9r_KRsWbu3FxnCyGVDwx2HmJQgTg-bg'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)

random.seed()


@dp.message_handler(commands='start', state='*')
async def start_bot(message: types.Message):
    await message.answer(f'Привет {message.from_user.username}, я бот с мини играми, в какую игру ты хочешь сыграть?🎲🎰🕹', reply_markup=user_game)


@dp.message_handler(commands='cancel', state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Действие отменено❌', reply_markup=user_game)


@dp.message_handler(Text(equals='Выйти в главное меню📋', ignore_case=True), state='*')
async def exit_game(message: types.Message, state: FSMContext):
    await message.answer('Вы вышли в главное меню📋', reply_markup=user_game)
    await state.finish()


@dp.message_handler(Text(equals='Орёл-решка🪙', ignore_case=True), state=None)
async def play_heads_tails(message: types.Message):
    await message.answer('Монетка брошена🪙, Орёл или Решка?', reply_markup=coin_heads_tails)

    await HeadsTails.user_coin.set()


@dp.message_handler(state=HeadsTails.user_coin)
async def user_coin(message: types.Message, state: FSMContext):
    await start_heads_tails(message, state)


@dp.message_handler(Text(equals='Больше-меньше🔮', ignore_case=True), state=None)
async def little_big(message: types.Message):
    await game(message)


@dp.message_handler(state=DataGame.Offer_game)
async def play_little_big(message: types.Message, state: FSMContext):
    await info_game(message, state)


@dp.message_handler(Text(equals='Крестики-Нолики❌⭕️', ignore_case=True), state=None)
async def tic_tac(message: types.Message):
    await message.answer('🔽Выбери клетку🔽', reply_markup=update_menu(empty_field_dict))

    await TicTacGame.tic_tac_user.set()


@dp.callback_query_handler(state=TicTacGame.tic_tac_user)
async def play_game_tic_tac(callback_query: types.CallbackQuery, state: FSMContext):
    await start_tic_tac(callback_query, state)


@dp.message_handler(Text(equals='BlackJack♠️♣️♥️♦️', ignore_case=True), state=None)
async def play_black_jack(message: types.Message):
    await start_play_black_jack_game(message)


@dp.message_handler(state=BJGame.black_jack_game)
async def choice(message: types.Message, state: FSMContext):
    await play_game_black_jack(message, state)


@dp.message_handler(Text(equals='Русская рулетка☠️', ignore_case=True), state='*')
async def start_russian_roulette(message: types.Message):
    await play_game(message)


@dp.message_handler(state=RussianRoulette.drum_roulette)
async def play_game_russian_roulette(message: types.Message):
    await drum_number(message)

    await RussianRoulette.shoot.set()


@dp.message_handler(Text(equals='Уйти🫣', ignore_case=True), state='*')
async def exit_game(message: types.Message, state: FSMContext):
    await message.answer('Вы ушли из-за стола👋', reply_markup=user_game)
    await state.finish()


@dp.message_handler(state=RussianRoulette.shoot)
async def shoot_russian_roulette(message: types.Message, state: FSMContext):
    await random_shoot(message, state)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
