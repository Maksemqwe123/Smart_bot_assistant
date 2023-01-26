# from telethon import TelegramClient, sync, events
#
# api_id = 19863647
# api_hash = 'f85fc6d1c6baa9922236b5f30fe2294c'
#
# client = TelegramClient('session_name', api_id, api_hash)
#
# @client.on(events.NewMessage(chats=('chat_name')))
# async def normal_handler(event):
# #    print(event.message)
#     print(event.message.to_dict()['message'])
#
# client.start()
# # print(client.get_me())
# #
# # client.send_message('Mrrejaf', 'Hello! Talking to you from Telethon')
# # print(all('chats name'))
# # for dialog in client.iter_dialogs():
# #     print(dialog.title)
#
# client.run_until_disconnected()
import csv

from aiogram.types import message
# import configparser
# import json
#
# from telethon.sync import TelegramClient
# from telethon import connection
#
# # для корректного переноса времени сообщений в json
# from datetime import date, datetime
#
# # классы для работы с каналами
# from telethon.tl.functions.channels import GetParticipantsRequest
# from telethon.tl.types import ChannelParticipantsSearch
#
# # класс для работы с сообщениями
# from telethon.tl.functions.messages import GetHistoryRequest
#
# # Считываем учетные данные
# config = configparser.ConfigParser()
# config.read("config.ini")
#
# # Присваиваем значения внутренним переменным
# api_id = config['Telegram']['api_id']
# api_hash = config['Telegram']['api_hash']
# username = config['Telegram']['username']
#
# # proxy = (proxy_server, proxy_port, proxy_key)
#
# client = TelegramClient(username, api_id, api_hash,
#     connection=connection.ConnectionTcpMTProxyRandomizedIntermediate)
#
# client.start()
#
#
# async def dump_all_participants(channel):
# 	"""Записывает json-файл с информацией о всех участниках канала/чата"""
# 	offset_user = 0    # номер участника, с которого начинается считывание
# 	limit_user = 100   # максимальное число записей, передаваемых за один раз
#
# 	all_participants = []   # список всех участников канала
# 	filter_user = ChannelParticipantsSearch('')
#
# 	while True:
# 		participants = await client(GetParticipantsRequest(channel,
# 			filter_user, offset_user, limit_user, hash=0))
# 		if not participants.users:
# 			break
# 		all_participants.extend(participants.users)
# 		offset_user += len(participants.users)
#
# 	all_users_details = []   # список словарей с интересующими параметрами участников канала
#
# 	for participant in all_participants:
# 		all_users_details.append({"id": participant.id,
# 			"first_name": participant.first_name,
# 			"last_name": participant.last_name,
# 			"user": participant.username,
# 			"phone": participant.phone,
# 			"is_bot": participant.bot})
#
# 	with open('channel_users.json', 'w', encoding='utf8') as outfile:
# 		json.dump(all_users_details, outfile, ensure_ascii=False)
#
#
# async def dump_all_messages(channel):
# 	"""Записывает json-файл с информацией о всех сообщениях канала/чата"""
# 	offset_msg = 0    # номер записи, с которой начинается считывание
# 	limit_msg = 100   # максимальное число записей, передаваемых за один раз
#
# 	all_messages = []   # список всех сообщений
# 	total_messages = 0
# 	total_count_limit = 0  # поменяйте это значение, если вам нужны не все сообщения
#
# 	class DateTimeEncoder(json.JSONEncoder):
# 		'''Класс для сериализации записи дат в JSON'''
# 		def default(self, o):
# 			if isinstance(o, datetime):
# 				return o.isoformat()
# 			if isinstance(o, bytes):
# 				return list(o)
# 			return json.JSONEncoder.default(self, o)
#
# 	while True:
# 		history = await client(GetHistoryRequest(
# 			peer=channel,
# 			offset_id=offset_msg,
# 			offset_date=None, add_offset=0,
# 			limit=limit_msg, max_id=0, min_id=0,
# 			hash=0))
# 		if not history.messages:
# 			break
# 		messages = history.messages
# 		for message in messages:
# 			all_messages.append(message.to_dict())
# 		offset_msg = messages[len(messages) - 1].id
# 		total_messages = len(all_messages)
# 		if total_count_limit != 0 and total_messages >= total_count_limit:
# 			break
#
# 	with open('channel_messages.json', 'w', encoding='utf8') as outfile:
# 		 json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)
#
#
# async def main():
# 	url = input("Введите ссылку на канал или чат: ")
# 	channel = await client.get_entity(url)
# 	await dump_all_participants(channel)
# 	await dump_all_messages(channel)
#
#
# with client:
# 	client.loop.run_until_complete(main())

from telethon import types
from telethon import TelegramClient, events


api_id = 19863647
api_hash = 'f85fc6d1c6baa9922236b5f30fe2294c'

client = TelegramClient('session_name', api_id=api_id, api_hash=api_hash)
client.start()


@client.on(events.NewMessage(chats=['Makcemjoi', 'u_job', 'myresume_ru', 'scrip_chillzone', 'prbezgranic']))
async def normal_handler(event):
    if isinstance(event.chat, types.Channel):
        username = event.chat.username
        add_chat_name = '@' + str(username)
        print('всё ок')

        with open("chat.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(add_chat_name)
            print('запись готова')
        await client.send_message("https://t.me/Makcemjoi", event.message)

if __name__ == '__main__':
    client.run_until_disconnected()

# from xmlrpc.client import DateTime
# from telethon.sync import TelegramClient
#
# from telethon.tl.functions.messages import GetDialogsRequest
# from telethon.tl.types import InputPeerEmpty
# from telethon.tl.functions.messages import GetHistoryRequest
# from telethon.tl.types import PeerChannel
#
# import csv
#
# from telethon import functions, types
# from telethon.sync import TelegramClient
# from telethon import TelegramClient, sync
# from telethon import TelegramClient, events, sync
#
# api_id = 19863647
# api_hash = "f85fc6d1c6baa9922236b5f30fe2294c"
# phone = "+375292459132"
#
# client = TelegramClient(phone, api_id, api_hash)
#
# client.start()
#
# chats = []
# last_date = None
# chunk_size = 200
# groups = []
# result = client(GetDialogsRequest(
#     offset_date=last_date,
#     offset_id=0,
#     offset_peer=InputPeerEmpty(),
#     limit=chunk_size,
#     hash=0
# ))
# chats.extend(result.chats)
# for chat in chats:
#     try:
#         if chat.megagroup == True:
#             groups.append(chat)
#     except:
#         continue
# print("Выберите группу для парсинга сообщений и членов группы:")
# i = 0
# for g in groups:
#     print(str(i) + "- " + g.title)
#     i += 1
# g_index = input("Введите нужную цифру: ")
#
# api_id = 123456 # ваши данные, брать с my.telegram.org
# api_hash = "ada12245jsfo5o2525o6o36" # ваши данные, брать с my.telegram.org
#
#
# client = TelegramClient("Test", api_id, api_hash) # логинимся
# client.start() # старт клиента
# @client.on(events.NewMessage(chats=["test1", 'test2'])) # список каналов, откуда будем брать посты
# async def normal_handler(event):
#     if isinstance(event.chat, types.Channel):
#         username = event.chat.username
#         rdy = "@" + str(username) # получаем юзернейм канала, откуда забрали пост
#         await client.send_message("https://t.me/joinchat/AAAAAE1t242", rdy) # будет отправлять инфу, о том, с какого канала спизжен пост
#         await client.send_message("https://t.me/joinchat/AAAAAE1t242", event.message) # отправка поста в канал
# client.run_until_disconnected()
#
# print("Сохраняем данные в файл...")
# with open("chats.csv", "w", encoding="UTF-8") as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\n")
#     for message in all_messages:
#         writer.writerow([message])
# print('Парсинг сообщений группы успешно выполнен.')


# import configparser
# import json
#
# from telethon.sync import TelegramClient
# from telethon import connection
#
# # для корректного переноса времени сообщений в json
# from datetime import date, datetime
#
# # классы для работы с каналами
# from telethon.tl.functions.channels import GetParticipantsRequest
# from telethon.tl.types import ChannelParticipantsSearch
#
# # класс для работы с сообщениями
# from telethon.tl.functions.messages import GetHistoryRequest
#
# # Считываем учетные данные
# config = configparser.ConfigParser()
# config.read("config.ini")
#
# # Присваиваем значения внутренним переменным
# api_id = 19863647
# api_hash = 'f85fc6d1c6baa9922236b5f30fe2294c'
#
#
# client = TelegramClient('session_name', api_id, api_hash)
#
# client.start()
#
#
# async def dump_all_participants(channel):
# 	"""Записывает json-файл с информацией о всех участниках канала/чата"""
# 	offset_user = 0    # номер участника, с которого начинается считывание
# 	limit_user = 100   # максимальное число записей, передаваемых за один раз
#
# 	all_participants = []   # список всех участников канала
# 	filter_user = ChannelParticipantsSearch('')
#
# 	while True:
# 		participants = await client(GetParticipantsRequest(channel,
# 			filter_user, offset_user, limit_user, hash=0))
# 		if not participants.users:
# 			break
# 		all_participants.extend(participants.users)
# 		offset_user += len(participants.users)
#
# 	all_users_details = []   # список словарей с интересующими параметрами участников канала
#
# 	for participant in all_participants:
# 		all_users_details.append({"id": participant.id,
# 			"first_name": participant.first_name,
# 			"last_name": participant.last_name,
# 			"user": participant.username,
# 			"phone": participant.phone,
# 			"is_bot": participant.bot})
#
# 	with open('channel_users.json', 'w', encoding='utf8') as outfile:
# 		json.dump(all_users_details, outfile, ensure_ascii=False)
#
#
# async def dump_all_messages(channel):
# 	"""Записывает json-файл с информацией о всех сообщениях канала/чата"""
# 	offset_msg = 0    # номер записи, с которой начинается считывание
# 	limit_msg = 100   # максимальное число записей, передаваемых за один раз
#
# 	all_messages = []   # список всех сообщений
# 	total_messages = 0
# 	total_count_limit = 0  # поменяйте это значение, если вам нужны не все сообщения
#
# 	class DateTimeEncoder(json.JSONEncoder):
# 		'''Класс для сериализации записи дат в JSON'''
# 		def default(self, o):
# 			if isinstance(o, datetime):
# 				return o.isoformat()
# 			if isinstance(o, bytes):
# 				return list(o)
# 			return json.JSONEncoder.default(self, o)
#
# 	while True:
# 		history = await client(GetHistoryRequest(
# 			peer=channel,
# 			offset_id=offset_msg,
# 			offset_date=None, add_offset=0,
# 			limit=limit_msg, max_id=0, min_id=0,
# 			hash=0))
# 		if not history.messages:
# 			break
# 		messages = history.messages
# 		for message in messages:
# 			all_messages.append(message.to_dict())
# 		offset_msg = messages[len(messages) - 1].id
# 		total_messages = len(all_messages)
# 		if total_count_limit != 0 and total_messages >= total_count_limit:
# 			break
#
# 	with open('channel_messages.json', 'w', encoding='utf8') as outfile:
# 		 json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)
#
#
# async def main():
# 	url = input("Введите ссылку на канал или чат: ")
# 	channel = await client.get_entity(url)
# 	await dump_all_participants(channel)
# 	await dump_all_messages(channel)
#
#
# with client:
# 	client.loop.run_until_complete(main())

# import json
# from telegram import Telegram
# import plotly.graph_objects as go
#
# from telethon import TelegramClient, sync, events
#
# api_id = 19863647
# api_hash = 'f85fc6d1c6baa9922236b5f30fe2294c'
#
# client = TelegramClient('session_name', api_id, api_hash)
# client.start()
#
# print('all chats name')
# for dialog in client.iter_dialogs():
#     print(dialog)
#
# param = {
#     'supergroup_id': 118948
# }
#
# result = client.catch_up()
#
#
# import json
# from telegram.client import Telegram
# import plotly.graph_objects as go
# import config
# from datetime import datetime
#
# def unix_date_to_dt(data, date_format):
#     return datetime.fromtimestamp(data).strftime(date_format)
# tg = Telegram(
#     api_id=config.api_id,
#     api_hash=config.api_hash,
#     phone=config.phone,  # you can pass 'bot_token' instead
#     database_encryption_key=config.database_encryption_key,
# )
# chat_id=config.supergroup_id
# supergroup_id=int(str(chat_id)[4:])
# tg.login()