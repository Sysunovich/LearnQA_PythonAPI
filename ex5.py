'''
Ex5: Парсинг JSON

Давайте создадим пустой Python-скрипт.
Внутри него создадим переменную json_text. Значение этой переменной должно быть таким, как указано тут: https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37

Наша задача с помощью библиотеки “json”, которую мы показывали на занятии, распарсить нашу переменную json_text и вывести текст второго сообщения с помощью функции print.

Ответом должна быть ссылка на скрипт в вашем репозитории.
'''

import json

# some JSON:
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

# Convert from JSON to Python
json_text_pars = json.loads(json_text)
print(json_text_pars)

# Convert from Python to JSON
format_text = json.dumps(json_text_pars, indent=4)
print(format_text)
