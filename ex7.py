'''
Ex7: Запросы и методы

Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE

При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос.
Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом - то параметр method
должен равняться ‘POST’. И так далее.

Надо написать скрипт, который делает следующее:

1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

Не забывайте, что для GET-запроса данные надо передавать через params=
А для всех остальных через data=

Итогом должна быть ссылка на коммит со скриптом и ответы на все 4 вопроса.
'''

import requests

response_get = requests.get("https://playground.learnqa.ru/ajax/api/check_type", params={"param_get_1":"value_1", "param_det_2":"value_2"})
response_post = requests.post("https://playground.learnqa.ru/ajax/api/check_type", data={"data_post_1":"value_1", "data_post_2":"value_2"})
response_put = requests.put("https://playground.learnqa.ru/ajax/api/check_type", data={"data_put_1":"value_1", "data_put_2":"value_2"})
response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/check_type", data={"data_delete_1":"value_1", "data_delete_2":"value_2"})

print(response_get.text)
print(response_post.text)
print(response_put.text)
print(response_delete.text)
