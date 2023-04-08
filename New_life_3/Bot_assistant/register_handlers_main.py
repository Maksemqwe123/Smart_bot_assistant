# -*- coding: utf-8 -*-
from aiogram.dispatcher.filters import Text

from New_life_3.Bot_assistant.handler import *


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_message, commands='start', state='*')
    dp.register_message_handler(cmd_cancel, commands='cancel', state='*')
    dp.register_message_handler(send_all, commands='sendall', state='*')
    dp.register_message_handler(info, commands='info_db', state='*')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(select_user, Text(equals='Просмотреть всех пользователей', ignore_case=True))
    dp.register_message_handler(delete_all_users, Text(equals='Удалить всех пользователей', ignore_case=True))
    dp.register_message_handler(delete_and_no, state=DeleteAllUsers.are_you_sure)
    dp.register_message_handler(select_number_users, Text(equals='Сколько пользователей?', ignore_case=True))
    dp.register_message_handler(delete_one_user, Text(equals='Удалить пользователя', ignore_case=True))
    dp.register_message_handler(id_user_delete, state=DeleteOneUsers.one_user)


def register_handlers_weather_house_street(dp: Dispatcher):
    dp.register_message_handler(today, state=WeatherToday.weather_today_city)
    dp.register_message_handler(leisure, Text(equals='Что можно поделать дома ?🏠', ignore_case=True))
    dp.register_message_handler(back_street, Text(equals='Вернуться назад⬅️', ignore_case=True), state='*')
    dp.register_message_handler(street, Text(equals='Как можно провести время на улице ?🚶‍♂🚶‍♀', ignore_case=True),
                                state=None)
    dp.register_message_handler(leisure_city, state=DataFilms.Film_cimema)


def register_handlers_back_game(dp: Dispatcher):
    dp.register_message_handler(back_weather, Text(equals='Узнать погоду в городе🌤', ignore_case=True))
    dp.register_message_handler(game, Text(equals='Сыграть в игру🔮', ignore_case=True), state=None)
    dp.register_message_handler(info_game, state=DataGame.Offer_game)
    dp.register_message_handler(exit_menu, Text(equals='Выйти в главное меню📋', ignore_case=True), state='*')


def register_handlers_eats_drinks(dp: Dispatcher):
    dp.register_message_handler(pizza, Text(equals='Что за акция на пиццу?🍕', ignore_case=True))
    dp.register_message_handler(cook, Text(equals='Какой десерт можно легко приготовить?🧁', ignore_case=True))
    dp.register_message_handler(restaurant, Text(equals='Куда можно сходить поесть ?🍽', ignore_case=True), state=None)
    dp.register_message_handler(coffee, Text(equals='Где и какой кофе можно выпить?☕️', ignore_case=True), state=None)


def register_handlers_film_book(dp: Dispatcher):
    dp.register_message_handler(kinogo, Text(equals='Какой фильм можно посмотреть?🎬', ignore_case=True))
    dp.register_message_handler(book, Text(equals='Какую книгу можно почитать?📚', ignore_case=True))
    dp.register_message_handler(cinema, Text(equals='На какой фильм в кинотеатр можно сходить ?🎬', ignore_case=True),
                                state=None)


def register_handlers_location_new_city(dp: Dispatcher):
    dp.register_message_handler(location_cinema, content_types=["location"], state=DataCinema.Loc_cinema)
    dp.register_message_handler(location_restaurant, content_types=["location"], state=DataRestaurant.Loc_restaurant)
    dp.register_message_handler(location_coffee, content_types=["location"], state=DataCoffee.Loc_coffee)
    dp.register_message_handler(other_city, Text(equals='Выбрать другой город🏙️🌃', ignore_case=True), state=None)
    dp.register_message_handler(new_city, state=Other.Other_city)
