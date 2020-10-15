import exceptions
import parser


class Int:
	def __init__(self,value,variables):
		try:
			
			self.value = eval(str(value),variables)
			x = int(self.value)

		except ValueError:
			exceptions.type_error('Объект не является числом')
		except Exception as e:
			exceptions.ValueError('Объект не является числом')

	def return_value(self):
		return int(self.value)

class String:
	def __init__(self,value,variables):
		try:
			self.value = eval(str(value),variables)
		except Exception as e:
			exceptions.type_error('Объект не является строкой')

	def return_value(self):
		return str(self.value)
