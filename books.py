import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


class Books:
    def __init__(self, book: dict):
        self.title = book['book_title']
        self.author = book['book_author']
        self.genre = book['book_genre']
        self.year = book['book_year']
        self.publisher = book['book_publisher']
        self.summary = book['book_summary']

    @staticmethod
    def parse_site():
        url = 'https://libcat.ru/'
        columns = ['Title', 'Author', 'Genre', 'Year', 'Publisher', 'Summary']
        needed_hrefs: list = [
            link['href'] for link in bs(requests.get(url).content, 'html.parser')
            .find_all('a', {'class': 'tag'})
        ]
        df_w = pd.DataFrame([columns], columns=columns)
        df_w.to_csv('results/books.csv', mode='w', index=False, header=False)
        for href in needed_hrefs:
            links = set([
                link['href'] for link in bs(requests.get(url + href).content, 'html.parser')
                .find('div', {'id': 'dle-content'})
                .find_all('a') if 'page' not in link['href']
            ])
            for link in links:
                try:
                    book_page = bs(requests.get(link).content, 'html.parser')
                    title_of_book = book_page.find('div', attrs={'itemprop': 'name'}).text
                    author_of_book = book_page.find('a', attrs={'itemprop': 'author'}).text
                    genre_of_book = book_page.find('a', attrs={'itemprop': 'genre'}).text
                    year_of_book = book_page.find('div', attrs={'itemprop': 'copyrightYear'}).text
                    publisher_of_book = book_page.find('div', attrs={'itemprop': 'publisher'}).text
                    summary_of_book = 'Неизвестно' if '' == book_page.find('div', attrs={'itemprop': 'about'}).text \
                        else book_page.find('div', attrs={'itemprop': 'about'}).text
                    book_info = [
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
            if field == '':
                book_info[index] = 'Неизвестно'
            continue
        return book_info

    def add_book_to_csv(self):
        columns = ['Title', 'Author', 'Genre', 'Year', 'Publisher', 'Summary']
        new_book_info: list = [
            self.title, self.author, self.genre,
            self.year, self.publisher, self.summary
        ]
        checked_book_info = self.check_unknown_fields(new_book_info)
        df_a = pd.DataFrame([checked_book_info], columns=columns)
        df_a.to_csv('results/books.csv', mode='a', index=False, header=False)
        return self.read_csv_to_html()

    @staticmethod
    def read_csv_to_html() -> list:
        file = open('results/books.csv', 'r')
        lines = [x.split('\n') for x in file.read().splitlines()[1:]]
        return lines

    @staticmethod
    def search(word: str) -> str or dict:
        result = {
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


if __name__ == '__main__':
    Books.parse_site()
