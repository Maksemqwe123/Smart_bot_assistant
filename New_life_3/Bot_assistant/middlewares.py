# -*- coding: utf-8 -*-
import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

import time

from New_life_3.Bot_assistant.db_bots.postgresql_db import *

today_date = time.strftime("%Y-%m-%d")

my_db = MyPostgres()


class AccessMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def on_process_message(self, message: types.Message, _):
        strings_date = time.strftime("%Y-%m-%d %H:%M:%S")

        my_db.update_table_last_date("'" + strings_date + "'", message.from_user.id)

        try:
            if len(message.text.encode('utf-8', 'ignore')) == 49:
                if not my_db.select_user_home_buttons(message.from_user.id):
                    my_db.insert_table_home_buttons(message.from_user.id, "'" + message.from_user.full_name + "'", "'" + today_date + "'")

            if len(message.text.encode('utf-8', 'ignore')) == 58:

                films_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][2]
                pizza_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][3]
                books_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][4]
                cook_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][5]
                game_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][6]

                if films_buttons == 0:
                    my_db.update_home_buttons(1, pizza_buttons + 0, books_buttons + 0, cook_buttons + 0, game_buttons + 0, "'" + today_date + "'", message.from_user.id)

                elif films_buttons is None:
                    my_db.update_home_buttons(1, 0, 0, 0, 0, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_home_buttons(films_buttons + 1, pizza_buttons + 0, books_buttons + 0, cook_buttons + 0, game_buttons + 0, "'" + today_date + "'", message.from_user.id)

            elif len(message.text.encode('utf-8', 'ignore')) == 43:

                films_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][2]
                pizza_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][3]
                books_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][4]
                cook_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][5]
                game_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][6]

                if pizza_buttons == 0:
                    my_db.update_home_buttons(films_buttons + 0, 1, books_buttons + 0, cook_buttons + 0, game_buttons + 0, "'" + today_date + "'", message.from_user.id)

                elif pizza_buttons is None:
                    my_db.update_home_buttons(0, 1, 0, 0, 0, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_home_buttons(films_buttons + 0, pizza_buttons + 1, books_buttons + 0, cook_buttons + 0, game_buttons + 0, "'" + today_date + "'", message.from_user.id)

            elif len(message.text.encode('utf-8', 'ignore')) == 54:

                films_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][2]
                pizza_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][3]
                books_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][4]
                cook_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][5]
                game_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][6]

                if books_buttons == 0:
                    my_db.update_home_buttons(films_buttons + 0, pizza_buttons + 0, 1, cook_buttons + 0, game_buttons + 0, "'" + today_date + "'", message.from_user.id)

                elif books_buttons is None:
                    my_db.update_home_buttons(0, 0, 1, 0, 0, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_home_buttons(films_buttons + 0, pizza_buttons + 0, books_buttons + 1, cook_buttons + 0, game_buttons + 0, "'" + today_date + "'", message.from_user.id)

            elif len(message.text.encode('utf-8', 'ignore')) == 73:

                films_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][2]
                pizza_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][3]
                books_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][4]
                cook_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][5]
                game_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][6]

                if cook_buttons == 0:
                    my_db.update_home_buttons(films_buttons + 0, pizza_buttons + 0, books_buttons + 0, 1, game_buttons + 0, "'" + today_date + "'", message.from_user.id)

                elif cook_buttons is None:
                    my_db.update_home_buttons(0, 0, 0, 1, 0, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_home_buttons(films_buttons + 0, pizza_buttons + 0, books_buttons + 0, cook_buttons + 1, game_buttons + 0, "'" + today_date + "'", message.from_user.id)

            elif len(message.text.encode('utf-8', 'ignore')) == 30:

                films_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][2]
                pizza_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][3]
                books_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][4]
                cook_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][5]
                game_buttons = my_db.select_user_home_buttons_active(message.from_user.id)[0][6]

                if game_buttons == 0:
                    my_db.update_home_buttons(films_buttons + 0, pizza_buttons + 0, books_buttons + 0, cook_buttons + 0, 1, "'" + today_date + "'", message.from_user.id)

                elif game_buttons is None:
                    my_db.update_home_buttons(0, 0, 0, 0, 1, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_home_buttons(films_buttons + 0, pizza_buttons + 0, books_buttons + 0, cook_buttons + 0, game_buttons + 1, "'" + today_date + "'", message.from_user.id)

            if len(message.text.encode('utf-8', 'ignore')) == 83:
                if not my_db.select_user_street_buttons(message.from_user.id):
                    my_db.insert_table_street_buttons(message.from_user.id, "'" + message.from_user.full_name + "'", "'" + today_date + "'")

            elif len(message.text.encode('utf-8', 'ignore')) == 80:

                cinema_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][2]
                restaurant_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][3]
                coffee_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][4]
                weather_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][5]

                if cinema_buttons == 0:
                    my_db.update_street_buttons(1, restaurant_buttons + 0, coffee_buttons + 0, weather_buttons + 0, "'" + today_date + "'", message.from_user.id)

                elif cinema_buttons is None:
                    my_db.update_street_buttons(1, 0, 0, 0, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_street_buttons(cinema_buttons + 1, restaurant_buttons + 0, coffee_buttons + 0, weather_buttons + 0, "'" + today_date + "'", message.from_user.id)

            elif len(message.text.encode('utf-8', 'ignore')) == 53:

                cinema_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][2]
                restaurant_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][3]
                coffee_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][4]
                weather_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][5]

                if restaurant_buttons == 0:
                    my_db.update_street_buttons(cinema_buttons + 0, 1, coffee_buttons + 0, weather_buttons + 0, "'" + today_date + "'", message.from_user.id)

                elif restaurant_buttons is None:
                    my_db.update_street_buttons(0, 1, 0, 0, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_street_buttons(cinema_buttons + 0, restaurant_buttons + 1, coffee_buttons + 0, weather_buttons + 0, "'" + today_date + "'", message.from_user.id)

            elif len(message.text.encode('utf-8', 'ignore')) == 60:

                cinema_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][2]
                restaurant_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][3]
                coffee_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][4]
                weather_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][5]

                if coffee_buttons == 0:
                    my_db.update_street_buttons(cinema_buttons + 0, restaurant_buttons + 0, 1, weather_buttons + 0, "'" + today_date + "'", message.from_user.id)

                elif coffee_buttons is None:
                    my_db.update_street_buttons(0, 0, 1, 0, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_street_buttons(cinema_buttons + 0, restaurant_buttons + 0, coffee_buttons + 1, weather_buttons + 0, "'" + today_date + "'", message.from_user.id)

            elif len(message.text.encode('utf-8', 'ignore')) == 45:

                cinema_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][2]
                restaurant_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][3]
                coffee_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][4]
                weather_buttons = my_db.select_user_street_buttons_active(message.from_user.id)[0][5]

                if weather_buttons == 0:
                    my_db.update_street_buttons(cinema_buttons + 0, restaurant_buttons + 0, coffee_buttons + 0, 1, "'" + today_date + "'", message.from_user.id)

                elif weather_buttons is None:
                    my_db.update_street_buttons(0, 0, 0, 1, "'" + today_date + "'", message.from_user.id)

                else:
                    my_db.update_street_buttons(cinema_buttons + 0, restaurant_buttons + 0, coffee_buttons + 0, weather_buttons + 1, "'" + today_date + "'", message.from_user.id)

        except:
            logging.info('Эта функция не отслеживается')
