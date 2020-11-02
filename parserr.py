from lexer import lexer
import time
import typess
import exceptions
import locale
import time
import random
import methods


class Parser:

	def __init__(self):
		self.variables = dict()


	def add_queue(self,lexemes,line_start):
		'''
		Принимает список лексем и формирует список для выполнения команд
		'''
		line_start,line_end = line_start,line_start
 		
		for line in range(line_start,len(lexemes) - 1):
			if lexemes[line] == {'end_if' : 0}:
				break
			line_end += 1
		list_executable_code = []
		for line in range(line_start,line_end):
			list_executable_code.append(lexemes[line])

		return list_executable_code



	def parser(self,lexemes,tick=1):
		line_count = 1
		lexemes = lexemes
		try:
			for tick in range(tick):
				for el in lexemes:
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
							name_variable = key.split(' ')[0][4::].split('=')[0]
							value_variable = key.split(' ')[0][4::].split('=')[1]
							condition = ''.join(key.split(' ')[1::])
							step = value

							list_executable_code = self.add_queue(lexemes,line_count)

							self.variables[name_variable] = int(value_variable)
							while eval(condition,self.variables):
								if step[0] == '+':
									self.variables[name_variable] += int(step)
								elif step[0] == '-':
									self.variables[name_variable] -= int(step)
								self.parser(list_executable_code)



						if key.startswith('range'):
							list_executable_code = self.add_queue(lexemes,line_count)
							
							parser.parser(self,lexemes=list_executable_code,tick=int(value))

						elif key.startswith('if'):
							try:
								if not eval(value,self.variables): #если условия неверно
									for elem in range(line_count - 1,len(lexemes)): #проходимся по ифу
										if lexemes[elem] == {'end_if': 0}: #если закончился останавливаем цикл
											break
										else:
											del lexemes[elem] #иначе удаляем из лексем

								elif eval(value,self.variables):
									line_end = line_count - 1
									for elem in range(line_end,len(lexemes) - 1): #находим лайн конца цикла
										if lexemes[elem] == {'end_if': 0}:
											break
										else:
											line_end += 1 


							except Exception as e:
								pass

						elif key.startswith('else'):
							pass

						line_count += 1


		except Exception as e:
			print(e)
			exceptions.Parser_Error('Ошибка парсера')
