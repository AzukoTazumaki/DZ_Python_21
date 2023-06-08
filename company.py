from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
from random import choice
import pandas as pd


class Company:
    def __init__(self, employee_info: dict):
        self.full_name: str = \
            employee_info['employee_last_name'].capitalize() + ' ' + \
            employee_info['employee_first_name'].capitalize() + ' ' + \
            employee_info['employee_surname'].capitalize()
        self.phone: str = employee_info['employee_phone_number']
        self.email: str = employee_info['employee_email']
        self.age: str = employee_info['employee_age']
        self.occupation: str = employee_info['employee_occupation']
        self.nationality: str = employee_info['employee_nationality']
        self.university: str = employee_info['employee_university']
        self.work_experience: str = employee_info['employee_work_experience']

    @staticmethod
    def auto_create_employees():
        person: Person = Person(locale=Locale.RU)
        gender = choice([Gender.FEMALE, Gender.MALE])
        columns: list = ['Name', 'Phone', 'Email', 'Age', 'Occupation', 'Nationality', 'University', 'Work Experience']
        employees_list = [
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
            employee_info = [
                employee['name'], employee['phone'], employee['email'], employee['age'],
                employee['occupation'], employee['nationality'], employee['university'], employee['work_experience']
            ]
            df_a = pd.DataFrame([employee_info], columns=columns)
            df_a.to_csv('results/employees.csv', mode='a', index=False, header=False)

    def add_employee_to_csv(self):
        columns: list = ['Name', 'Phone', 'Email', 'Age', 'Occupation', 'Nationality', 'University', 'Work Experience']
        new_employee_info: list = [
            self.full_name, self.phone, self.email, self.age,
            self.occupation, self.nationality, self.university, self.work_experience
        ]
        check_employee_info = self.check_unknown_fields(new_employee_info)
        df_a = pd.DataFrame([check_employee_info], columns=columns)
        df_a.to_csv('results/employees.csv', mode='a', index=False, header=False)
        return self.read_csv_to_html()

    @staticmethod
    def check_unknown_fields(employee_info: list):
        for index, field in enumerate(employee_info):
            if field == '' or field == '  ':
                employee_info[index] = 'Неизвестно'
            continue
        return employee_info

    @staticmethod
    def read_csv_to_html() -> list:
        file = open('results/employees.csv', 'r')
        lines = [x.split(',') for x in file.read().splitlines()[1:]]
        return lines

    @staticmethod
    def search(word: str) -> str or list:
        result = []
        with open('results/employees.csv') as employees:
            employees_rows: list = [x.split('\n') for x in employees.read().splitlines()[1:]]
            employees_pandas: list = pd.read_csv('results/employees.csv')
            for title in employees_pandas:
                if title not in ['Phone', 'Email', 'Age', 'Work Experience']:
                    for index, row in enumerate(employees_pandas[title]):
                        if word in str(row):
                            needed_row = ' ,'.join(employees_rows[index]).split(',')
                            result.append(needed_row)
                        continue
                continue
        return result if len(result) > 0 else 'Совпадений не найдено.'


if __name__ == '__main__':
    Company.auto_create_employees()
