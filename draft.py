import translators as ts
from spellchecker import SpellChecker as sp
import pandas as pd
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from unitsnet_py import Length, LengthUnits, Mass, MassUnits
import re
from bs4 import BeautifulSoup as bs
import requests
from currency_converter import CurrencyConverter as cc
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
from random import choice


# translator = ts

# spell = sp(language='ru')
# word = 'Привет'
# if spell.correction(word) == word:
#     x = ts.translate_text(word, from_language='ru', to_language='fr')
#
# else:
#     print('неверно')
#     print(spell.candidates(word))

# word = 'Привет'
#
# words = {
#                 'ru': word.capitalize(),
#                 'en': ts.translate_text(word, from_language='ru', to_language='en'),
#                 'fr': ts.translate_text(word, from_language='ru', to_language='fr')
#             }
#
# print(words.keys())


# file = open('results/words.csv', 'r')
# lines = [x.split(',') for x in file.read().splitlines()]
# print(lines)

# a = pd.read_html('results/table_translate.html')
# print(a)

# a = open('results/table_translate.html', mode='r')
# a = a.readlines()
# print(a)

# code = 'import translators from spellchecker import SpellChecker import pandas as pd class Translate: def __init__(self, user_word: str): self.spell = SpellChecker(language="ru") self.translator = translators self.word = user_word'
# code = 'def check_form(self): if len(self.word) == 0: return "Поле ввода пустое. Введите слово" return self.check_spelling()'
# code = 'def check_spelling(self): if self.spell.correction(self.word) == self.word: return self.translate() return self.error()'
# code = 'def translate(self): if self.read_csv(): return self.to_csv([self.word.capitalize(), self.translator.translate_text(self.word, from_language="ru", to_language="en").capitalize(), self.translator.translate_text(self.word, from_language="ru", to_language="fr").capitalize()])else:return "Данное слово уже существует."'
# code = 'def read_csv(self) -> bool: csv = pd.read_csv("results/words.csv")["Russian"].to_dict() for index in csv: if self.word.capitalize() == csv[index]: return False continue return True'
# code = 'def to_csv(self, words_list: list): columns = ["Russian", "English", "French"] df = pd.DataFrame([words_list], columns=columns) df.to_csv("results/words.csv", mode="a", header=False, index=False) return self.read_csv_to_html()'
# code = '@staticmethod def read_csv_to_html() -> list: file = open("results/words.csv", 'r') lines = [x.split(",") for x in file.read().splitlines()[1:]] return lines'
# code = 'def error(self) -> str: try: mistakes = ", ".join([mistake.capitalize() for mistake in self.spell.candidates(self.word)]) return f"Ошибка в написании. Возможно, вы имели ввиду одно из следующих слов: {mistakes}" except TypeError: return "Такого слова не предусмотрено."'
# print(highlight(code, PythonLexer(), HtmlFormatter(noclasses=True, style='solarized-light', cssstyles='border-radius: 8px;border: 1px solid grey;padding: 15px')))

# first = "6'"
# second = ' 4"'
#
# result = f"{re.findall(r'[1-9]+', first + second)[0]}.{re.findall(r'[1-9]+', first + second)[1]}"
# feet = Length(float(result), LengthUnits.Foot).centimeters
# print(feet)

# lbs =
# print(lbs)

# url = 'https://www.espn.com'
# response = requests.get(url + '/nba/teams')
#
# response_body = bs(response.content, 'html.parser')
# needed_hrefs = [link["href"] for link in response_body.find('div', {'class': 'layout is-split'}).find_all('a', {'class': 'AnchorLink'}) if 'roster' in link["href"]]
# result_list = []
#
# for href in needed_hrefs:
#     table_rows = bs(requests.get(url + href).content, 'html.parser').find('tbody', {'class': 'Table__TBODY'}).find_all('tr', {'class': 'Table__TR'})
#     for table_row in table_rows:
#         table_datas = table_row.find_all('td', {'class': 'Table__TD'})
#         player_info = {
#             'name': table_datas[1].text,
#             'position': table_datas[2].text,
#             'age': table_datas[3].text,
#             'height': f"{round(Length(float('.'.join(re.findall(r'[1-9]+', table_datas[4].text))), LengthUnits.Foot).centimeters)} см",
#             'weight': f"{round(Mass(int(re.findall(r'[1-9]+', table_datas[5].text)[0]), MassUnits.Pound).kilograms)} кг",
#             'college': table_datas[6].text,
#             'salary': table_datas[7].text
#         }
#         result_list.append(player_info)
#
# print(result_list)
# print(len(result_list))

# salary = '$22,600,000'
# result = f"{''.join(''.join(re.findall(r'[0-9,]+', salary)).split(','))}"
# print(result)

# a = '12345'
# print(a + '')

# value = round(cc(fallback_on_wrong_date=True).convert(4600000, 'USD', 'RUB') / 1000000, 2)
# print(value, 'млн. руб')

# a = ''
# print(a.capitalize())

person = Person(locale=Locale.RU)
phone = person.telephone(mask='+7(9##)-###-##-##')
print(phone)
