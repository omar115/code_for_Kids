import googletrans
from googletrans import Translator

translator = Translator()

result = translator.translate('Mitä sinä teet', dest='bengali')

print(result.text)

print(googletrans.LANGUAGES)