import typess
import exceptions
import methods



class Parser:

	def __init__(self):
		self.variables = dict()


	def _for(self, lexemes, key, value, line_count):
		name_variable = key.split(' ')[0][4::].split('=')[0]
		value_variable = key.split(' ')[0][4::].split('=')[1]
		condition = ''.join(key.split(' ')[1::])
		step = value

		list_executable_code = self.add_queue(lexemes, line_count)

		self.variables[name_variable] = int(value_variable)
		while eval(condition, self.variables):
			self.parser(list_executable_code)
			self.variables[name_variable] += int(step)


	def add_queue(self, lexemes, line_start):
		'''
		Принимает список лексем и формирует список для выполнения команд
		:param lexemes: лексемы
		:param line_start: лайн на котором остановились
		:return: None
		'''
		line_start, line_end = line_start, line_start

		for line in range(line_start, len(lexemes) - 1):
			if lexemes[line] == {'end_if': 0}:
				break
			line_end += 1
		list_executable_code = []
		for line in range(line_start, line_end):
			list_executable_code.append(lexemes[line])

		return list_executable_code


	def parser(self, lexemes, tick=1):
		line_count = 1
		lexemes = lexemes
		try:
			for tick in range(tick):
				for el in lexemes:
					for key, value in el.items():
						value = str(value)

						if value[-1] == '\n':
							value = value[:-1]

						if value.startswith('scan'):  # ввод данных от пользователя
							value = input()

						if value == 'coinflip()':
							value = methods.coin_flip()

						if value.replace(' ', '').startswith('random'):  # рандом
							value = methods.random_int(value, self.variables)

						if key[0] == 'v':  # если переменная
							if key.split('_')[1] == 'string':  # тип данных
								if value[0] != "'" and value[-1] != "'":
									value = "'" + str(value) + "'"
								self.variables[key.split('_')[2]] = typess.String(value, self.variables).return_value()
							elif key.split('_')[1] == 'int':
								self.variables[key.split('_')[2]] = typess.Int(value, self.variables).return_value()

							elif key.split('_')[1] == 'array':
								self.variables[key.split('_')[2]] = typess.Array(value, self.variables).return_value()

						if key[0] == 'f':

							if key.split('_')[1] == 'write':  # функция вывода в консоль
								methods.write(value, self.variables)

							elif key.split('_')[1] == 'sleep':  # ожидания
								methods.sleep(value)
						
						if key.startswith('def_'):
							self.parser(self.variables[value])

						if key.startswith('for'):  # циклы
							self._for(lexemes, key, value, line_count)

						if key.startswith('def'):
							list_executable_code = self.add_queue(lexemes, line_count)

							self.variables[value] = list_executable_code

							for elem in range(line_count - 1, len(lexemes)):  # проходимся по ифу
								if lexemes[elem] == {'end_if': 0}:  # если закончился останавливаем цикл
									break
								else:
									del lexemes[elem]  # иначе удаляем из лексем

						if key.startswith('range'):
							list_executable_code = self.add_queue(lexemes, line_count)

							self.parser(list_executable_code, int(value))

						if key.startswith('if'):
							if not eval(value, self.variables):  # если условия неверно
								for elem in range(line_count - 1, len(lexemes)):  # проходимся по ифу
									if lexemes[elem] == {'end_if': 0}:  # если закончился останавливаем цикл
										break
									else:
										del lexemes[elem]  # иначе удаляем из лексем

							elif eval(value, self.variables):
								line_end = line_count - 1
								for elem in range(line_end, len(lexemes) - 1):  # находим лайн конца цикла
									if lexemes[elem] == {'end_if': 0}:
										break
									else:
										line_end += 1

								if lexemes[line_end + 1] == {'else': 'else'}:  # если после if идёт else
									for elem in range(line_end + 2, len(lexemes) - 1):
										if lexemes[elem] == {'end_if': 0}:
											break
										else:
											del lexemes[elem]

						if key.startswith('else'):
							pass

						line_count += 1

		except ValueError:
			exceptions.Value_Error('Ошибка значения')
		except TypeError:
			exceptions.Type_Error('Ошибка типа данных')
		except IndexError:
			exceptions.Index_Error('Ошибка индекса')
		except SyntaxError:
			exceptions.Syntax_Error('Ошибка синтаксиса')
		except Exception as e:
			print(e)
			exceptions.Parser_Error('Ошибка парсера')
