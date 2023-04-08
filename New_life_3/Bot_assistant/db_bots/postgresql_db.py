from New_life_3.Bot_assistant.config_bot.connect_db import connection


class MyPostgres:
    def __init__(self):
        self.connection = connection
        self.cursor = connection.cursor()

        self._create_table()
        self._home_buttons_table()
        self._street_buttons_table()

    def _create_table(self):
        with connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS bot_users (
            USER_ID BIGINT UNIQUE, 
            FULL_NAME TEXT,
            LATITUDE DOUBLE PRECISION,
            LONGITUDE DOUBLE PRECISION,
            CITY VARCHAR(32),
            ENTRY_DATE TIMESTAMP,
            LAST_DATE TIMESTAMP NULL
            );""")

    def _home_buttons_table(self):
        with connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS home_buttons (
            USER_ID BIGINT UNIQUE, 
            FULL_NAME TEXT,
            FILMS INTEGER,
            PIZZA INTEGER,
            BOOKS INTEGER,
            COOK INTEGER,
            GAME INTEGER,
            TODAY_DATE DATE
            );""")

    def _street_buttons_table(self):
        with connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS street_buttons (
            USER_ID BIGINT UNIQUE, 
            FULL_NAME TEXT,
            CINEMA INTEGER,
            RESTAURANT INTEGER,
            COFFEE INTEGER,
            WEATHER INTEGER,
            TODAY_DATE DATE
            );""")

    def insert_table_home_buttons(self, user_id, full_name, today_date):
        with connection:
            self.cursor.execute(
                """INSERT INTO home_buttons (user_id, full_name, today_date) VALUES (%s, %s, %s)""" %
                (user_id, full_name, today_date)
            )

    def insert_table_street_buttons(self, user_id, full_name, today_date):
        with connection:
            self.cursor.execute(
                """INSERT INTO street_buttons (user_id, full_name, today_date) VALUES (%s, %s, %s)""" %
                (user_id, full_name, today_date)
            )

    def update_home_buttons(self, films, pizza, books, cook, game, today_date, user_id):
        with connection:
            self.cursor.execute(
                """UPDATE home_buttons SET films = %s, pizza = %s, books = %s, cook = %s, game = %s, today_date = %s WHERE user_id = %s""" %
                (films, pizza, books, cook, game, today_date, user_id)
            )

    def update_street_buttons(self, cinema, restaurant, coffee, weather, today_date, user_id):
        with connection:
            self.cursor.execute(
                """UPDATE street_buttons SET cinema = %s, restaurant = %s, coffee = %s, weather = %s, today_date = %s WHERE user_id = %s""" %
                (cinema, restaurant, coffee, weather, today_date, user_id)
            )

    def select_user_home_buttons_active(self, user_id):
        with connection:
            self.cursor.execute("""SELECT * FROM home_buttons WHERE user_id = %s""", (user_id, ))
            return self.cursor.fetchall()

    def select_user_home_buttons(self, user_id):
        with connection:
            self.cursor.execute("""SELECT user_id FROM home_buttons WHERE user_id = %s""", (user_id, ))
            return self.cursor.fetchall()

    def select_analytics_home(self):
        with connection:
            self.cursor.execute("""SELECT * FROM home_buttons""")
            return self.cursor.fetchall()

    def select_user_street_buttons_active(self, user_id):
        with connection:
            self.cursor.execute("""SELECT * FROM street_buttons WHERE user_id = %s""", (user_id, ))
            return self.cursor.fetchall()

    def select_user_street_buttons(self, user_id):
        with connection:
            self.cursor.execute("""SELECT user_id FROM street_buttons WHERE user_id = %s""", (user_id, ))
            return self.cursor.fetchall()

    def select_analytics_street(self):
        with connection:
            self.cursor.execute("""SELECT * FROM street_buttons""")
            return self.cursor.fetchall()

    def insert_table_users_date(self, user_id, full_name, entry_date):
        with connection:
            self.cursor.execute("""INSERT INTO bot_users (user_id, full_name, entry_date) 
            VALUES (%s, %s, %s)""", (user_id, full_name, entry_date))

    def insert_geo_date(self, latitude, longitude, city):
        with connection:
            self.cursor.execute(
                """INSERT INTO bot_users (latitude, longitude, city) VALUES (%s, %s, %s)""" % (latitude, longitude, city)
            )

    def select_all_users(self):
        with connection:
            self.cursor.execute("""SELECT * FROM bot_users""")
            return self.cursor.fetchall()

    def number_users(self):
        with connection:
            self.cursor.execute("""SELECT COUNT(user_id) FROM bot_users""")
            return self.cursor.fetchall()

    def select_user(self, user_id):
        with connection:
            self.cursor.execute("""SELECT user_id FROM bot_users WHERE user_id = %s""" % (user_id, ))
            return self.cursor.fetchall()

    def update_table_geo(self, latitude, longitude, city, user_id):
        with connection:
            self.cursor.execute(
                """UPDATE bot_users SET latitude = %s, longitude = %s, city = %s WHERE user_id = %s""",
                (latitude, longitude, city, user_id)
                                )

    def update_table_last_date(self, last_date, user_id):
        with connection:
            self.cursor.execute(
                """UPDATE bot_users SET last_date = %s WHERE user_id = %s""", (last_date, user_id)
            )

    def delete_user_main_table(self, user_id):
        with connection:
            self.cursor.execute("""DELETE FROM bot_users WHERE user_id = %s""", (user_id, ))

    def delete_users_home_buttons_table(self, user_id):
        with connection:
            self.cursor.execute("""DELETE FROM home_buttons WHERE user_id = %s""", (user_id, ))

    def delete_users_street_buttons_table(self, user_id):
        with connection:
            self.cursor.execute("""DELETE FROM street_buttons WHERE user_id = %s""", (user_id, ))

    def delete_all_users(self):
        with connection:
            self.cursor.execute("""TRUNCATE TABLE bot_users""")
