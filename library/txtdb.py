import os.path

from exceptions import TableAlreadyCreated
from exceptions import DatabaseFileAlreadyCreated
from exceptions import ThereIsNoSuchColumn
from exceptions import NoTable
from exceptions import NoFileTable


class TxtDB:
	def __init__(self,source = None):
		self.source = source
		self.db_colums = []

		if source != None:
			try:
				with open(source,'r',encoding='utf-8') as file:
					colums = file.readlines(1)[0].split('|')[1::]

					for colum in colums:
						self.db_colums.append(colum[1:-1])
				self.count_colums = len(self.db_colums)
			except FileNotFoundError:
				raise NoFileTable('Файл таблицы был не найден')


	def create_table(self,name,fields):
		if self.source != None:
			raise TableAlreadyCreated('Таблица была передана аргументом в класс!')

		self.source = name
		self.count_colums = len(fields.split(' '))

		if os.path.exists(name):
			return

		fields = fields.split(' ')
		with open(name,'w',encoding='utf-8') as db:
			final_field = ''
			for field in fields:
				final_field += ' | ' + field.replace('|','')
			final_field += '\n' + '―' * len(final_field)
			db.write(final_field)



	def insert(self,values : list):
		with open(self.source,'a',encoding="utf-8") as db:
			final_line = '\n'
			for element in values:
				final_line += ' | ' + str(element)
			else:
				final_line += ' '
			db.write(final_line)

	def select_all(self,column):
		try:
			all_line_db = self.get_all_db()

			index_column = self.get_colums_db().index(column) + 1
			all_values = []

			for line in all_line_db:
				try:
					value = int(line.split('|')[index_column][1:-1])
				except ValueError:
					value = line.split('|')[index_column][1:-1]
				all_values.append(value)

			return all_values

		except ValueError:
			raise ThereIsNoSuchColumn('Такого столбца нет!')

	def select_where(self,column,where,value_where):
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
			raise ThereIsNoSuchColumn('Такого столбца нет!')

	def update_where(self,update_column,where_column,where_value,value_for_update):
		all_line = self.get_all_db()

		index_update_column = self.get_colums_db().index(update_column) + 1
		index_where_column = self.get_colums_db().index(where_column) + 1

		for line in range(len(all_line)):
			line_split = all_line[line].split('|')
			if line_split[index_where_column][1:-1] == where_value:
				line_split[index_update_column] = value_for_update
				all_line[line] = ' | '.join(line_split)
		print(''.join(self.get_header_db() + all_line))
		with open(self.source,'w') as db:
			db.write(''.join(self.get_header_db() + all_line))

	def get_count_colums(self):
		return self.count_colums

	def get_all_db(self):
		try:
			with open(self.source,encoding='utf-8') as all_line:
				return all_line.readlines()[2::]
		except TypeError:
			raise NoTable('Не инициализирована таблица!')

	def get_colums_db(self):
		with open(self.source,encoding='utf-8') as line:
			all_colums = line.readline().replace('\n','')
			return all_colums.split(' | ')[1::]

	def get_header_db(self):
		with open(self.source,encoding='utf-8-sig') as line:
			all_colums = line.readlines()
			return all_colums[0:2]

	def get_all_line_db(self):
		with open(self.source,encoding='utf-8') as all_line:
			pass

db = TxtDB()
db.create_table('users.txt','user password')

