import psycopg2

host = '185.49.68.147'
user = 'postgres'
password = 'fge38Ko2Ebns'
db_name = 'assistant'

connection = psycopg2.connect(
    user=user,
    password=password,
    host=host,
    database=db_name
)
