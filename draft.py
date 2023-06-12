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
import csv

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
# lines = [x.split('\n') for x in file.read().splitlines()]
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

# person = Person(locale=Locale.RU)
# phone = person.telephone(mask='+7(9##)-###-##-##')
# print(phone)
# code = "from bs4 import BeautifulSoup as bs from unitsnet_py import Length, LengthUnits, Mass, MassUnits import requests import pandas as pd import re from currency_converter import CurrencyConverter as cc class Players: def __init__(self, player_info: dict): self.full_name = \ player_info['player_last_name'].capitalize() + ' ' + \ player_info['player_first_name'].capitalize() + ' ' + \ player_info['player_surname'].capitalize() self.position = player_info['player_role'].upper() self.age = player_info['player_age'] self.height = player_info['player_height'] self.weight = player_info['player_weight'] self.team = player_info['player_team'] self.education = player_info['player_education'] self.salary = player_info['player_salary']"
# code = "@staticmethod def parse_site(): url: str = 'https://www.espn.com' response = requests.get(url + '/nba/teams') response_body = bs(response.content, 'html.parser') needed_hrefs: list = [ link['href'] for link in response_body .find('div', {'class': 'layout is-split'}) .find_all('a', {'class': 'AnchorLink'}) if 'roster' in link['href'] ] columns: list = ['Name', 'Position', 'Age', 'Height', 'Weight', 'Team', 'College', 'Salary'] df_w = pd.DataFrame([columns], columns=columns) df_w.to_csv('results/players.csv', mode='w', index=False, header=False) for href in needed_hrefs: table_rows = bs(requests.get(url + href).content, 'html.parser')\ .find('tbody', {'class': 'Table__TBODY'})\ .find_all('tr', {'class': 'Table__TR'}) for table_row in table_rows: table_datas: list = table_row.find_all('td', {'class': 'Table__TD'}) player_name: str = ' '.join(re.findall('[A-z.]+', table_datas[1].text)) player_role: str = table_datas[2].text player_age: str = table_datas[3].text player_height: int = round(Length(float('.'.join(re.findall(r'[1-9]+', table_datas[4].text))), LengthUnits.Foot).centimeters) player_weight: int = round(Mass(int(re.findall(r'[0-9]+', table_datas[5].text)[0]), MassUnits.Pound).kilograms) player_team: str = ' '.join( [ team.text for team in bs(requests.get(url + href).content, 'html.parser') .find('main', {'id': 'fittPageContainer'}) .find('h1', {'class': 'ClubhouseHeader__Name'}) .find_all('span', {'class': 'db'}) ] ) player_info_unknown: str = 'Неизвестно' player_education: str = player_info_unknown if re.search(r'-', table_datas[6].text) else table_datas[6].text player_salary_usd: str = ''.join(''.join(re.findall(r'[0-9,]+', table_datas[7].text)).split(',')) player_salary: str = player_info_unknown \ if re.search(r'-', table_datas[7].text) \ else round(cc(fallback_on_wrong_date=True).convert(int(player_salary_usd), 'USD', 'RUB') / 1000000) player_info_list: list = [ player_name, player_role, player_age, player_height, player_weight, player_team, player_education, player_salary ] df_a = pd.DataFrame([player_info_list], columns=columns) df_a.to_csv('results/players.csv', mode='a', index=False, header=False)"
# code = "def add_player_to_csv(self): columns: list = ['Name', 'Position', 'Age', 'Height', 'Weight', 'Team', 'College', 'Salary'] new_player_info: list = [ self.full_name, self.position, self.age, self.height, self.weight, self.team, self.education, self.salary ] checked_player_info = self.check_unknown_fields(new_player_info) df_a = pd.DataFrame([checked_player_info], columns=columns) df_a.to_csv('results/players.csv', mode='a', index=False, header=False) return self.read_csv_to_html()"
# code = "@staticmethod def check_unknown_fields(player_info: list): for index, field in enumerate(player_info): if field == '' or len(field) == 2: player_info[index] = 'Неизвестно' continue return player_info"
# code = "@staticmethod def read_csv_to_html() -> list: file = open('results/players.csv', 'r') lines = [x.split(',') for x in file.read().splitlines()[1:]] return lines"
# print(highlight(code, PythonLexer(), HtmlFormatter(noclasses=True, style='solarized-light', cssstyles='border-radius: 8px;border: 1px solid grey;padding: 15px')))

# a = set()
# a.add(1)
# a.add(1)
# print(a)

# a = pd.read_csv('results/books.csv')
# for i in range(10000):
#     try:
#         print(a['Year'][i])
#     except KeyError:
#         break

# def search(word: str) -> str or list:
#     result = []
#     with open('results/players.csv') as players:
#         players_rows: list = [x.split('\n') for x in players.read().splitlines()[1:]]
#         players_pandas: list = pd.read_csv('results/players.csv')
#         for title in players_pandas:
#             if title not in ['Position', 'Age', 'Height', 'Weight', 'Salary']:
#                 for index, row in enumerate(players_pandas[title]):
#                     if word in str(row):
#                         needed_row = ' ,'.join(players_rows[index]).split(',')
#                         result.append(needed_row)
#                     continue
#             continue
#     print(result)
#     return result if len(result) > 0 else 'Совпадений не найдено.'
#
#
# search('Stephen')

# def search(word: str) -> str or list:
#     result = []
#     with open('results/words.csv') as words:
#         words_rows: list = [x.split('\n') for x in words.read().splitlines()[1:]]
#         words_pandas: list = pd.read_csv('results/words.csv')
#         for title in words_pandas:
#             for index, row in enumerate(words_pandas[title]):
#                 if word in row:
#                     needed_row = ' ,'.join(words_rows[index]).split(',')
#                     result.append(needed_row)
#                 continue
#     return result if len(result) > 0 else 'Совпадений не найдено.'
#
#
# print(search('Бросок'))

# def search(word: str) -> str or dict:
#     result = {
#         'Title': [],
#         'Author': [],
#         'Genre': [],
#         'Year': [],
#         'Publisher': [],
#         'Summary': []
#     }
#     with open('results/books.csv') as _:
#         books_pandas: list = pd.read_csv('results/books.csv')
#         for title in books_pandas:
#             if title not in ['Year', 'Summary']:
#                 for index, row in enumerate(books_pandas[title]):
#                     if word in str(row):
#                         result['Title'].append(books_pandas['Title'][index])
#                         result['Author'].append(books_pandas['Author'][index])
#                         result['Genre'].append(books_pandas['Genre'][index])
#                         result['Year'].append(books_pandas['Year'][index])
#                         result['Publisher'].append(books_pandas['Publisher'][index])
#                         result['Summary'].append(books_pandas['Summary'][index])
#                     continue
#             continue
#     return result if len(result['Title']) > 0 else 'Совпадений не найдено.'
#
#
# print(search('Дракон'))


# file = open('results/employees.csv', 'r')
# lines: list = [x.split(',') for x in file.read().splitlines()[1:]]
# print(lines)
# for line in lines:
#     print(line)

# table = pd.read_csv('results/players.csv')
# table.drop([513, 514, 515], inplace=True)
# print(table)


# delete_id = 1
# table = pd.read_csv('results/players.csv')
# table.drop(delete_id, inplace=True)
# table.to_csv('results/players.csv', mode='w', index=False)


# delete_id = 3
# with open('results/players.csv', 'r') as players_reader:
#     result = []
#     reader = csv.reader(players_reader)
#     for index, row in enumerate(reader):
#         if index != delete_id:
#             result.append(row)
#         continue
#     with open('results/players.csv', 'w') as players_writer:
#         for row in result:
#             csv.writer(players_writer).writerow(row)

# delete_id = 0
# table = pd.read_csv('results/players.csv')
# table = pd.read_csv('draft.csv')
# table.drop(delete_id, inplace=True)
# table.to_csv('draft.csv', index=False, mode='w')

# player_new_info: list = [
#     'full_name', '', 'age', 'height',
#     'weight', 'team', '  ', 'salary'
# ]
# df = pd.read_csv('draft.csv')
# for title in df:
#     for data in player_new_info:
#         df.loc[delete_id, title] = data if data not in ['', '  '] else df.loc[delete_id, title]
# # df.iloc[delete_id] = player_new_info
# print(df.iloc[delete_id])

# field = 'z  '
# a = re.sub(r'\s+', '', field)
# print(f"_{a}_")

# gender: str = choice([Gender.FEMALE, Gender.MALE])
# print(type(gender))

# print(type(pd))
# code = "from bs4 import BeautifulSoup as bs " \
#        "from unitsnet_py import Length, LengthUnits, Mass, MassUnits " \
#        "import requests " \
#        "import pandas as pd " \
#        "import re " \
#        "from currency_converter import CurrencyConverter as cc"
# code = "@staticmethod def parse_site(): result: list = [] url: str = 'https://www.espn.com' response = requests.get(url + '/nba/teams') response_body = bs(response.content, 'html.parser') needed_hrefs: list = [ link['href'] for link in response_body .find('div', {'class': 'layout is-split'}) .find_all('a', {'class': 'AnchorLink'}) if 'roster' in link['href'] ] columns: list = ['Name', 'Position', 'Age', 'Height', 'Weight', 'Team', 'College', 'Salary'] for href in needed_hrefs: table_rows: list = bs(requests.get(url + href).content, 'html.parser') \ .find('tbody', {'class': 'Table__TBODY'}) \ .find_all('tr', {'class': 'Table__TR'}) for table_row in table_rows: table_datas: list = table_row.find_all('td', {'class': 'Table__TD'}) player_name: str = ' '.join(re.findall('[A-z.]+', table_datas[1].text)) player_role: str = table_datas[2].text player_age: str = table_datas[3].text player_height: int = round( Length(float('.'.join(re.findall(r'[1-9]+', table_datas[4].text))), LengthUnits.Foot).centimeters) player_weight: int = round( Mass(int(re.findall(r'[0-9]+', table_datas[5].text)[0]), MassUnits.Pound).kilograms) player_team: str = ' '.join( [ team.text for team in bs(requests.get(url + href).content, 'html.parser') .find('main', {'id': 'fittPageContainer'}) .find('h1', {'class': 'ClubhouseHeader__Name'}) .find_all('span', {'class': 'db'}) ] ) player_info_unknown: str = 'Неизвестно' player_education: str = player_info_unknown if re.search(r'-', table_datas[6].text) else table_datas[ 6].text player_salary_usd: str = ''.join(''.join(re.findall(r'[0-9,]+', table_datas[7].text)).split(',')) player_salary: str = player_info_unknown \ if re.search(r'-', table_datas[7].text) \ else round(cc(fallback_on_wrong_date=True).convert(int(player_salary_usd), 'USD', 'RUB') / 1000000) player_info_list: list = [ player_name, player_role, player_age, player_height, player_weight, player_team, player_education, player_salary ] result.append(player_info_list) df_a = pd.DataFrame(result, columns=columns) df_a.to_csv('results/players.csv', mode='w', index=False)"
# code = "player_education: str = player_info_unknown \ if re.search(r'-', table_datas[6].text) else table_datas[6].text"
# code = "def add_player_to_csv(self): full_name: str = \ self.form_info['player_last_name'].capitalize() + ' ' + \ self.form_info['player_first_name'].capitalize() + ' ' + \ self.form_info['player_surname'].capitalize() position: str = self.form_info['player_role'].upper() age: str = self.form_info['player_age'] height: str = self.form_info['player_height'] weight: str = self.form_info['player_weight'] team: str = self.form_info['player_team'] education: str = self.form_info['player_education'] salary: str = self.form_info['player_salary'] columns: list = ['Name', 'Position', 'Age', 'Height', 'Weight', 'Team', 'College', 'Salary'] new_player_info: list = [ full_name, position, age, height, weight, team, education, salary ] checked_player_info: list = self.check_unknown_fields(new_player_info) df_a = pd.DataFrame([checked_player_info], columns=columns) df_a.to_csv('results/players.csv', mode='a', index=False, header=False) return self.read_csv_to_html()"
# code = "@staticmethod def check_unknown_fields(player_info: list) -> list: for index, field in enumerate(player_info): if len(re.sub(r'\s+', '', field)) == 0: player_info[index] = 'Неизвестно' continue return player_info"
# code = "@staticmethod def read_csv_to_html() -> list: file = open('results/players.csv', 'r') lines: list = [x.split(',') for x in file.read().splitlines()[1:]] return lines"
# code = "players_rows: list = [x.split('\') for x in players.read().splitlines()[1:]] players_pandas: list = pd.read_csv('results/players.csv') for title in players_pandas: if title not in ['Position', 'Age', 'Height', 'Weight', 'Salary']: for index, row in enumerate(players_pandas[title]): if word in str(row): needed_row: str = ' ,'.join(players_rows[index]).split(',') result.append(needed_row) continue continue return result if len(result) > 0 else 'Совпадений не найдено.' return 'Вы ничего не ввели, чтобы искать'"
# code = "class UDPlayers(Players): def __init__(self, form_info): super().__init__(form_info)"
# code = "def update(self): update_id: int = int(self.form_info['player_id_update']) - 1 full_name: str = \ self.form_info['player_first_name'].capitalize() + ' ' + \ self.form_info['player_last_name'].capitalize() + ' ' + \ self.form_info['player_surname'].capitalize() position: str = self.form_info['player_role'].capitalize() age: str = self.form_info['player_age'] height: str = self.form_info['player_height'] weight: str = self.form_info['player_weight'] team: str = self.form_info['player_team'] education: str = self.form_info['player_education'] salary: str = self.form_info['player_salary'] player_new_info: list = [ full_name, position, age, height, weight, team, education, salary ] checked_player_new_info: list = self.check_unknown_fields(player_new_info) file = pd.read_csv('results/players.csv') if 1 < update_id < len(file['Name']): file.loc[update_id, 'Name'] = checked_player_new_info[0] if checked_player_new_info[0] != 'Неизвестно' else file.loc[update_id, 'Name'] file.loc[update_id, 'Position'] = checked_player_new_info[1] if checked_player_new_info[1] != 'Неизвестно' else file.loc[update_id, 'Position'] file.loc[update_id, 'Age'] = checked_player_new_info[2] if checked_player_new_info[2] != 'Неизвестно' else file.loc[update_id, 'Age'] file.loc[update_id, 'Height'] = checked_player_new_info[3] if checked_player_new_info[3] != 'Неизвестно' else file.loc[update_id, 'Height'] file.loc[update_id, 'Weight'] = checked_player_new_info[4] if checked_player_new_info[4] != 'Неизвестно' else file.loc[update_id, 'Weight'] file.loc[update_id, 'Team'] = checked_player_new_info[5] if checked_player_new_info[5] != 'Неизвестно' else file.loc[update_id, 'Team'] file.loc[update_id, 'College'] = checked_player_new_info[6] if checked_player_new_info[6] != 'Неизвестно' else file.loc[update_id, 'College'] file.loc[update_id, 'Salary'] = checked_player_new_info[7] if checked_player_new_info[7] != 'Неизвестно' else file.loc[update_id, 'Salary'] file.to_csv('results/players.csv', index=False, mode='w') return self.read_csv_to_html() return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'"
# code = "def delete(self): delete_id: int = int(self.form_info['player_id_delete']) - 1 file = pd.read_csv('results/players.csv') if 1 < delete_id < len(file['Name']): file.drop(delete_id, inplace=True) file.to_csv('results/players.csv', index=False, mode='w') return self.read_csv_to_html() return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'"
# code = "import translators from spellchecker import SpellChecker import pandas as pd import re"
# code = "class Translate: def __init__(self, word: dict): self.spell: SpellChecker = SpellChecker(language='ru') self.translator: translators = translators self.word: dict = word"
# code = "def check_spelling(self): if self.spell.correction(self.word['word_translate']) == self.word['word_translate']: return self.translate() return self.error()"
# code = "def read_csv(self) -> bool: csv: dict = pd.read_csv('results/words.csv')['Russian'].to_dict() for index in csv: if self.word['word_translate'].capitalize() == csv[index]: return False continue return True"
# code = "def translate(self): if self.read_csv(): return self.to_csv([ self.word['word_translate'].capitalize(), self.translator.translate_text(self.word['word_translate'], from_language='ru', to_language='en').capitalize(), self.translator.translate_text(self.word['word_translate'], from_language='ru', to_language='fr').capitalize() ]) else: return 'Данное слово уже существует.'"
# code = "def to_csv(self, words_list: list): columns: list = ['Russian', 'English', 'French'] df = pd.DataFrame([words_list], columns=columns) df.to_csv('results/words.csv', mode='a', header=False, index=False) return self.read_csv_to_html()"
# code = "lines: list = [x.split(',') for x in file.read().splitlines()[1:]]"
# code = "mistakes: str = ', '.join([mistake.capitalize() for mistake in self.spell.candidates(self.word)])"
# code = "@staticmethod def search(word: str) -> str or list: if len(word.replace(r'\s+', '')) > 0: result: list = [] with open('results/words.csv') as words: words_rows: list = [x.split('\') for x in words.read().splitlines()[1:]] words_pandas: list = pd.read_csv('results/words.csv') for title in words_pandas: for index, row in enumerate(words_pandas[title]): if word in row: needed_row: str = ' ,'.join(words_rows[index]).split(',') result.append(needed_row) continue return result if len(result) > 0 else 'Совпадений не найдено.' return 'Вы ничего не ввели, чтобы искать'"
# code = "class UDTranslate(Translate): def __init__(self, word: dict): super().__init__(word)"
# code = "def update(self): update_id: int = int(self.word['word_translate_id_update']) - 1 word_english: str = self.word['word_translate_english'] word_french: str = self.word['word_translate_french'] file = pd.read_csv('results/words.csv') if 1 < update_id < len(file['Russian']): file.loc[update_id, 'English'] = word_english \ if len(re.sub(r'\s+', '', word_english)) != 0 else file.loc[update_id, 'English'] file.loc[update_id, 'French'] = word_french \ if len(re.sub(r'\s+', '', word_french)) != 0 else file.loc[update_id, 'French'] file.to_csv('results/words.csv', index=False, mode='w') return self.read_csv_to_html() return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'"
# code = "def delete(self): delete_id: int = int(self.word['word_translate_id_delete']) - 1 file = pd.read_csv('results/words.csv') if 1 < delete_id < len(file['Russian']): file.drop(delete_id, inplace=True) file.to_csv('results/words.csv', index=False, mode='w') return self.read_csv_to_html() return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'"
# code = "import pandas as pd from bs4 import BeautifulSoup as bs import requests import re"
# code = "class Company: def __init__(self, form_info: dict): self.form_info: dict = form_info"
# code = "@staticmethod def auto_create_employees(): person: Person = Person(locale=Locale.RU) gender: Gender = choice([Gender.FEMALE, Gender.MALE]) columns: list = ['Name', 'Phone', 'Email', 'Age', 'Occupation', 'Nationality', 'University', 'Work Experience'] employees_list: list = [ { 'name': person.full_name(gender=gender), 'phone': person.telephone(mask='+7(9##)-###-##-##'), 'email': person.email(domains=['mail.ru', 'gmail.com', 'yandex.ru']), 'age': person.age(minimum=25, maximum=66), 'occupation': person.occupation(), 'nationality': person.nationality(gender=gender), 'university': person.university(), 'work_experience': person.work_experience(working_start_age=20) } for _ in range(100) ] df_w = pd.DataFrame([columns], columns=columns) df_w.to_csv('results/employees.csv', mode='w', index=False, header=False) for employee in employees_list: employee_info: list = [ employee['name'], employee['phone'], employee['email'], employee['age'], employee['occupation'], employee['nationality'], employee['university'], employee['work_experience'] ] df_a = pd.DataFrame([employee_info], columns=columns) df_a.to_csv('results/employees.csv', mode='a', index=False, header=False)"
# code = "def add_employee_to_csv(self): full_name: str = \ self.form_info['employee_first_name'].capitalize() + ' ' + \ self.form_info['employee_last_name'].capitalize() + ' ' + \ self.form_info['employee_surname'].capitalize() phone: str = self.form_info['employee_phone_number'] email: str = self.form_info['employee_email'] age: str = self.form_info['employee_age'] occupation: str = self.form_info['employee_occupation'] nationality: str = self.form_info['employee_nationality'] university: str = self.form_info['employee_university'] work_experience: str = self.form_info['employee_work_experience'] columns: list = ['Name', 'Phone', 'Email', 'Age', 'Occupation', 'Nationality', 'University', 'Work Experience'] new_employee_info: list = [ full_name, phone, email, age, occupation, nationality, university, work_experience ] check_employee_info: list = self.check_unknown_fields(new_employee_info) df_a = pd.DataFrame([check_employee_info], columns=columns) df_a.to_csv('results/employees.csv', mode='a', index=False, header=False) return self.read_csv_to_html()"
# code = "@staticmethod def check_unknown_fields(employee_info: list) -> list: for index, field in enumerate(employee_info): if len(re.sub(r'\s+', '', field)) == 0: employee_info[index] = 'Неизвестно' continue return employee_info"
# code = "@staticmethod def search(word: str) -> str or list: if len(word.replace(r'\s+', '')) > 0: result: list = [] with open('results/employees.csv') as employees: employees_rows: list = [x.split('\') for x in employees.read().splitlines()[1:]] employees_pandas: list = pd.read_csv('results/employees.csv') for title in employees_pandas: if title not in ['Phone', 'Email', 'Age', 'Work Experience']: for index, row in enumerate(employees_pandas[title]): if word in str(row): needed_row: str = ' ,'.join(employees_rows[index]).split(',') result.append(needed_row) continue continue return result if len(result) > 0 else 'Совпадений не найдено.' return 'Вы ничего не ввели, чтобы искать'"
# code = "class UDCompany(Company): def __init__(self, form_info: dict): super().__init__(form_info)"
# code = "def update(self): update_id: int = int(self.form_info['employee_id_update']) - 1 full_name: str = \ self.form_info['employee_first_name'].capitalize() + ' ' + \ self.form_info['employee_last_name'].capitalize() + ' ' + \ self.form_info['employee_surname'].capitalize() phone: str = self.form_info['employee_phone_number'] email: str = self.form_info['employee_email'] age: str = self.form_info['employee_age'] occupation: str = self.form_info['employee_occupation'] nationality: str = self.form_info['employee_nationality'] university: str = self.form_info['employee_university'] work_experience: str = self.form_info['employee_work_experience'] new_employee_info: list = [ full_name, phone, email, age, occupation, nationality, university, work_experience ] check_employee_info: list = self.check_unknown_fields(new_employee_info) file = pd.read_csv('results/employees.csv') if 1 < update_id < len(file['Name']): file.loc[update_id, 'Name'] = check_employee_info[0] \ if check_employee_info[0] != 'Неизвестно' else file.loc[update_id, 'Name'] file.loc[update_id, 'Phone'] = check_employee_info[1] \ if check_employee_info[1] != 'Неизвестно' else file.loc[update_id, 'Phone'] file.loc[update_id, 'Email'] = check_employee_info[2] \ if check_employee_info[2] != 'Неизвестно' else file.loc[update_id, 'Email'] file.loc[update_id, 'Age'] = check_employee_info[3] \ if check_employee_info[3] != 'Неизвестно' else file.loc[update_id, 'Age'] file.loc[update_id, 'Occupation'] = check_employee_info[4] \ if check_employee_info[4] != 'Неизвестно' else file.loc[update_id, 'Occupation'] file.loc[update_id, 'Nationality'] = check_employee_info[5] \ if check_employee_info[5] != 'Неизвестно' else file.loc[update_id, 'Nationality'] file.loc[update_id, 'University'] = check_employee_info[6] \ if check_employee_info[6] != 'Неизвестно' else file.loc[update_id, 'University'] file.loc[update_id, 'Work Experience'] = check_employee_info[7] \ if check_employee_info[7] != 'Неизвестно' else file.loc[update_id, 'Work Experience'] file.to_csv('results/employees.csv', index=False, mode='w') return self.read_csv_to_html() return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'"
# code = "def delete(self): delete_id: int = int(self.form_info['employee_id_delete']) - 1 file = pd.read_csv('results/employees.csv') if 1 < delete_id < len(file['Name']): file.drop(delete_id, inplace=True) file.to_csv('results/employees.csv', index=False, mode='w') return self.read_csv_to_html() return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'"
# code = "from mimesis import Person from mimesis.locales import Locale from mimesis.enums import Gender from random import choice import pandas as pd import re"
# code = "class Books: def __init__(self, form_info: dict): self.form_info: dict = form_info"
# code = "@staticmethod def parse_site(): url: str = 'https://libcat.ru/' columns: list = ['Title', 'Author', 'Genre', 'Year', 'Publisher', 'Summary'] needed_hrefs: list = [ link['href'] for link in bs(requests.get(url).content, 'html.parser') .find_all('a', {'class': 'tag'}) ] df_w = pd.DataFrame([columns], columns=columns) df_w.to_csv('results/books.csv', mode='w', index=False, header=False) for href in needed_hrefs: links: set = set([ link['href'] for link in bs(requests.get(url + href).content, 'html.parser') .find('div', {'id': 'dle-content'}) .find_all('a') if 'page' not in link['href'] ]) for link in links: try: book_page = bs(requests.get(link).content, 'html.parser') title_of_book: str = book_page.find('div', attrs={'itemprop': 'name'}).text author_of_book: str = book_page.find('a', attrs={'itemprop': 'author'}).text genre_of_book: str = book_page.find('a', attrs={'itemprop': 'genre'}).text year_of_book: str = book_page.find('div', attrs={'itemprop': 'copyrightYear'}).text publisher_of_book: str = book_page.find('div', attrs={'itemprop': 'publisher'}).text summary_of_book: str = 'Неизвестно' if '' == book_page.find('div', attrs={'itemprop': 'about'}).text \ else book_page.find('div', attrs={'itemprop': 'about'}).text book_info: list = [ title_of_book, author_of_book, genre_of_book, year_of_book, publisher_of_book, summary_of_book ] df_a = pd.DataFrame([book_info], columns=columns) df_a.to_csv('results/books.csv', mode='a', index=False, header=False) except AttributeError: continue"
# code = "@staticmethod def check_unknown_fields(book_info: list) -> list: for index, field in enumerate(book_info): if len(re.sub(r'\s+', '', field)) == 0: book_info[index] = 'Неизвестно' continue return book_info"
# code = "def add_book_to_csv(self): title: str = self.form_info['book_title'] author: str = self.form_info['book_author'] genre: str = self.form_info['book_genre'] year: str = self.form_info['book_year'] publisher: str = self.form_info['book_publisher'] summary: str = self.form_info['book_summary'] columns: list = ['Title', 'Author', 'Genre', 'Year', 'Publisher', 'Summary'] new_book_info: list = [ title, author, genre, year, publisher, summary ] checked_book_info: list = self.check_unknown_fields(new_book_info) df_a = pd.DataFrame([checked_book_info], columns=columns) df_a.to_csv('results/books.csv', mode='a', index=False, header=False) return self.read_csv_to_html()"
# code = "@staticmethod def read_csv_to_html(): books = pd.read_csv('results/books.csv') return books"
# print(type(pd.read_csv('results/books.csv')))
# code = "@staticmethod def search(word: str) -> str or dict: if len(word.replace(r'\s+', '')) > 0: result: dict = { 'Title': [], 'Author': [], 'Genre': [], 'Year': [], 'Publisher': [], 'Summary': [] } with open('results/books.csv') as _: books_pandas: list = pd.read_csv('results/books.csv') for title in books_pandas: if title not in ['Year', 'Summary']: for index, row in enumerate(books_pandas[title]): if word in str(row): result['Title'].append(books_pandas['Title'][index]) result['Author'].append(books_pandas['Author'][index]) result['Genre'].append(books_pandas['Genre'][index]) result['Year'].append(books_pandas['Year'][index]) result['Publisher'].append(books_pandas['Publisher'][index]) result['Summary'].append(books_pandas['Summary'][index]) continue continue return result if len(result['Title']) > 0 else 'Совпадений не найдено.' return 'Вы ничего не ввели, чтобы искать'"
# code = "if len(re.sub(r'\s+', '', word)) > 0:"
# code = "class UDBooks(Books): def __init__(self, form_info: dict): super().__init__(form_info)"
# code = "def update(self): update_id: int = int(self.form_info['book_id_update']) - 1 title: str = self.form_info['book_title'] author: str = self.form_info['book_author'] genre: str = self.form_info['book_genre'] year: str = self.form_info['book_year'] publisher: str = self.form_info['book_publisher'] summary: str = self.form_info['book_summary'] new_book_info: list = [ title, author, genre, year, publisher, summary ] checked_book_info: list = self.check_unknown_fields(new_book_info) file = pd.read_csv('results/books.csv') if 1 < update_id < len(file['Title']): file.loc[update_id, 'Title'] = checked_book_info[0] \ if checked_book_info[0] != 'Неизвестно' else file.loc[update_id, 'Title'] file.loc[update_id, 'Author'] = checked_book_info[1] \ if checked_book_info[1] != 'Неизвестно' else file.loc[update_id, 'Author'] file.loc[update_id, 'Genre'] = checked_book_info[2] \ if checked_book_info[2] != 'Неизвестно' else file.loc[update_id, 'Genre'] file.loc[update_id, 'Year'] = checked_book_info[3] \ if checked_book_info[3] != 'Неизвестно' else file.loc[update_id, 'Year'] file.loc[update_id, 'Publisher'] = checked_book_info[4] \ if checked_book_info[4] != 'Неизвестно' else file.loc[update_id, 'Publisher'] file.loc[update_id, 'Summary'] = checked_book_info[5] \ if checked_book_info[5] != 'Неизвестно' else file.loc[update_id, 'Summary'] file.to_csv('results/books.csv', index=False, mode='w') return self.read_csv_to_html() return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'"
code = "def delete(self): delete_id: int = int(self.form_info['book_id_delete']) - 1 file = pd.read_csv('results/books.csv') if 1 < delete_id < len(file['Title']): file.drop(delete_id, inplace=True) file.to_csv('results/books.csv', index=False, mode='w') return self.read_csv_to_html() return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'"
print(highlight(code, PythonLexer(), HtmlFormatter(noclasses=True, style='solarized-light', cssstyles='border-radius: 8px;border: 1px solid grey;padding: 15px')))
