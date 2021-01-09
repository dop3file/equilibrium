import requests


url = 'http://equilibriumweb.pythonanywhere.com/api'

# Параметры запроса
params = {
    'code': """
    include time
    run 3 > 2
    run time_month()
    """

}


# Ответ : True, 29/12/2020
response = requests.get(url=url, params=params)
print(response.text)

