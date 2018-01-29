import requests
import sys


def translate_file(source_file, translation_file, from_lang, to_lang='ru'):
    def translate_it(text, to_lang, from_lang):
        API_KEY = 'trnsl.1.1.20180129T193855Z.7f826604e6fa6a11.e07ea3418d58e9fae8e826820ff47fb97454ad52'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

        params = {
            'key': API_KEY,
            'lang': '{}-{}'.format(from_lang, to_lang),
            'text': text
        }

        response = requests.post(URL, params)

        json_ = response.json()
        return ''.join(json_['text'])

    with open(source_file, encoding='utf-8') as file:
        text = file.read()
        translation = translate_it(text, to_lang, from_lang)

        with open(translation_file, 'w', encoding='utf-8') as target_file:
            target_file.write(translation)

source_file, translation_file, from_lang, to_lang = sys.argv[1:]

translate_file(source_file, translation_file, from_lang, to_lang)