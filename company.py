from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
from random import choice
import pandas as pd
import re


class Company:
    def __init__(self, form_info: dict):
        self.form_info: dict = form_info

    @staticmethod
    def auto_create_employees():
        person = Person(locale=Locale.RU)
        gender = choice([Gender.FEMALE, Gender.MALE])
        columns: list = ['Name', 'Phone', 'Email', 'Age', 'Occupation', 'Nationality', 'University', 'Work Experience']
        employees_list: list = [
            {
                'name': person.full_name(gender=gender),
                'phone': person.telephone(mask='+7(9##)-###-##-##'),
                'email': person.email(domains=['mail.ru', 'gmail.com', 'yandex.ru']),
                'age': person.age(minimum=25, maximum=66),
                'occupation': person.occupation(),
                'nationality': person.nationality(gender=gender),
                'university': person.university(),
                'work_experience': person.work_experience(working_start_age=20)
            } for _ in range(100)
        ]
        df_w = pd.DataFrame([columns], columns=columns)
        df_w.to_csv('results/employees.csv', mode='w', index=False, header=False)
        for employee in employees_list:
            employee_info: list = [
                employee['name'], employee['phone'], employee['email'], employee['age'],
                employee['occupation'], employee['nationality'], employee['university'], employee['work_experience']
            ]
            df_a = pd.DataFrame([employee_info], columns=columns)
            df_a.to_csv('results/employees.csv', mode='a', index=False, header=False)

    def add_employee_to_csv(self):
        full_name: str = \
            self.form_info['employee_first_name'].capitalize() + ' ' + \
            self.form_info['employee_last_name'].capitalize() + ' ' + \
            self.form_info['employee_surname'].capitalize()
        phone: str = self.form_info['employee_phone_number']
        email: str = self.form_info['employee_email']
        age: str = self.form_info['employee_age']
        occupation: str = self.form_info['employee_occupation']
        nationality: str = self.form_info['employee_nationality']
        university: str = self.form_info['employee_university']
        work_experience: str = self.form_info['employee_work_experience']
        columns: list = ['Name', 'Phone', 'Email', 'Age', 'Occupation', 'Nationality', 'University', 'Work Experience']
        new_employee_info: list = [
            full_name, phone, email, age, occupation,
            nationality, university, work_experience
        ]
        check_employee_info: list = self.check_unknown_fields(new_employee_info)
        df_a = pd.DataFrame([check_employee_info], columns=columns)
        df_a.to_csv('results/employees.csv', mode='a', index=False, header=False)
        return self.read_csv_to_html()

    @staticmethod
    def check_unknown_fields(employee_info: list) -> list:
        for index, field in enumerate(employee_info):
            if len(re.sub(r'\s+', '', field)) == 0:
                employee_info[index] = 'Неизвестно'
            continue
        return employee_info

    @staticmethod
    def read_csv_to_html() -> list:
        file = open('results/employees.csv', 'r')
        lines: list = [x.split(',') for x in file.read().splitlines()[1:]]
        return lines

    @staticmethod
    def search(word: str) -> str or list:
        if len(word.replace(r'\s+', '')) > 0:
            result: list = []
            with open('results/employees.csv') as employees:
                employees_rows: list = [x.split('\n') for x in employees.read().splitlines()[1:]]
                employees_pandas: list = pd.read_csv('results/employees.csv')
                for title in employees_pandas:
                    if title not in ['Phone', 'Email', 'Age', 'Work Experience']:
                        for index, row in enumerate(employees_pandas[title]):
                            if word in str(row):
                                needed_row: str = ' ,'.join(employees_rows[index]).split(',')
                                result.append(needed_row)
                            continue
                    continue
            return result if len(result) > 0 else 'Совпадений не найдено.'
        return 'Вы ничего не ввели, чтобы искать'


class UDCompany(Company):
    def __init__(self, form_info: dict):
        super().__init__(form_info)

    def update(self):
        update_id: int = int(self.form_info['employee_id_update']) - 1
        full_name: str = \
            self.form_info['employee_first_name'].capitalize() + ' ' + \
            self.form_info['employee_last_name'].capitalize() + ' ' + \
            self.form_info['employee_surname'].capitalize()
        phone: str = self.form_info['employee_phone_number']
        email: str = self.form_info['employee_email']
        age: str = self.form_info['employee_age']
        occupation: str = self.form_info['employee_occupation']
        nationality: str = self.form_info['employee_nationality']
        university: str = self.form_info['employee_university']
        work_experience: str = self.form_info['employee_work_experience']
        new_employee_info: list = [
            full_name, phone, email, age, occupation,
            nationality, university, work_experience
        ]
        check_employee_info: list = self.check_unknown_fields(new_employee_info)
        file = pd.read_csv('results/employees.csv')
        if 1 < update_id < len(file['Name']):
            file.loc[update_id, 'Name'] = check_employee_info[0] \
                if check_employee_info[0] != 'Неизвестно' else file.loc[update_id, 'Name']
            file.loc[update_id, 'Phone'] = check_employee_info[1] \
                if check_employee_info[1] != 'Неизвестно' else file.loc[update_id, 'Phone']
            file.loc[update_id, 'Email'] = check_employee_info[2] \
                if check_employee_info[2] != 'Неизвестно' else file.loc[update_id, 'Email']
            file.loc[update_id, 'Age'] = check_employee_info[3] \
                if check_employee_info[3] != 'Неизвестно' else file.loc[update_id, 'Age']
            file.loc[update_id, 'Occupation'] = check_employee_info[4] \
                if check_employee_info[4] != 'Неизвестно' else file.loc[update_id, 'Occupation']
            file.loc[update_id, 'Nationality'] = check_employee_info[5] \
                if check_employee_info[5] != 'Неизвестно' else file.loc[update_id, 'Nationality']
            file.loc[update_id, 'University'] = check_employee_info[6] \
                if check_employee_info[6] != 'Неизвестно' else file.loc[update_id, 'University']
            file.loc[update_id, 'Work Experience'] = check_employee_info[7] \
                if check_employee_info[7] != 'Неизвестно' else file.loc[update_id, 'Work Experience']
            file.to_csv('results/employees.csv', index=False, mode='w')
            return self.read_csv_to_html()
        return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'

    def delete(self):
        delete_id: int = int(self.form_info['employee_id_delete']) - 1
        file = pd.read_csv('results/employees.csv')
        if 1 < delete_id < len(file['Name']):
            file.drop(delete_id, inplace=True)
            file.to_csv('results/employees.csv', index=False, mode='w')
            return self.read_csv_to_html()
        return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'
