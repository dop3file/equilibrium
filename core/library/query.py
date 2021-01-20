import requests


class Query:
	@staticmethod
	def get_request(url, params, variables):
		if params != 'bad':
			response = requests.get(url=eval(url, variables),params=eval(params, variables))
		else:
			response = requests.get(url=eval(url, variables))
		return response.text

	@staticmethod
	def post_request(url, params, variables):
		if params != 'bad':
			response = requests.post(url=eval(url, variables),params=eval(params, variables))
		else:
			response = requests.post(url=eval(url, variables))
		return response.text



