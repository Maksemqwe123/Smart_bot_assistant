import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import time

from New_life_db_work.config import *

connection = psycopg2.connect(
    user=user,
    password=password,
    host=host,
    database='bot_users'
)

print('Выполнено подключение к бд')
print('Информация о сервере бд')
print(connection.get_dsn_parameters(), '\n')

# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()

create_table_query = '''CREATE TABLE IF NOT EXISTS "new_table_stock_pm" (
                        NAME_STOCK TEXT PRIMARY KEY NOT NULL,
                        STOCK TEXT NOT NULL UNIQUE)'''  # Создание таблицы если её нету

cursor.execute(create_table_query)
connection.commit()
print('Таблица успешно создана в бд')

insert_query = '''INSERT INTO "new_table_stock_pm" (NAME_STOCK, STOCK) VALUES (%s, %s)'''  # Вставка значений

insert_tuple = ('Close', '123.8436464')  # указание этих значений
cursor.execute(insert_query, insert_tuple)
connection.commit()
print('Дабавлены новые значение в бд')

update_query = """Update new_table_stock_pm set stock = '4531.3453556' where name_stock = 'Close'"""  # Обновление значений
cursor.execute(update_query)
connection.commit()
print('Обновление значений в бд')

output_values = """SELECT * from new_table_stock_pm"""
cursor.execute(output_values)
print(cursor.fetchall())
print('Вывод значений из бд')

cursor.close()
connection.close()
print('Подключение закрыто')
