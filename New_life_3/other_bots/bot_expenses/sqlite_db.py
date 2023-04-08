import sqlite3 as sq


class DataBase:
    def __init__(self, db_file: str):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()

        self._create_table_users()

    def _create_table_users(self):
        with self.connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            users_id INTEGER,
            user_name TEXT,
            sum_budget INTEGER,
            date_save_budget TEXT,
            today_date TEXT
            """)

    def insert_table(self, users_id, user_name):
        with self.connection:
            self.cursor.execute("""INSERT INTO users (users_id, user_name) VALUES (?, ?)""", (users_id, user_name))

    def update_info_budget(self, sum_budget, user_id):
        with self.connection:
            self.cursor.execute("""UPDATE users SET sum_budget = ? WHERE user_id = ?""", (sum_budget, user_id))

    def update_date_save_budget(self, date_save_budget, user_id):
        with self.connection:
            self.cursor.execute("""UPDATE users SET date_save_budget = ? WHERE user_id = ?""", (date_save_budget, user_id))

    def select_table(self):
        with self.connection:
            self.cursor.execute("""SELECT * FROM users""")

    def delete_table(self, sum_budget, date_save_budget, user_name):
        with self.connection:
            self.cursor.execute("""DELETE sum_budget, date_save_budget FROM users WHERE user_name = ?""", (sum_budget, date_save_budget, user_name))
