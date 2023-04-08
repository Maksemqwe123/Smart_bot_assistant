# -*- coding: utf-8 -*-

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State

from New_life_3.Bot_assistant.parsers.parser_cinema import *
from New_life_3.Bot_assistant.parsers.parser_restaurant_pizza import *
from New_life_3.Bot_assistant.parsers.parser_coffee import *

from New_life_3.Bot_assistant.buttons_bot.buttons import *

from aiogram import types

from geopy import Nominatim

import logging

from New_life_3.Bot_assistant.db_bots.postgresql_db import MyPostgres

from New_life_3.Bot_assistant.weather_tg_bot import bot


database = MyPostgres()

locations_latitude_and_longitude = []
location_no_duplicates = []

locations_latitude_and_longitude_restaurant = []
location_no_duplicates_restaurant = []

real_location_coffee = []
real_location_restaurant = []
real_location_cinema = []


locations_latitude_and_longitude_cinema = []
location_no_duplicates_cinema = []


class DataCinema(StatesGroup):
    Loc_cinema = State()


class DataRestaurant(StatesGroup):
    Loc_restaurant = State()


class DataCoffee(StatesGroup):
    Loc_coffee = State()


async def loc_cinema(message: types.Message, state: FSMContext):
    geolocator_cinema = Nominatim(user_agent="Cinema")
    for sort_loc_address_cinema in loc_address_cinema:
        geolocation_cinema = geolocator_cinema.geocode(sort_loc_address_cinema, timeout=10)
        if geolocation_cinema is None:
            locations_latitude_and_longitude_cinema.append(None)
        else:
            locations_cinema = geolocation_cinema.latitude, geolocation_cinema.longitude

            locations_latitude_and_longitude_cinema.append(locations_cinema)

    geolocation_no_duplicates_cinema = list(set(locations_latitude_and_longitude_cinema))
    loc_geo_cinema = list(filter(None, geolocation_no_duplicates_cinema))

    if message.location is not None:
        geolocation_me_cinema = (message.location.latitude, message.location.longitude)
        me_loc_name = Nominatim(user_agent='Me_loc')
        me_loc = me_loc_name.reverse(geolocation_me_cinema)
        for add_location_db in geolocation_me_cinema:
            real_location_cinema.append(add_location_db)

        ab_cinema = loc_geo_cinema[:]
        ab_cinema.append(geolocation_me_cinema)
        ab_cinema.sort()

        ab_index_cinema = ab_cinema.index(geolocation_me_cinema) - 1 if ab_cinema.index(
            geolocation_me_cinema) > 0 else 1
        spend_cinema = (ab_cinema[ab_index_cinema])

        await bot.send_location(message.chat.id, spend_cinema[0], spend_cinema[1], reply_markup=help_assistant_street)

        nom = Nominatim(user_agent='Location_cinema')
        location_address = nom.reverse(spend_cinema)

        city_users = (str(me_loc).split(',')[-4]).encode('utf-8').decode('utf-8')

        database.update_table_geo(
            message.location.latitude, message.location.longitude, city_users, message.from_user.id
        )

        logging.info('В бд добавлено новые данные о пользователе')

        await message.answer(f'Находится: {location_address}')

        async with state.proxy() as data:
            data["answer1"] = location_address

        await state.finish()


async def loc_restaurant(message: types.Message, state: FSMContext):
    geolocator_restaurant = Nominatim(user_agent="Restaurant")
    for restaurant_city in address_restaurant:
        geolocation_restaurant = geolocator_restaurant.geocode(restaurant_city, timeout=10)
        if geolocation_restaurant is None:
            locations_latitude_and_longitude_restaurant.append(None)
        else:
            locations_restaurant = geolocation_restaurant.latitude, geolocation_restaurant.longitude

            locations_latitude_and_longitude_restaurant.append(locations_restaurant)

    geolocation_no_duplicates_restaurant = list(set(locations_latitude_and_longitude_restaurant))
    loc_geo_restaurant = list(filter(None, geolocation_no_duplicates_restaurant))

    if message.location is not None:
        geolocation_me_restaurant = (message.location.latitude, message.location.longitude)
        me_loc_name = Nominatim(user_agent='Me_loc')
        me_loc = me_loc_name.reverse(geolocation_me_restaurant)
        for add_location_db in geolocation_me_restaurant:
            real_location_restaurant.append(add_location_db)

        ab_restaurant = loc_geo_restaurant[:]
        ab_restaurant.append(geolocation_me_restaurant)
        ab_restaurant.sort()

        ab_index_restaurant = ab_restaurant.index(geolocation_me_restaurant) - 1 if ab_restaurant.index(
            geolocation_me_restaurant) > 0 else 1

        spend_restaurant = (ab_restaurant[ab_index_restaurant])
        await bot.send_location(message.chat.id, spend_restaurant[0], spend_restaurant[1],
                                reply_markup=help_assistant_street)

        nom = Nominatim(user_agent='Restaurant')
        location_address_restaurant = nom.reverse(spend_restaurant)

        city_users = (str(me_loc).split(',')[-4])

        database.update_table_geo(
            message.location.latitude, message.location.longitude, city_users, message.from_user.id
        )
        logging.info('В бд добавлено новые данные о пользователе')

        await message.answer(f'Находится: {location_address_restaurant}')

        async with state.proxy() as data:
            data["answer3"] = location_address_restaurant

        await state.finish()


async def loc_coffee(message: types.Message, state: FSMContext):
    geolocator = Nominatim(user_agent="Location_coffee")
    for coffee_city in address_coffee:
        geolocation_coffee = geolocator.geocode(coffee_city, timeout=10)
        if geolocation_coffee is None:
            locations_latitude_and_longitude.append(None)
        else:
            locations = geolocation_coffee.latitude, geolocation_coffee.longitude

            locations_latitude_and_longitude.append(locations)

    geolocation_no_duplicates = list(set(locations_latitude_and_longitude))
    loc_geo = list(filter(None, geolocation_no_duplicates))

    if message.location is not None:
        geolocation_me = (message.location.latitude, message.location.longitude)
        me_loc_name = Nominatim(user_agent='Me_loc')
        me_loc = me_loc_name.reverse(geolocation_me)
        for add_location_db in geolocation_me:
            real_location_coffee.append(add_location_db)

        ab = loc_geo[:]
        ab.append(geolocation_me)
        ab.sort()
        ab_index = ab.index(geolocation_me) - 1 if ab.index(geolocation_me) > 0 else 1
        spend = (ab[ab_index])
        await bot.send_location(message.chat.id, spend[0], spend[1], reply_markup=help_assistant_street)

        nom = Nominatim(user_agent='Location_coffee')
        location_address = nom.reverse(spend)
        city_users = (str(me_loc).split(',')[-4])

        database.update_table_geo(
            message.location.latitude, message.location.longitude, city_users, message.from_user.id
        )
        logging.info('В бд добавлено новые данные о пользователе')

        await message.answer(f'Находится: {location_address}')

        async with state.proxy() as data:
            data["answer2"] = location_address

        await state.finish()
