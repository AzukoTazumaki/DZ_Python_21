import translators as ts
from spellchecker import SpellChecker as sp
import pandas as pd

translator = ts

# spell = sp(language='ru')
# word = 'Привет'
# if spell.correction(word) == word:
#     x = ts.translate_text(word, from_language='ru', to_language='fr')
#
# else:
#     print('неверно')
#     print(spell.candidates(word))

word = 'Привет'

words = {
                'ru': word.capitalize(),
                'en': ts.translate_text(word, from_language='ru', to_language='en'),
                'fr': ts.translate_text(word, from_language='ru', to_language='fr')
            }

print(words.keys())
