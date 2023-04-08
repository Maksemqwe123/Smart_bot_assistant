# -*- coding: utf8 -*-

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import filters
BOT_TOKEN = '5846191784:AAHRbeVwS5SfmfzgSI0gFDNbOCrushXr6S8'


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    welcome = message.from_user.full_name
    await bot.send_game(chat_id=message.chat.id, game_short_name='SubwaySurfers_134_bot')


@dp.callback_query_handler(lambda callback_query: callback_query.game_short_name == 'SubwaySurfers_134_bot')
async def bot_games(call):
    await bot.answer_callback_query(callback_query_id=call.id, url='https://agar.io/#ffa')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
