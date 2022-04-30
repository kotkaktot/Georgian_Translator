from transliterate import translit
from googletrans import Translator

translator = Translator()


def katoru_translate(text):
    georgian_text = translit(text, 'ka')
    return translator.translate(georgian_text, dest='ru', src='ka').text