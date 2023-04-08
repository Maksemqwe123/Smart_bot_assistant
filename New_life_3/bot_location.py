# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# import h3
# from aiogram.dispatcher.filters import Command
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from geolocation import loc_geo
# from aiogram.dispatcher.filters.state import StatesGroup, State
# from aiogram.dispatcher import FSMContext
# from parsers.parser_cinema import *
# metrix_1 = []
# poi = []
#
#
# class Test(StatesGroup):
#     Q1 = State()
#     Q2 = State()
#
#
# bot_expenses = Bot('5587641606:AAGVMc75T2zaq_GovxKy0nn8wiKFAKBbOvg')
# dp = Dispatcher(bot_expenses, storage=MemoryStorage())
#
# me = []
#
#
# @dp.message_handler(commands='start')
# async def geo(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
#     keyboard.add(button_geo)
#     keyboard_1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo_1 = types.KeyboardButton(text="Узнать ближайшую кофе", request_location=loc_geo)
#     keyboard_1.add(button_geo_1)
#     await bot_expenses.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)
#
#
# @dp.message_handler(Command("test"), state=None)
# async def enter_test(message: types.Message):
#     await message.answer("Введите город")
#
#     await Test.Q1.set()
#
#
# @dp.message_handler(state=Test.Q1)
# async def answer_q1(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     await state.update_data(answer1=answer)
#     print(answer)
#     poi.append(answer)
#
#     await Test.next()



# @dp.message_handler(content_types=['text'])
# def text(message):
#     msg = message.text
#
#     if msg == '1':
#         send = bot_expenses.send_message(message.chat.id,
#                                     "Введите следующее значение".format(message.from_user, bot_expenses.get_me()),
#                                     parse_mode='html')
#
#         a = inputBot(message, 'Введите следующее значение')
#         print(a)  # Вводит значение, которое мы запросили у пользователя

# def inputBot(message, text):
#     global a
#     def ret(message):
#         a.clear()
#         a.append(message.text)
#         return False
#
#     a.clear()
#     mes = bot_expenses.send_message(message, text)
#     print(mes)


        # for i in l:
        #     ab = l[:]
        #     ab.append(geolocation_me)
        #     ab.sort()
        #     ab_index = ab.index(geolocation_me) - 1 if ab.index(geolocation_me) > 0 else 0
        #     spend = (ab[ab_index])
        #     print(spend)


        #     distance = h3.point_dist(geolocation_me, i, unit='m')  # to get distance in meters
        #     # print(i, round(distance))
        #     metrix = (round(distance))
        #     print(f'Дистанция между точка {metrix} m')
        #     metrix_1.append(metrix)
        # print(min(metrix_1))


# def location(message):
#     if message.location is not None:
#         print(message.location)
#         print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude)
#
# if __name__ == '__main__':
#     print('bot_expenses polling started')
#     executor.start_polling(dp, skip_updates=True)
# latitude: 52.473507; longitude: 31.02713



# import telebot
# from telebot import types
# bot_expenses = telebot.TeleBot('5587641606:AAGVMc75T2zaq_GovxKy0nn8wiKFAKBbOvg')
#
#
# @bot_expenses.message_handler(commands=["start"])
# def start (message):
#     #Клавиатура с кнопкой запроса локации
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
#     keyboard.add(button_geo)
#     bot_expenses.send_message(message.chat.id, "Поделись местоположением", reply_markup=keyboard)
#
#  #Получаю локацию
# @bot_expenses.message_handler(content_types=['location'])
# def location (message):
#     if message.location is not None:
#         print(message.location)
#         print(message)
#
# bot_expenses.polling(none_stop = True)
# input()

# Отдать с начала пользователю долготу и шыроту, а потом запросить координаты, чтобы показать его геолокацию



# @dp.message_handler(content_types=["location"])
# async def location(message):
#     if message.location is not None:
#         geolocation_me = (message.location.latitude, message.location.longitude)
#         me.append(geolocation_me)
#         print(geolocation_me)
#         ab = loc_geo[:]
#         ab.append(geolocation_me)
#         ab.sort()
#         ab_index = ab.index(geolocation_me) - 1 if ab.index(geolocation_me) > 0 else 0
#         spend = (ab[ab_index])
#         print(spend[0])
#         await bot_expenses.send_location(message.chat.id, spend[0], spend[1])


from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from geolocation import loc_geo
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sq_file_lite import *

metrix_1 = []

db = Database('database.db')
bot = Bot('5587641606:AAGVMc75T2zaq_GovxKy0nn8wiKFAKBbOvg')
dp = Dispatcher(bot, storage=MemoryStorage())

me = []
db.cursor.execute('INSERT INTO use VALUES(?)', ['gomel', ])

@dp.message_handler(commands='start')
async def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    keyboard_1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo_1 = types.KeyboardButton(text="Узнать ближайшую кофе", request_location=loc_geo)
    keyboard_1.add(button_geo_1)
    await bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)


@dp.message_handler(content_types=["location"])
async def location(message):
    if message.location is not None:
        geolocation_me = (message.location.latitude, message.location.longitude)
        me.append(geolocation_me)
        print(geolocation_me)
        ab = loc_geo[:]
        ab.append(geolocation_me)
        ab.sort()
        ab_index = ab.index(geolocation_me) - 1 if ab.index(geolocation_me) > 0 else 0
        spend = (ab[ab_index])
        print(spend[0])
        await bot.send_location(message.chat.id, spend[0], spend[1])


class DataInput(StatesGroup):
    Q1 = State()
    Q2 = State()


@dp.message_handler(commands=['test'], state=None)
async def process_hello(message: types.Message):
    await message.answer('Введите ваш город')

    await DataInput.Q1.set()


@dp.message_handler(state=DataInput.Q1)
async def put_registration_number(message: types.Message, state: FSMContext):
    kb_text = message.text

    async with state.proxy() as data:
        data["answer1"] = kb_text

    await message.answer('Сейчас обработаем')

    db.cursor.execute('INSERT INTO use VALUES(?)', ['gomel', ])

    await state.reset_state(with_data=False)


    # async with state.proxy() as data:
    #     data["answer1"] = kb_text
    # if message.chat.type == 'private':
    #     if not db.create_profile(kb_text):
    #         print(db.edit_profile(kb_text))
        # cursor = db.cursor()
        # cursor.execute(db)
        # record = cursor.fetchall()
        # print(record)


if __name__ == '__main__':
    print('bot_expenses polling started')
    executor.start_polling(dp, skip_updates=True)
