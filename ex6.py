"""
Ex6: Длинный редирект
Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect

С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой.
И какой URL итоговый.

Ответ опубликуйте в виде ссылки на коммит со скриптом, а также укажите количество редиректов и конечный URL.
"""

import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

# solution with for
for resp in response.history:
    print(resp.url, resp.text)

# solution with simple
first_response = response.history[0]
second_response = response
print("") # new line
print(first_response.url)
print(second_response.url)