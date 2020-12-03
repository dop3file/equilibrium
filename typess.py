import exceptions


def choose_type(value, vars, typess):
	if typess == 'string' and value[0] == "'" and value[-1] == "'":
		return String(value, vars).return_value()
	elif typess == 'int' and isinstance(value, int):
		return Int(value, vars).return_value()
	elif typess == 'array' and isinstance(list(value), list):
		return Array(value, vars).return_value()
	else:
		return value


class Int:
	def __init__(self,value,variables):
		try:

			self.value = eval(str(value),variables)
			x = int(self.value)

		except Exception as e:
			exceptions.Type_Error('Объект не является числом')

	def return_value(self):
		return int(self.value)

class String:
	def __init__(self,value,variables):
		try:
			self.value = eval(str(value),variables)
		except Exception as e:
			exceptions.Type_Error('Объект не является строкой')

	def return_value(self):
		return str(self.value)


class Array:
	def __init__(self,value,variables):
		try:
			self.value = eval(str(value),variables)

		except Exception as e:
			print(e)
			exceptions.Type_Error('Объект не является массивом')

	def return_value(self):
		return self.value
