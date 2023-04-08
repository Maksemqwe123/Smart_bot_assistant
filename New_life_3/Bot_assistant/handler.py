from weather_tg_bot import *

from New_life_3.Bot_assistant.city_weather_bot.city_rename import *
from New_life_3.Bot_assistant.city_weather_bot.geolocation_user import *
from New_life_3.Bot_assistant.city_weather_bot.weather import ru
from New_life_3.Bot_assistant.parsers.cook_parser import *
from New_life_3.Bot_assistant.parsers.parser_cinema import *
from New_life_3.Bot_assistant.parsers.parser_kinogo import *
from New_life_3.Bot_assistant.parsers.parser_litres import *
from New_life_3.Bot_assistant.parsers.parser_pizza import *

from New_life_3.Bot_assistant.buttons_bot.buttons import *
from New_life_3.Bot_assistant.buttons_bot.buttons_admin import *

import asyncio
import os
import random
import time
from copy import deepcopy

import aioschedule
from aiogram.utils.exceptions import BotBlocked

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

strings_date = time.strftime("%Y-%m-%d %H:%M:%S")

database = MyPostgres()

number = random.randint(1, 20)
count_of_attempts = 1

list_users = []

winter_img_files_jokes = r'C:/Users/makce/PycharmProjects/pythonProject/New_life_3/Bot_assistant/winter_img'
summer_img_files_jokes = r'C:/Users/makce/PycharmProjects/pythonProject/New_life_3/Bot_assistant/summer_img'

winter_img_jokes = os.listdir(winter_img_files_jokes)
summer_img_jokes = os.listdir(summer_img_files_jokes)


class WeatherToday(StatesGroup):
    weather_today_city = State()


async def start_message(message: types.Message):
    welcome = message.from_user.full_name
    await message.answer(f'Привет {welcome}, Выбери в каком городе хочешь круто отдохнуть🏙😎',
                         reply_markup=user_kb)
    await message.answer('❗️Если вашего города нету в меню, укажите его в ручную❗️')

    if not database.select_user(message.from_user.id):
        database.insert_table_users_date(message.from_user.id, welcome, '"' + strings_date + '"')

        logging.info('Добавлен новый пользователь в бд')
    else:
        logging.info('Новых данных в бд не добавлено')

    await WeatherToday.weather_today_city.set()


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Действие отменено❌', reply_markup=house_or_street)


async def info(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer('Отправляю клавиатуру', reply_markup=db_users)


async def select_user(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        info_db = ''
        user_select = database.select_all_users()
        for all_info_users in range(len(user_select)):
            info_db = info_db + 'id_users|' + f'{user_select[all_info_users][0]}\n'
            info_db = info_db + 'full_name|' + f'{user_select[all_info_users][1]}\n'
            info_db = info_db + 'latitude|' + f'{user_select[all_info_users][2]}\n'
            info_db = info_db + 'longitude|' + f'{user_select[all_info_users][3]}\n'
            info_db = info_db + 'city|' + f'{user_select[all_info_users][4]}\n'
            info_db = info_db + 'entry_date|' + f'{user_select[all_info_users][5]}\n'
            info_db = info_db + 'last_date|' + f'{user_select[all_info_users][6]}\n\n'

        await message.answer(info_db)


class DeleteAllUsers(StatesGroup):
    are_you_sure = State()


class DeleteOneUsers(StatesGroup):
    one_user = State()


async def delete_all_users(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        ready = 'Вы уверены?'
        await message.answer(ready)
        await DeleteAllUsers.are_you_sure.set()


async def delete_and_no(message: types.Message, state: FSMContext):
    if message.text == 'yeS':
        database.delete_all_users()
        await message.answer('Удаление прошло успешно', reply_markup=db_users)
    await state.finish()


async def delete_one_user(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer('Введите id пользователя которого хотите удалить')

    await DeleteOneUsers.one_user.set()


async def id_user_delete(message: types.Message, state: FSMContext):
    if database.select_user(message.text):
        database.delete_user_main_table(message.text)

        await message.answer('Пользователь успешно удалён', reply_markup=db_users)

    else:
        await message.answer('Произошла ошибка', reply_markup=db_users)

    await state.finish()


async def select_number_users(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer(f'Сейчас пользователей: {database.number_users()[0][0]}')


async def send_all(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == ADMIN_ID:
            text_admin = message.text[9:]
            try:
                all_info = database.select_all_users()  # Получаю всю информацию с бд
                for all_user in range(len(all_info)):  # Раскрываю список
                    id_user = all_info[all_user][0]  # Получаю все id

                    try:
                        await bot.send_message(
                            chat_id=id_user, text=text_admin)

                    except BotBlocked:
                        database.delete_user_main_table(int(id_user))

            except Exception as ex:
                logging.error(repr(ex))

            await bot.send_message(message.from_user.id, "Успешная рассылка")


async def today(message: types.Message, state: FSMContext):
    user_location = {}
    try:
        if not message.location is None:
            geolocator = Nominatim(user_agent="LocWeather")

            city_address = (message.location.latitude, message.location.longitude)
            location_user_weather_today = geolocator.reverse(city_address)
            geo_loc_user_weather = (str(location_user_weather_today).split(',')[-4].lstrip())
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={geo_loc_user_weather}&appid={OPEN_WEATHER_TOKEN}&units=metric&lang={ru}"
            )

            data = r.json()

            user_location = deepcopy(data)

            database.update_table_geo(
                message.location.latitude, message.location.longitude, geo_loc_user_weather, message.from_user.id
            )
            logging.info('В бд добавлено новые данные о пользователе')

        else:
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPEN_WEATHER_TOKEN}&units=metric&lang={ru}"
            )

            data = r.json()

            user_location = deepcopy(data)

        city = user_location["name"]
        cur_weather = user_location["main"]["temp"]
        weather_description = user_location["weather"][0]["description"]
        wind = user_location["wind"]["speed"]

        await message.answer(
            f'В городе🏙: {city} \nТемпература воздуха🌤: {cur_weather} C \nОжидается🌎: {weather_description}\n'
            f'Скорость ветра🌬: {wind} м/c', reply_markup=house_or_street)

        if cur_weather > 30:
            await message.answer('Сегодня на улице безумная жара☀️🥵'
                                 'Внимание На улицу без головного убора выходить опасно и крайне не рекомендуется выходить на улицу до 14:30')

        if 30 > cur_weather > 25 and wind < 7:
            await message.answer('Сегодня на улице очень жаркая погода☀️🥵'
                                 '\nКрайне не рекомендуется выходить на улицу без головного убора🧢'
                                 '\nТакже в этот день рекомендуется пить побольше воды🚰')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{summer_img_files_jokes}/' + random.choice(summer_img_jokes), 'rb'))

        if 25 > cur_weather > 20 and wind < 6:
            await message.answer('Сегодня на улице жаркая погода☀️'
                                 '\nПришло время для летнего загара и водных процедур🏊‍♂'
                                 '\nВ такую погоду можно надеть: футболку, шорты👟🩳👕, кроссовки и обязательно надень головной убор🧢')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{summer_img_files_jokes}/' + random.choice(summer_img_jokes), 'rb'))

        elif 20 > cur_weather > 15 and wind < 5:
            await message.answer('Сегодня на улице тепло🌤☀️😎, отличный день чтобы пойти на улицу🚶‍♂️🚶‍♀️'
                                 '\nВ такую погоду посоветую одеть легкую кофту, джинсы и кроссовки или можно остаться дома👨‍💻')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{summer_img_files_jokes}/' + random.choice(summer_img_jokes), 'rb'))

        elif 15 > cur_weather > 10 and wind < 5:
            await message.answer('На улице теплая погода, но сегодня не время загорать☀️😎'
                                 '\nВ такую погоду можно одеть кофту или лёгкую ветровку, а также можно остаться дома👨‍💻')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))

        elif 10 > cur_weather > 5 and wind < 5:
            await message.answer('Сегодня на улице довольно нестабильная погода☀️☔️🏊‍♂️'
                                 '\nВозможны перепады температуры🥶🥵 \nМожно остаться дома👨‍💻 или пойти на улицу🚶‍♂🚶‍♀')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))

        elif 2 > cur_weather > -2 and (weather_description == 'снег' or weather_description == 'небольшой проливной дождь' or weather_description == 'дождь' or weather_description == 'небольшой снегопад' or weather_description == 'небольшой снег'):
            await message.answer('Сегодня на улице плохая погода, выпадение осадков☔️❄️ слякоть или гололёд🏊‍♂'
                                 '\nВ этот день лучше остаться дома и посмотреть какие развлечение я тебе приготовил😉🎬🍕')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))


        elif 5 > cur_weather > -4 and wind < 5:
            await message.answer('Сегодня на улице прохладно❄️ \nВозможно слякоть и гололёд🏊‍♂️⛸'
                                 '\nМожно остаться дома👨‍💻 или пойти на улицу🚶‍♂🚶‍♀')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))

        elif -4 > cur_weather > -9 and wind < 5:
            await message.answer(
                'Сейчас на улице холодно❄️ \nОденься потеплее🧤 \nЖелательно ещё поесть перед выходом🍜🍳')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))

        elif -9 > cur_weather > -16:
            await message.answer('Cейчас на улице довольно холодно \nПосоветую тебе остаться дома👨‍💻'
                                 '\nНо если тебе не страшен холод🥶 \nМогу посоветовать куда можно сходить🚶‍♂🚶‍♀')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))

        elif cur_weather < -16:
            await message.answer('Cейчас на улице очень холодно🥶☠️ \nостанься лучше дома👨‍💻')

            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))

        if 8 > wind > 5:
            await message.answer('На сегодня ожидается сильный ветер🌬, посоветую остаться дома👨‍💻')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))

        if weather_description == 'небольшой проливной дождь' or weather_description == 'дождь':
            await message.answer('На сегодня ожидается дождь☔️'
                                 '\nПосоветую остаться дома и посмотреть что я для тебя приготовил😉🎬🍕')
            await bot.send_photo(chat_id=message.from_user.id, photo=open(f'{winter_img_files_jokes}/' + random.choice(winter_img_jokes), 'rb'))

    except (TypeError, KeyError):
        await message.reply("Проверьте название города")

    finally:
        await state.finish()
        user_location.clear()


async def leisure(message: types.Message):
    await message.answer(
        'можно посмотреть/почитать фильм/книгу, но перед этим,🎬📚 я бы посоветовал заварить чая/кофе.☕\n'
        'могу подсказать как легко и просто приготовить вкусный десерт,🧁'
        'так же проходит акция при заказе пиццы🍕', reply_markup=help_assistant_house)


class DataFilms(StatesGroup):
    Film_cimema = State()


async def street(message: types.Message):
    await DataFilms.Film_cimema.set()

    await message.answer('В каком городе вы хотите посмотреть развлечения🎬☕🍕', reply_markup=user_kb)


async def leisure_city(message: types.Message, state: FSMContext):
    await rename_leisure_city(message, state)


async def back_weather(message: types.Message):
    await message.answer('Погода на сегодня ожидается...', reply_markup=user_kb)

    await WeatherToday.weather_today_city.set()


class DataGame(StatesGroup):
    Offer_game = State()


async def game(message: types.Message):
    global count_of_attempts, number

    if count_of_attempts == 1:
        await message.answer(f'Отгадай число \nя загадал число от 1 до 20, попробуй его угадать😉', reply_markup=menu)
    else:
        await message.answer(f'Введите число🧐')

    await DataGame.Offer_game.set()


async def exit_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('секунду⏱', reply_markup=house_or_street)


async def back_street(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('секунду⏱', reply_markup=help_assistant_street)


@dp.callback_query_handler(text='go_to_back')
async def back_today(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.send_message(callback_query.from_user.id, 'секунду⏱', reply_markup=house_or_street)


async def pizza(message: types.Message):
    for sort_parser_pizza in all_parser_pizza[1:4]:
        await message.answer(sort_parser_pizza[0])


async def kinogo(message: types.Message):
    for sort_kinogo_no_duplicates in kinogo_no_duplicates[1:4]:
        await message.answer(f'Название: {sort_kinogo_no_duplicates[0]} \nCсылка: {sort_kinogo_no_duplicates[-1]}')
    await message.answer('Хочешь посмотреть больше фильмов и выбрать свой любимый жанр❓'
                         '\nУ нас есть бот "I love you kinogo" который поможет вам с '
                         'выбором фильма🍿🎬', reply_markup=bot_films)


async def book(message: types.Message):
    for sort_all_books in all_books[1:4]:
        await message.answer(f'Название:{sort_all_books[0]} \nCcылка: {sort_all_books[-1]}\n')


async def cook(message: types.Message):
    for sort_all_cooks in all_cooks[1:4]:
        await message.answer(f'Название: {sort_all_cooks[0]} \nCcылка: {sort_all_cooks[-1]}\n')

    await message.answer(
        'Нравится готовить и хочешь узнать больше рецептов по приготовлению десертов❓ '
        '\nУ нас есть бот "Nice Desserts" который поможет тебе приготовить больше вкусных десертов🥧🍦',
        reply_markup=bot_desserts
    )


async def cinema(message: types.Message):
    ParserCinema(location_city_name)
    all_cinema = list(zip(items_genre, urls_genre, loc_address_cinema))
    for sort_all_cinema in all_cinema[1:4]:
        await message.answer(
            f'Название: {sort_all_cinema[0]} \nCcылка: {sort_all_cinema[1]}'
            f'\nНаходится: {sort_all_cinema[2]} ', reply_markup=types.ReplyKeyboardRemove()
        )
    await message.answer(f'Добавлена новая функция❗ \nМожно узнать о ближайшей кинотеатре который находится возле тебя🧭'
                         f' \nФункция работает только на телефоне📱',
                         reply_markup=me_location)

    await DataCinema.Loc_cinema.set()


async def location_cinema(message: types.Message, state: FSMContext):
    await loc_cinema(message, state)


async def restaurant(message: types.Message):
    ParserRestaurant(location_city_name)
    all_pizza = list(zip(items_restaurant, urls_restaurant, address_restaurant))
    for sort_all_pizza in all_pizza[1:4]:
        await message.answer(
            f'Название: {sort_all_pizza[0]} \nCcылка: {sort_all_pizza[1]}'
            f'\nНаходится: {sort_all_pizza[2]} ', reply_markup=types.ReplyKeyboardRemove())

    await message.answer(f'Добавлена новая функция❗ \nМожно узнать о ближайшей кофейни которая находится возле тебя🧭'
                         f' \nФункция работает только на телефоне📱',
                         reply_markup=me_location)

    await DataRestaurant.Loc_restaurant.set()


async def location_restaurant(message: types.Message, state: FSMContext):
    await loc_restaurant(message, state)


async def coffee(message: types.Message):
    ParserCoffee(location_city_name)
    all_coffee = list(zip(items_coffee, urls_coffee, address_coffee))
    for sort_all_coffee in all_coffee[1:4]:
        await message.answer(
            f'Название: {sort_all_coffee[0]} \nCcылка: {sort_all_coffee[1]} '
            f'\nАдрес: {sort_all_coffee[2]}', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'Добавлена новая функция❗ \nМожно узнать о ближайшей кофейни которая находится возле тебя🧭'
                         f' \nФункция работает только на телефоне📱',
                         reply_markup=me_location)

    await DataCoffee.Loc_coffee.set()


async def location_coffee(message: types.Message, state: FSMContext):
    await loc_coffee(message, state)


class Other(StatesGroup):
    Other_city = State()


async def other_city(message: types.Message):
    location_city_name.clear()
    items_restaurant.clear()
    urls_restaurant.clear()
    address_restaurant.clear()
    locations_latitude_and_longitude_restaurant.clear()

    items_coffee.clear()
    urls_coffee.clear()
    address_coffee.clear()
    locations_latitude_and_longitude.clear()

    await Other.Other_city.set()

    await message.answer('В каком городе вы хотите посмотреть развлечения🎬☕🍕', reply_markup=user_kb)


async def new_city(message: types.Message, state: FSMContext):
    await rename_leisure_city(message, state)


async def info_game(message: types.Message, state: FSMContext):
    global number, count_of_attempts

    async with state.proxy() as data:
        data["answer2"] = count_of_attempts

    await state.finish()

    try:
        if int(message.text) == number:
            await message.answer(f'Вы угадали!🎉\nКоличество попыток: {count_of_attempts}', reply_markup=house_or_street)
            restart_game = count_of_attempts - 1
            count_of_attempts -= restart_game
            number = random.randint(1, 20)

            await message.answer(f'Любишь игры и хочешь поиграть в другие мини-игры❓ \nУ нас есть бот "Mini Game" '
                                 f'который предложит вам различные мини-игры🎲🎰🕹', reply_markup=bot_mini_game)

        elif int(message.text) < number:
            await message.answer(f'Попробуйте ещё раз🙃 \nЗагаданное число больше')
            count_of_attempts += 1
            await game(message)

        elif int(message.text) > number:
            await message.answer(f'Попробуйте ещё раз🙃 \nЗагаданное число меньше')
            count_of_attempts += 1
            await game(message)

    except ValueError:
        if len(message.text.encode('utf-8', 'ignore')) == 41:
            await state.finish()
            await message.answer('секунду⏱', reply_markup=house_or_street)

        else:
            await message.answer(f'Ошибка❗\nДанные должны иметь числовой тип')
            await game(message)


async def send_reminder():
    try:
        all_info = database.select_all_users()  # Получаю всю информацию с бд
        for all_user in range(len(all_info)):  # Раскрываю список
            id_user = all_info[all_user][0]  # Получаю все id
            full_name = all_info[all_user][1]  # Получаю имя пользователя

            try:
                await bot.send_message(
                    chat_id=id_user, text=f'Привет {full_name}, Есть предложение как можно провести день😉',
                    reply_markup=house_or_street)

            except BotBlocked:
                database.delete_user_main_table(int(id_user))

    except Exception as ex:
        logging.error(repr(ex))


async def scheduler():
    # aioschedule.every().day.at('3:40').do(send_reminder)
    # aioschedule.every(15).seconds.do(send_reminder)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())
