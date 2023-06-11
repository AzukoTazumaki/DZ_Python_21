from bs4 import BeautifulSoup as bs
from unitsnet_py import Length, LengthUnits, Mass, MassUnits
import requests
import pandas as pd
import re
from currency_converter import CurrencyConverter as cc


class Players:
    def __init__(self, form_info: dict):
        self.form_info = form_info

    @staticmethod
    def parse_site():
        result = []
        url: str = 'https://www.espn.com'
        response = requests.get(url + '/nba/teams')
        response_body = bs(response.content, 'html.parser')
        needed_hrefs: list = [
            link["href"] for link in response_body
            .find('div', {'class': 'layout is-split'})
            .find_all('a', {'class': 'AnchorLink'}) if 'roster' in link["href"]
        ]
        columns: list = ['Name', 'Position', 'Age', 'Height', 'Weight', 'Team', 'College', 'Salary']
        for href in needed_hrefs:
            table_rows: list = bs(requests.get(url + href).content, 'html.parser') \
                .find('tbody', {'class': 'Table__TBODY'}) \
                .find_all('tr', {'class': 'Table__TR'})
            for table_row in table_rows:
                table_datas: list = table_row.find_all('td', {'class': 'Table__TD'})
                player_name: str = ' '.join(re.findall('[A-z.]+', table_datas[1].text))
                player_role: str = table_datas[2].text
                player_age: str = table_datas[3].text
                player_height: int = round(
                    Length(float('.'.join(re.findall(r'[1-9]+', table_datas[4].text))), LengthUnits.Foot).centimeters)
                player_weight: int = round(
                    Mass(int(re.findall(r'[0-9]+', table_datas[5].text)[0]), MassUnits.Pound).kilograms)
                player_team: str = ' '.join(
                    [
                        team.text for team in bs(requests.get(url + href).content, 'html.parser')
                    .find('main', {'id': 'fittPageContainer'})
                    .find('h1', {'class': 'ClubhouseHeader__Name'})
                    .find_all('span', {'class': 'db'})
                    ]
                )
                player_info_unknown: str = 'Неизвестно'
                player_education: str = player_info_unknown if re.search(r'-', table_datas[6].text) else table_datas[
                    6].text
                player_salary_usd: str = ''.join(''.join(re.findall(r'[0-9,]+', table_datas[7].text)).split(','))
                player_salary: str = player_info_unknown \
                    if re.search(r'-', table_datas[7].text) \
                    else round(cc(fallback_on_wrong_date=True).convert(int(player_salary_usd), 'USD', 'RUB') / 1000000)
                player_info_list: list = [
                    player_name, player_role, player_age, player_height,
                    player_weight, player_team, player_education, player_salary
                ]
                print(player_info_list)
                result.append(player_info_list)
        df_a = pd.DataFrame(result, columns=columns)
        df_a.to_csv('results/players.csv', mode='w', index=False)

    def add_player_to_csv(self):
        full_name = \
            self.form_info['player_last_name'].capitalize() + ' ' + \
            self.form_info['player_first_name'].capitalize() + ' ' + \
            self.form_info['player_surname'].capitalize()
        position = self.form_info['player_role'].upper()
        age = self.form_info['player_age']
        height = self.form_info['player_height']
        weight = self.form_info['player_weight']
        team = self.form_info['player_team']
        education = self.form_info['player_education']
        salary = self.form_info['player_salary']
        columns: list = ['Name', 'Position', 'Age', 'Height', 'Weight', 'Team', 'College', 'Salary']
        new_player_info: list = [
            full_name, position, age, height,
            weight, team, education, salary
        ]
        checked_player_info = self.check_unknown_fields(new_player_info)
        df_a = pd.DataFrame([checked_player_info], columns=columns)
        df_a.to_csv('results/players.csv', mode='a', index=False, header=False)
        return self.read_csv_to_html()

    @staticmethod
    def check_unknown_fields(player_info: list):
        for index, field in enumerate(player_info):
            if len(re.sub(r'\s+', '', field)) == 0:
                player_info[index] = 'Неизвестно'
            continue
        return player_info

    @staticmethod
    def read_csv_to_html() -> list:
        file = open('results/players.csv', 'r')
        lines = [x.split(',') for x in file.read().splitlines()[1:]]
        return lines

    @staticmethod
    def search(word: str) -> str or list:
        if len(re.sub(r'\s+', '', word)) > 0:
            result = []
            with open('results/players.csv') as players:
                players_rows: list = [x.split('\n') for x in players.read().splitlines()[1:]]
                players_pandas: list = pd.read_csv('results/players.csv')
                for title in players_pandas:
                    if title not in ['Position', 'Age', 'Height', 'Weight', 'Salary']:
                        for index, row in enumerate(players_pandas[title]):
                            if word in str(row):
                                needed_row = ' ,'.join(players_rows[index]).split(',')
                                result.append(needed_row)
                            continue
                    continue
            return result if len(result) > 0 else 'Совпадений не найдено.'
        return 'Вы ничего не ввели, чтобы искать'


class UD(Players):
    def __init__(self, form_info):
        super().__init__(form_info)

    def update(self):
        update_id = int(self.form_info['player_id_update']) - 1
        full_name = \
            self.form_info['player_first_name'].capitalize() + ' ' + \
            self.form_info['player_last_name'].capitalize() + ' ' + \
            self.form_info['player_surname'].capitalize()
        position = self.form_info['player_role'].capitalize()
        age = self.form_info['player_age']
        height = self.form_info['player_height']
        weight = self.form_info['player_weight']
        team = self.form_info['player_team']
        education = self.form_info['player_education']
        salary = self.form_info['player_salary']
        player_new_info: list = [
            full_name, position, age, height,
            weight, team, education, salary
        ]
        checked_player_new_info = self.check_unknown_fields(player_new_info)
        file = pd.read_csv('results/players.csv')
        file.loc[update_id, 'Name'] = checked_player_new_info[0] \
            if checked_player_new_info[0] != 'Неизвестно' else file.loc[update_id, 'Name']
        file.loc[update_id, 'Position'] = checked_player_new_info[1] \
            if checked_player_new_info[1] != 'Неизвестно' else file.loc[update_id, 'Position']
        file.loc[update_id, 'Age'] = checked_player_new_info[2] \
            if checked_player_new_info[2] != 'Неизвестно' else file.loc[update_id, 'Age']
        file.loc[update_id, 'Height'] = checked_player_new_info[3] \
            if checked_player_new_info[3] != 'Неизвестно' else file.loc[update_id, 'Height']
        file.loc[update_id, 'Weight'] = checked_player_new_info[4] \
            if checked_player_new_info[4] != 'Неизвестно' else file.loc[update_id, 'Weight']
        file.loc[update_id, 'Team'] = checked_player_new_info[5] \
            if checked_player_new_info[5] != 'Неизвестно' else file.loc[update_id, 'Team']
        file.loc[update_id, 'College'] = checked_player_new_info[6] \
            if checked_player_new_info[6] != 'Неизвестно' else file.loc[update_id, 'College']
        file.loc[update_id, 'Salary'] = checked_player_new_info[7] \
            if checked_player_new_info[7] != 'Неизвестно' else file.loc[update_id, 'Salary']
        file.to_csv('results/players.csv', index=False, mode='w')
        return self.read_csv_to_html()

    def delete(self):
        delete_id = int(self.form_info['player_id_delete'])
        file = pd.read_csv('results/players.csv')
        file.drop(delete_id, inplace=True)
        file.to_csv('results/players.csv', index=False, mode='w')
        return self.read_csv_to_html()


# if __name__ == '__main__':
#     Players.parse_site()
