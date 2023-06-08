import translators
from spellchecker import SpellChecker
import pandas as pd


class Translate:
    def __init__(self, user_word: str):
        self.spell: SpellChecker = SpellChecker(language='ru')
        self.translator: translators = translators
        self.word: str = user_word

    def check_spelling(self):
        if self.spell.correction(self.word) == self.word:
            return self.translate()
        return self.error()

    def translate(self):
        if self.read_csv():
            return self.to_csv([
                self.word.capitalize(),
                self.translator.translate_text(self.word, from_language='ru', to_language='en').capitalize(),
                self.translator.translate_text(self.word, from_language='ru', to_language='fr').capitalize()
            ])
        else:
            return 'Данное слово уже существует.'

    def read_csv(self) -> bool:
        csv = pd.read_csv('results/words.csv')['Russian'].to_dict()
        for index in csv:
            if self.word.capitalize() == csv[index]:
                return False
            continue
        return True

    def to_csv(self, words_list: list):
        columns: list = ['Russian', 'English', 'French']
        df = pd.DataFrame([words_list], columns=columns)
        df.to_csv('results/words.csv', mode='a', header=False, index=False)
        return self.read_csv_to_html()

    @staticmethod
    def read_csv_to_html() -> list:
        file = open('results/words.csv', 'r')
        lines: list = [x.split(',') for x in file.read().splitlines()[1:]]
        return lines

    def error(self) -> str:
        try:
            mistakes: str = ', '.join([mistake.capitalize() for mistake in self.spell.candidates(self.word)])
            return f'Ошибка в написании. Возможно, вы имели ввиду одно из следующих слов: {mistakes}?'
        except TypeError:
            return 'Такого слова не предусмотрено.'

    @staticmethod
    def search(word: str) -> str or list:
        result = []
        with open('results/words.csv') as words:
            words_rows: list = [x.split('\n') for x in words.read().splitlines()[1:]]
            words_pandas: list = pd.read_csv('results/words.csv')
            for title in words_pandas:
                for index, row in enumerate(words_pandas[title]):
                    if word in row:
                        needed_row = ' ,'.join(words_rows[index]).split(',')
                        result.append(needed_row)
                    continue
        return result if len(result) > 0 else 'Совпадений не найдено.'
