from lexer import lexer
import time
import typess
import exceptions
import locale
import time
import random
import methods


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

					if value == 'scan()': #ввод данных от пользователя
						value = "'" + input() + "'"

					if value == 'coinflip()':
						value = methods.coin_flip()

					if value.replace(' ','').startswith('random('): #рандом
						value = random.randint(int(eval(str(value.split(',')[0].replace('random(','')),self.variables)),int(eval(str(value.split(',')[1][:-1]),self.variables)))

					if key[0] == 'v': #если переменная

						if key.split('_')[1] == 'string': # тип данных
							self.variables[key.split('_')[2]] = typess.String(value,self.variables).return_value()
						elif key.split('_')[1] == 'int':
							self.variables[key.split('_')[2]] = typess.Int(value,self.variables).return_value()

					elif key[0] == 'f':

						if key.split('_')[1] == 'write': # функция вывода в консоль
							print(eval(str(value),self.variables))

						elif key.split('_')[1] == 'sleep': #ожидания
							time.sleep(int(value))


		except Exception as e:
			print(e)
			exceptions.Parser_Error('Ошибка парсера')
