import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


class ParserBank:
	def __init__(self, aim_parse):
		ua = UserAgent()
		category_items = {
			'money': self.parse_money_course,
			'weather': self.parse_weather
		}
		self.aim_parse = aim_parse

		self.category = aim_parse.split('.')[0] # категория из category_items
		self.value = aim_parse.split('.')[1]
		self.headers = {'User-Agent': ua.random}

		self.return_value = category_items[self.category]()

	def parse_money_course(self):
		"""
		Парсинг курса валюты в валюту
		Формат запроса: money.currency_to_currency
		Пример: money.usd_to_byn
		"""
		link = 'https://finance.rambler.ru/calculators/converter/1-' + self.value.split('_')[0].upper() + '-' + self.value.split('_')[2].upper()
		html_doc = requests.get(link,self.headers).content
		soup = bs(html_doc,'html.parser')

		convert = soup.findAll('div', {'class': 'converter-display__value'})

		return convert[1].text

	def parse_weather(self):
		"""
		Парсинг прогноза погоды
		Формат запроса: weather.city.param
		Пример: weather.gomel.temp
		"""
		link = f'http://api.openweathermap.org/data/2.5/weather?q={self.aim_parse.split(".")[-2]}&appid=412efa8f683561e258840d1a03be4644'
		weather = requests.get(link, self.headers).json()
		return float(weather['main'][self.aim_parse.split(".")[-1]]) - 273.15

