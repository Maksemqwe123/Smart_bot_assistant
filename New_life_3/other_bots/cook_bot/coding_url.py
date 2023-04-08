# -*- coding: utf-8 -*-

import urllib.request

import chardet
import urllib.parse  # free = urllib.request.urlopen('https://www.russianfood.com/')
#
text = 'CF%E8%F0%EE%E3%E8&tag_tree%5B1%5D%5B%5D'
# print(chardet.detect(free.read())['encoding'])
slovo = 'пироги'
text_1 = {'title': 'Пироги'}
# with open('text.txt', 'rb') as f:
#     for file in f:
#         print(chardet.detect(f.readline())['encoding'])
#
#         print(file)

# text_1251 = (slovo.encode('utf-8').decode('ascii'))
# print(text_1251)

# print(text_1251.encode('windows-1251').decode('utf-8'))
# udata = slovo.encode('utf-8').decode('utf-8')
# BBB = u' '.join((text, ''))
# BBB_1 = BBB.encode('ascii')
# BBB_2 = unquote(BBB)
# print(BBB_2)

safe_string = urllib.parse.quote_plus('Пироги')
print(safe_string)
from bs4 import UnicodeDammit

with open('text.txt', 'rb') as f:
    content = f.read()

suggestion = UnicodeDammit(content)
print(suggestion.original_encoding)


#
# from bs4 import BeautifulSoup
# try:
#     from urllib import unquote
# except ImportError:
#     from urllib.parse import unquote
#
# soup = BeautifulSoup(unquote(text), 'html.parser')  # consider installing lxml instead
# text_1 = soup.get_text('\n', strip=True)  # put newlines between sections
# print(text_1)
