import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text=None, input_file=None, output_file=None, to_lang='ru', from_lang=None):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    #
    # params = {
    #     'key': API_KEY,
    #     'text': text,
    #     'lang': 'ru-{}'.format(to_lang),
    # }
    #
    # response = requests.get(URL, params=params)
    # json_ = response.json()
    # return ''.join(json_['text'])

    params = {'key': API_KEY,}

    if text:
        params['text'] = text

        if not from_lang:
            params['lang'] = to_lang
            params['options'] = 1
        else:
            params['lang'] = f'{from_lang}-{to_lang}'

        response = requests.get(URL, params=params)
        json_ = response.json()
        return ''.join(json_['text']), json_['code']

    elif input_file and output_file:
        with open(input_file, 'r', encoding='utf-8') as fin:
            text = fin.read()

        params['text'] = text
        if not from_lang:
            params['lang'] = to_lang
            params['options'] = 1
        else:
            params['lang'] = f'{from_lang}-{to_lang}'
        response = requests.get(URL, params=params)
        json_ = response.json()
        with open(output_file, 'w', encoding='utf-8') as fout:
            fout.write(''.join(json_['text']))
        return 0
    raise AttributeError(f'required text or input and output files')


