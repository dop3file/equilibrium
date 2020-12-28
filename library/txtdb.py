import os.path

class TxtDBError:
	def __init__(self, msg):
		print(f'\nОшибка в библиотеке db - {msg}')
		exit()

class NoFileTable(TxtDBError):
	pass

class TableAlreadyCreated(TxtDBError):
	pass

class ThereIsNoSuchColumn(TxtDBError):
	pass

class DatabaseFileAlreadyCreated(TxtDBError):
	pass

class NoTable(TxtDBError):
	pass


class TxtDB:
	def __init__(self,source = None):
		self.source = source
		self.db_colums = []

	def create_table(self,name_file,fields):
		"""
		Метод создаёт файл и макет таблицы с полями
		:param name_file: названия файла
		:param fields: поля, перечисленные через пробел
		:return: None
		"""
		self.source = name_file
		self.count_colums = len(fields.split(' '))

		fields = fields.split(' ')
		if os.path.exists(str(name_file)):
			return
		with open(name_file,'w',encoding='utf-8') as db:
			final_field = ''
			for field in fields:
				final_field += ' | ' + field.replace('|','')
			final_field += '\n' + '―' * len(final_field)
			db.write(final_field)

	def insert(self,values : list):
		"""
		Вставить значения в таблицу
		:param values: значения для заполнения, является массивом
		индекс элемента соответсвует индексу поля
		:return: None
		"""
		with open(self.source,'a',encoding="utf-8") as db:
			final_line = '\n'
			for element in values:
				final_line += ' | ' + str(element)
			else:
				final_line += ' '
			db.write(final_line)

	def select_all(self,column):
		"""
		:param column: столбец
		:return: возвращает все значения по столбцу
		"""
		try:
			all_line_db = self.get_all_db()
			index_column = self.get_colums_db().index(column) + 1
			all_values = []

			for line in all_line_db:
				try:
					value = int(line.split('|')[index_column])
				except ValueError:
					value = line.split('|')[index_column][1:-1]
				all_values.append(value)
			return all_values

		except ValueError:
			ThereIsNoSuchColumn('Такого столбца нет!')

	def select_where(self,column,where,value_where):
		"""
		:param column: названия столбца, которое нужно вернуть
		:param where: названия столбца, по которому искать
		:param value_where: значения столбца, по которому искать
		:return: возвращает значения столбца column
		"""
		try:
			index_column = self.get_colums_db().index(column) + 1
			index_where = self.get_colums_db().index(where) + 1

			all_line_db = self.get_all_db()
			all_values = []

			for line in all_line_db:
				line_split = line.split('|')
				if line_split[index_where][1:-1] == value_where:
					all_values.append(line_split[index_column][1:-1])

			return all_values
		except ValueError:
			ThereIsNoSuchColumn('Такого столбца нет!')

	def update_where(self,update_column,where_column,where_value,value_for_update):
		try:
			all_line = self.get_all_db()
			# TODO доделать
			index_update_column = self.get_colums_db().index(update_column) + 1
			index_where_column = self.get_colums_db().index(where_column) + 1

			for line in range(len(all_line)):
				line_split = all_line[line].split('|')
				if line_split[index_where_column][1:-1] == where_value:
					line_split[index_update_column] = value_for_update
					all_line[line] = ' | '.join(line_split)
			final_value_for_update = '\n'.join(self.get_header_db()) + '\n' + ''.join(all_line)
			with open(self.source,'w') as db:
				db.write('\n' + ''.join(all_line))
		except ValueError as e:
			ThereIsNoSuchColumn('Такого столбца нет!')

	def get_count_colums(self):
		return self.count_colums

	def get_all_db(self):
		try:
			with open(self.source,encoding='utf-8') as all_line:
				return all_line.readlines()[2::]
		except TypeError:
			NoTable('Не инициализирована таблица!')

	def get_colums_db(self):
		with open(self.source,encoding='utf-8') as line:
			all_colums = line.readline().replace(' ','').replace('\n','').split('|')
			return all_colums[1::]

	def get_header_db(self):
		with open(self.source,encoding='utf-8') as line:
			return [l.strip() for l in line][0:2]

	def get_all_line_db(self):
		with open(self.source,encoding='utf-8') as all_line:
			pass



