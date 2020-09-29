import exceptions


class Int:
	def __init__(self,value):
		try:
			self.value = eval(value)
			x = int(self.value)
		except Exception:
			exceptions.ValueError('Объект не является числом')

	def return_value(self):
		return self.value

class String:
	def __init__(self,value):
		try:
			if value[0] != "'" and value[-1] != "'":
				exceptions.type_string_error('Объект не является строкой')
			self.value = eval(value)
		except Exception:
			exceptions.type_string_error('Объект не является строкой')

	def return_value(self):
		return self.value


