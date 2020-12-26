'''
Для того что бы получить ответ от сервера, нужно сделать get запрос на /api/
и в params указать JSON с ключём code и значением в виде твоего кода,сервер вернёт ответ в виде JSON
'''
import requests


# URL, на который собираетесь отправлять запрос
url = 'http://127.0.0.1:5000/api'

# Параметры запроса
params = {
    'code': "run 3 > 2",
}

# Ответ
r = requests.get(url=url, params=params)
print(r.text)