# -*- coding: utf8 -*-

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import filters
from aiogram.dispatcher.filters import Text
from buttons import *
import time

BOT_TOKEN = '5846191784:AAHRbeVwS5SfmfzgSI0gFDNbOCrushXr6S8'


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer('Всё это конец, план А полностью праволился')
    time.sleep(3)
    await message.answer('Саню походу убили, мы остались вдвоём с максом')
    time.sleep(3)
    await message.answer('И нахрена мы пошли грабить этого деда?', reply_markup=response_to_start)


@dp.message_handler(Text(equals='Привет, знакомы?', ignore_case=True))
async def hallo(message: types.Message):
    time.sleep(3)
    await message.answer('Вот так значит да?')
    time.sleep(3)
    await message.answer('То-есть когда тебе нужна помощь чтобы обокрасть чёкнутого деда, '
                         'я ради тебя не полетел в египет, а когда у нас проблема С ТВОИМ ЖЕ ДЕЛОМ, '
                         'ты делаешь вид как будто мы не знакомы?')
    time.sleep(3)
    await message.answer('У тебя последний шанс или я звоню ментам и сдаю тебя первого,'
                         ' либо ты рассказываешь что за план Б', reply_markup=cops_or_plan_B)


@dp.message_handler(Text(equals='Ты похоже ошибся номером', ignore_case=True))
async def error_number(message: types.Message):
    time.sleep(3)
    await message.answer('Подожди то-есть ты не Дима?', reply_markup=false_or_true)


@dp.message_handler(Text(equals='Нет' or "Я Дима но я уверен, что я не тот Дима, которого ты ищешь", ignore_case=True))
async def no_dima(message: types.Message):
    time.sleep(3)
    await message.answer('Вот чёрт, в спешки на одну цифру ошибся')
    time.sleep(3)
    await message.answer('Вызови пожалуйста ментов, мне сейчас очень страшно', reply_markup=stranger_help)


@dp.message_handler(Text(equals='Почему ты сам их не вызовишь?', ignore_case=True))
async def what_number_call(message: types.Message):
    time.sleep(3)
    await message.answer('Он может услышать')


@dp.message_handler(Text(equals='Кто он?'))
async def who_is_he(message: types.Message):
    time.sleep(3)
    await message.answer('Дед которого мы пошли грабить, мэр нашего города')
    time.sleep(3)
    await message.answer('Мы решили ограбить деда, из-за того что он сбил девушку нашего друга,'
                         ' а милиция даже не приняла наше заявление, сказали что им не нужны неприятности')
    time.sleep(3)
    await message.answer('Мы решили ему отомстить, у этой твари раскошный дворец в котором он живёт,'
                         ' а когда мы у него потребовали деньги он даже отказался платить за лечение этой девушки')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
