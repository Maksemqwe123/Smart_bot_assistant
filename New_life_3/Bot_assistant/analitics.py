# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

from New_life_3.Bot_assistant.db_bots.postgresql_db import *

home_films_list = []
home_pizza_list = []
home_books_list = []
home_cook_list = []
home_game_list = []

street_cinema_list = []
street_restaurant_list = []
street_coffee_list = []
street_weather_list = []


db = MyPostgres()
home_analytics = db.select_analytics_home()

street_analytics = db.select_analytics_street()

for i in home_analytics:
    try:
        if not i[2] is None:
            home_films_list.append(i[2])

        if not i[3] is None:
            home_pizza_list.append(i[3])

        if not i[4] is None:
            home_books_list.append(i[4])

        if not i[5] is None:
            home_cook_list.append(i[5])

        if not i[6] is None:
            home_game_list.append(i[6])

    except UnicodeEncodeError:
        print('у какого-то смайлик')


for i in street_analytics:
    try:
        if not i[2] is None:
            street_cinema_list.append(i[2])

        if not i[3] is None:
            street_restaurant_list.append(i[3])

        if not i[4] is None:
            street_coffee_list.append(i[4])

        if not i[5] is None:
            street_weather_list.append(i[5])

    except UnicodeEncodeError:
        print('у какого-то смайлик')


sum_home_films = sum(home_films_list)
sum_home_pizza = sum(home_pizza_list)
sum_home_books = sum(home_books_list)
sum_home_cook = sum(home_cook_list)
sum_home_game = sum(home_game_list)

sum_street_cinema = sum(street_cinema_list)
sum_street_restaurant = sum(street_restaurant_list)
sum_street_coffee = sum(street_coffee_list)
sum_street_weather = sum(street_weather_list)

x_list = ['Films', 'Pizza', 'Books', 'Cook', 'Game']

street_list = ['Cinema', 'Restaurant', 'Coffee', 'Weather']


plt.figure()
plt.subplot(1, 2, 1)

plt.title('Развлечения дома')
plt.ylabel('Самая часто используемая функция')
plt.xlabel('За 36 часов')

plt.bar(x_list[0], sum_home_films, label='Films')
plt.bar(x_list[1], sum_home_pizza, label='Pizza')
plt.bar(x_list[2], sum_home_books, label='Books')
plt.bar(x_list[3], sum_home_cook, label='Cook')
plt.bar(x_list[4], sum_home_game, label='Game')
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Развлечения на улице')
plt.xlabel('За 36 часов')


plt.bar(street_list[0], sum_street_cinema, label='Cinema')
plt.bar(street_list[1], sum_street_restaurant, label='Restaurant')
plt.bar(street_list[2], sum_street_coffee, label='Coffee')
plt.bar(street_list[3], sum_street_weather, label='Weather')
plt.legend()

plt.show()

plt.figure()
plt.subplot(1, 2, 1)
plt.title('Развлечения дома')

plt.xlabel('За 36 часов')
y = np.array([sum_home_films, sum_home_pizza, sum_home_books, sum_home_cook, sum_home_game])
plt.pie(y, labels=x_list)
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Развлечения на улице')
plt.xlabel('За 36 часов')
x = np.array([sum_street_cinema, sum_street_restaurant, sum_street_coffee, sum_street_weather])
plt.pie(x, labels=street_list)
plt.legend()

plt.show()
