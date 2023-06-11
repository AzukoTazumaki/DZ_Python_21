import translators
from spellchecker import SpellChecker
import pandas as pd
import re


class Translate:
    def __init__(self, word: dict):
        self.spell: SpellChecker = SpellChecker(language='ru')
        self.translator: translators = translators
        self.word: dict = word

    def check_spelling(self):
        if self.spell.correction(self.word['word_translate']) == self.word['word_translate']:
            return self.translate()
        return self.error()

    def translate(self):
        if self.read_csv():
            return self.to_csv([
                self.word['word_translate'].capitalize(),
                self.translator.translate_text(self.word['word_translate'], from_language='ru', to_language='en').capitalize(),
                self.translator.translate_text(self.word['word_translate'], from_language='ru', to_language='fr').capitalize()
            ])
        else:
            return 'Данное слово уже существует.'

    def read_csv(self) -> bool:
        csv: dict = pd.read_csv('results/words.csv')['Russian'].to_dict()
        for index in csv:
            if self.word['word_translate'].capitalize() == csv[index]:
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
        if len(word.replace(r'\s+', '')) > 0:
            result: list = []
            with open('results/words.csv') as words:
                words_rows: list = [x.split('\n') for x in words.read().splitlines()[1:]]
                words_pandas: list = pd.read_csv('results/words.csv')
                for title in words_pandas:
                    for index, row in enumerate(words_pandas[title]):
                        if word in row:
                            needed_row: str = ' ,'.join(words_rows[index]).split(',')
                            result.append(needed_row)
                        continue
            return result if len(result) > 0 else 'Совпадений не найдено.'
        return 'Вы ничего не ввели, чтобы искать'


class UDTranslate(Translate):
    def __init__(self, word: dict):
        super().__init__(word)

    def update(self):
        update_id: int = int(self.word['word_translate_id_update']) - 1
        word_english: str = self.word['word_translate_english']
        word_french: str = self.word['word_translate_french']
        file = pd.read_csv('results/words.csv')
        if 1 < update_id < len(file['Russian']):
            file.loc[update_id, 'English'] = word_english \
                if len(re.sub(r'\s+', '', word_english)) != 0 else file.loc[update_id, 'English']
            file.loc[update_id, 'French'] = word_french \
                if len(re.sub(r'\s+', '', word_french)) != 0 else file.loc[update_id, 'French']
            file.to_csv('results/words.csv', index=False, mode='w')
            return self.read_csv_to_html()
        return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'

    def delete(self):
        delete_id: int = int(self.word['word_translate_id_delete']) - 1
        file = pd.read_csv('results/words.csv')
        if 1 < delete_id < len(file['Russian']):
            file.drop(delete_id, inplace=True)
            file.to_csv('results/words.csv', index=False, mode='w')
            return self.read_csv_to_html()
        return 'Введенный ID недопустим. Вы ввели ID за пределами границ таблицы.'
