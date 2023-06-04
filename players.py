from bs4 import BeautifulSoup as bs
from unitsnet_py import Length, LengthUnits, Mass, MassUnits
import requests
import pandas as pd
import re
from currency_converter import CurrencyConverter as cc


class Players:
    def __init__(self, player_info: dict):
        self.full_name = \
            player_info['player_last_name'].capitalize() + ' ' + \
            player_info['player_first_name'].capitalize() + ' ' + \
            player_info['player_surname'].capitalize()
        self.position = player_info['player_role'].upper()
        self.age = player_info['player_age']
        self.height = player_info['player_height']
        self.weight = player_info['player_weight']
        self.team = player_info['player_team']
        self.education = player_info['player_education']
        self.salary = player_info['player_salary']

    @staticmethod
    def parse_site():
        url = 'https://www.espn.com'
        response = requests.get(url + '/nba/teams')
        response_body = bs(response.content, 'html.parser')
        needed_hrefs = [
            link["href"] for link in response_body
            .find('div', {'class': 'layout is-split'})
            .find_all('a', {'class': 'AnchorLink'}) if 'roster' in link["href"]
        ]
        columns = ['Name', 'Position', 'Age', 'Height', 'Weight', 'Team', 'College', 'Salary']
        df_w = pd.DataFrame([columns], columns=columns)
        df_w.to_csv('results/players.csv', mode='w', index=False, header=False)
        for href in needed_hrefs:
            table_rows = bs(requests.get(url + href).content, 'html.parser')\
                .find('tbody', {'class': 'Table__TBODY'})\
                .find_all('tr', {'class': 'Table__TR'})
            for table_row in table_rows:
                table_datas = table_row.find_all('td', {'class': 'Table__TD'})
                player_name = ' '.join(re.findall('[A-z.]+', table_datas[1].text))
                player_role = table_datas[2].text
                player_age = table_datas[3].text
                player_height = round(Length(float('.'.join(re.findall(r'[1-9]+', table_datas[4].text))), LengthUnits.Foot).centimeters)
                player_weight = round(Mass(int(re.findall(r'[0-9]+', table_datas[5].text)[0]), MassUnits.Pound).kilograms)
                player_team = ' '.join(
                    [
                        team.text for team in bs(requests.get(url + href).content, 'html.parser')
                        .find('main', {'id': 'fittPageContainer'})
                        .find('h1', {'class': 'ClubhouseHeader__Name'})
                        .find_all('span', {'class': 'db'})
                    ]
                )
                player_info_unknown = 'Неизвестно'
                player_education = player_info_unknown if re.search(r'-', table_datas[6].text) else table_datas[6].text
                player_salary_usd = ''.join(''.join(re.findall(r'[0-9,]+', table_datas[7].text)).split(','))
                player_salary = player_info_unknown \
                    if re.search(r'-', table_datas[7].text) \
                    else round(cc(fallback_on_wrong_date=True).convert(int(player_salary_usd), 'USD', 'RUB') / 1000000)

                player_info_list = [
                    player_name, player_role, player_age, player_height,
                    player_weight, player_team, player_education, player_salary
                ]
                df_a = pd.DataFrame([player_info_list], columns=columns)
                df_a.to_csv('results/players.csv', mode='a', index=False, header=False)

    def add_player_to_csv(self):
        columns = ['Name', 'Position', 'Age', 'Height', 'Weight', 'Team', 'College', 'Salary']
        new_player_info = [
            self.full_name, self.position, self.age, self.height,
            self.weight, self.team, self.education, self.salary
        ]
        checked_player_info = self.check_unknown_fields(new_player_info)
        df_a = pd.DataFrame([checked_player_info], columns=columns)
        df_a.to_csv('results/players.csv', mode='a', index=False, header=False)
        return self.read_csv_to_html()

    @staticmethod
    def check_unknown_fields(player_info: list):
        for index, field in enumerate(player_info):
            if field == '' or field == '  ':
                player_info[index] = 'Неизвестно'
            continue
        return player_info

    @staticmethod
    def read_csv_to_html() -> list:
        file = open('results/players.csv', 'r')
        lines = [x.split(',') for x in file.read().splitlines()[1:]]
        return lines


if __name__ == '__main__':
    Players.parse_site()
