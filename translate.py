import translators
from spellchecker import SpellChecker
import pandas as pd


class Translate:
    def __init__(self, user_word: str):
        self.spell = SpellChecker(language='ru')
        self.translator = translators
        self.word = user_word

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

    def read_csv(self):
        csv = pd.read_csv('results/words.csv')['Russian'].to_dict()
        for index in csv:
            if self.word.capitalize() == csv[index]:
                return False
            continue
        return True

    @staticmethod
    def to_csv(words_list: list):
        columns = ['Russian', 'English', 'French']
        df = pd.DataFrame([words_list], columns=columns)
        df.to_csv('results/words.csv', mode='a', header=False, index=False)

    def error(self):
        try:
            mistakes = ', '.join([mistake.capitalize() for mistake in self.spell.candidates(self.word)])
            return f'Ошибка в написании. Возможно, вы имели ввиду одно из следующих слов: {mistakes}'
        except TypeError:
            return 'Такого слова не предусмотрено.'


word = input('Введите слово\n>>> ')
x = Translate(word).check_spelling()
print(x)
