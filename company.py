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
        self.nationality: str = employee_info['nationality']
        self.work_experience: str = employee_info['work_experience']

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
            } for _ in range(500)
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

    def to_csv(self):
        pass

    def read_csv(self):
        pass

    @staticmethod
    def read_csv_to_html() -> list:
        file = open('results/employees.csv', 'r')
        lines = [x.split(',') for x in file.read().splitlines()[1:]]
        return lines


if __name__ == '__main__':
    Company.auto_create_employees()
