import exceptions


class Int:
	def __init__(self,value):
		try:
			self.value = eval(value)
			x = int(self.value)
		except Exception as e:
			print(e)
			exceptions.ValueError('Объект не является числом')

	def return_value(self):
		return self.value

class String:
	def __init__(self,value):
		try:
			self.value = value
		except Exception as e:
			print(e)
			exceptions.type_string_error('Объект не является строкой')

	def return_value(self):
		return self.value
