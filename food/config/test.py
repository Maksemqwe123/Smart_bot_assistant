import configparser

config = configparser.ConfigParser()
config.read(r'bot_config.ini')

print(
    list(config['bot']['test'])
)

""""
{'bot': {'token': '5587641606:AAGVMc75T2zaq_GovxKy0nn8wiKFAKBbOvg', 'admin_id': '123'}}
"""

a = list()
print(type(a))
