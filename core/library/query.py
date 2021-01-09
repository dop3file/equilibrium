import requests


class Query:
	@staticmethod
	def get_request(url, params):
		if params != 'bad':
			response = requests.get(url=url.replace("'",''),params=eval(params))
		else:
			response = requests.get(url=url.replace("'",''))
		return response.text

	@staticmethod
	def post_request(url, params):
		if params != 'bad':
			response = requests.post(url=url.replace("'",''),params=eval(params))
		else:
			response = requests.post(url=url.replace("'",''))
		return response.text



