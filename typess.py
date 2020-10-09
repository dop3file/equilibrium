import exceptions
import parser


class Int:
	def __init__(self,value,variables):
		try:
			self.value = eval(value,variables)
			x = int(self.value)
		except Exception as e:
			print(e)
			exceptions.ValueError('Объект не является числом')

	def return_value(self):
		return self.value

class String:
	def __init__(self,value,variables):
		try:
			if value[0] != "'":
				exceptions.type_string_error('Объект не является строкой')
			self.value = eval(str(value),variables)
		except Exception as e:
			print(e)
			exceptions.type_string_error('Объект не является строкой')

	def return_value(self):
		return self.value
