'''
Для того что бы получить ответ от сервера, нужно сделать get запрос на /api/
и в params указать JSON с ключём code и значением в виде твоего кода,сервер вернёт ответ в виде JSON
'''
import requests


# URL, на который собираетесь отправлять запрос
url = 'http://equilibriumweb.pythonanywhere.com/api'

# Параметры запроса
params = {
    'code': "int a := 10\nrun a",
}

# Ответ
r = requests.get(url=url, params=params)
print(r.text)
