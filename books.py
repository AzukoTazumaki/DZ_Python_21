import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re


class Books:
    def __init__(self, form_info: dict):
        self.form_info: dict = form_info

    @staticmethod
    def parse_site():
        url: str = 'https://libcat.ru/'
        columns: list = ['Title', 'Author', 'Genre', 'Year', 'Publisher', 'Summary']
        needed_hrefs: list = [
            link['href'] for link in bs(requests.get(url).content, 'html.parser')
            .find_all('a', {'class': 'tag'})
        ]
        df_w = pd.DataFrame([columns], columns=columns)
        df_w.to_csv('results/books.csv', mode='w', index=False, header=False)
        for href in needed_hrefs:
            links: set = set([
                link['href'] for link in bs(requests.get(url + href).content, 'html.parser')
                .find('div', {'id': 'dle-content'})
                .find_all('a') if 'page' not in link['href']
            ])
            for link in links:
                try:
                    book_page = bs(requests.get(link).content, 'html.parser')
                    title_of_book: str = book_page.find('div', attrs={'itemprop': 'name'}).text
                    author_of_book: str = book_page.find('a', attrs={'itemprop': 'author'}).text
                    genre_of_book: str = book_page.find('a', attrs={'itemprop': 'genre'}).text
                    year_of_book: str = book_page.find('div', attrs={'itemprop': 'copyrightYear'}).text
                    publisher_of_book: str = book_page.find('div', attrs={'itemprop': 'publisher'}).text
                    summary_of_book: str = 'Неизвестно' if '' == book_page.find('div', attrs={'itemprop': 'about'}).text \
                        else book_page.find('div', attrs={'itemprop': 'about'}).text
                    book_info: list = [
                        title_of_book, author_of_book, genre_of_book,
                        year_of_book, publisher_of_book, summary_of_book
                    ]
                    df_a = pd.DataFrame([book_info], columns=columns)
                    df_a.to_csv('results/books.csv', mode='a', index=False, header=False)
                except AttributeError:
                    continue

    @staticmethod
    def check_unknown_fields(book_info: list) -> list:
        for index, field in enumerate(book_info):
            if len(re.sub(r'\s+', '', field)) == 0:
                book_info[index] = 'Неизвестно'
            continue
        return book_info

    def add_book_to_csv(self):
        title: str = self.form_info['book_title']
        author: str = self.form_info['book_author']
        genre: str = self.form_info['book_genre']
        year: str = self.form_info['book_year']
        publisher: str = self.form_info['book_publisher']
        summary: str = self.form_info['book_summary']
        columns: list = ['Title', 'Author', 'Genre', 'Year', 'Publisher', 'Summary']
        new_book_info: list = [
            title, author, genre,
            year, publisher, summary
        ]
        checked_book_info: list = self.check_unknown_fields(new_book_info)
        df_a = pd.DataFrame([checked_book_info], columns=columns)
        df_a.to_csv('results/books.csv', mode='a', index=False, header=False)
        return self.read_csv_to_html()

    @staticmethod
    def read_csv_to_html():
        books = pd.read_csv('results/books.csv')
        return books

    @staticmethod
    def search(word: str) -> str or dict:
        if len(word.replace(r'\s+', '')) > 0:
            result: dict = {
                'Title': [],
                'Author': [],
                'Genre': [],
                'Year': [],
                'Publisher': [],
                'Summary': []
            }
            with open('results/books.csv') as _:
                books_pandas: list = pd.read_csv('results/books.csv')
                for title in books_pandas:
                    if title not in ['Year', 'Summary']:
                        for index, row in enumerate(books_pandas[title]):
                            if word in str(row):
                                result['Title'].append(books_pandas['Title'][index])
                                result['Author'].append(books_pandas['Author'][index])
                                result['Genre'].append(books_pandas['Genre'][index])
                                result['Year'].append(books_pandas['Year'][index])
                                result['Publisher'].append(books_pandas['Publisher'][index])
                                result['Summary'].append(books_pandas['Summary'][index])
                            continue
                    continue
            return result if len(result['Title']) > 0 else 'Совпадений не найдено.'
        return 'Вы ничего не ввели, чтобы искать'


class UDBooks(Books):
    def __init__(self, form_info: dict):
        super().__init__(form_info)

    def update(self):
        update_id: int = int(self.form_info['book_id_update']) - 1
        title: str = self.form_info['book_title']
        author: str = self.form_info['book_author']
        genre: str = self.form_info['book_genre']
        year: str = self.form_info['book_year']
        publisher: str = self.form_info['book_publisher']
        summary: str = self.form_info['book_summary']
        new_book_info: list = [
            title, author, genre,
            year, publisher, summary
        ]
        checked_book_info: list = self.check_unknown_fields(new_book_info)
        file = pd.read_csv('results/books.csv')
        if 1 < update_id < len(file['Title']):
            file.loc[update_id, 'Title'] = checked_book_info[0] \
                if checked_book_info[0] != 'Неизвестно' else file.loc[update_id, 'Title']
            file.loc[update_id, 'Author'] = checked_book_info[1] \
                if checked_book_info[1] != 'Неизвестно' else file.loc[update_id, 'Author']
            file.loc[update_id, 'Genre'] = checked_book_info[2] \
                if checked_book_info[2] != 'Неизвестно' else file.loc[update_id, 'Genre']
            file.loc[update_id, 'Year'] = checked_book_info[3] \
                if checked_book_info[3] != 'Неизвестно' else file.loc[update_id, 'Year']
            file.loc[update_id, 'Publisher'] = checked_book_info[4] \
                if checked_book_info[4] != 'Неизвестно' else file.loc[update_id, 'Publisher']
            file.loc[update_id, 'Summary'] = checked_book_info[5] \
                if checked_book_info[5] != 'Неизвестно' else file.loc[update_id, 'Summary']
            file.to_csv('results/books.csv', index=False, mode='w')
            return self.read_csv_to_html()
        return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'

    def delete(self):
        delete_id: int = int(self.form_info['book_id_delete']) - 1
        file = pd.read_csv('results/books.csv')
        if 1 < delete_id < len(file['Title']):
            file.drop(delete_id, inplace=True)
            file.to_csv('results/books.csv', index=False, mode='w')
            return self.read_csv_to_html()
        return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'
