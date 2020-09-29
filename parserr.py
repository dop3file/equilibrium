from lexer import lexer
import time
import typess
import exceptions
import locale
import time


locale.setlocale(locale.LC_ALL, "ru")

class Parser:

	def __init__(self,lexemes):
		self.lexemes = lexemes
		self.variables = dict()

	def parser(self):
		try:
			for el in self.lexemes:
				for key,value in el.items():

					if value[-1] == '\n':
						value = value[:-1]

					if key[0] == 'v': #если переменная

						if value == 'scan()':
							value = input()

						if key.split('_')[1] == 'string': # тип данных
							self.variables[key.split('_')[2]] = typess.String(value).return_value()
						elif key.split('_')[1] == 'int':
							self.variables[key.split('_')[2]] = typess.Int(value).return_value()
					elif key[0] == 'f':

						if key.split('_')[1] == 'write':
							print(eval(value,self.variables))

						elif key.split('_')[1] == 'sleep':
							time.sleep(int(value))


		except Exception as e:
			print(e)
			exceptions.Parser_Error('Ошибка парсера')
