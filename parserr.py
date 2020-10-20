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
		line_count = 1
		try:
			for el in self.lexemes:
				for key,value in el.items():
					value = str(value)

					if value[-1] == '\n':
						value = value[:-1]

					if value == 'scan()': #ввод данных от пользователя
						value = input()

					if value == 'coinflip()':
						value = methods.coin_flip()

					if value.replace(' ','').startswith('random('): #рандом
						value = methods.random_int(value,self.variables)

					if key[0] == 'v': #если переменная
						if key.split('_')[1] == 'string': # тип данных
							if value[0] != "'" and value[-1] != "'":
								value = "'" + str(value) + "'"
							self.variables[key.split('_')[2]] = typess.String(value,self.variables).return_value()
						elif key.split('_')[1] == 'int':
							self.variables[key.split('_')[2]] = typess.Int(value,self.variables).return_value()

					elif key[0] == 'f':

						if key.split('_')[1] == 'write': # функция вывода в консоль
							methods.write(value,self.variables)

						elif key.split('_')[1] == 'sleep': #ожидания
							methods.sleep(value)

					if key.startswith('for'): #циклы
						name_variable = key.split(' ')[0][3::]
						print(name_variable)

					elif key.startswith('if'):
						try:
							if eval(value,self.variables) == False: #если условия неверно
								for elem in range(line_count - 1,len(self.lexemes) - 1): #проходимся по ифу
									if self.lexemes[elem] == {'end_if': 0}: #если закончился останавливаем цикл
										break
									else:
										del self.lexemes[elem] #иначе удаляем из лексем

							if eval(value,self.variables):
								line_end = line_count - 1
								for elem in range(line_end,len(self.lexemes) - 1): #находим лайн конца цикла
									if self.lexemes[elem] == {'end_if': 0}:
										break
									else:
										line_end += 1 

								if self.lexemes[line_end + 1] == {'else' : 'else'}: # если после if идёт else
									for elem in range(line_end + 2,len(self.lexemes) - 1):
										if self.lexemes[elem] == {'end_if': 0}: 
											break
										else:
											del self.lexemes[elem]

						except Exception as e:
							pass

					elif key.startswith('else'):
						pass

					line_count += 1


		except Exception as e:
			print(e)
			exceptions.Parser_Error('Ошибка парсера')
