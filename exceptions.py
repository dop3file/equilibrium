"""
Файл Exceptions
Обработка ошибок
"""

class Lexer_Error():
	def __init__(self, msg, line_warning):
		print(f'{msg}\n{line_warning}')
		exit()


class Excp:
	def __init__(self, msg):
		print(f'Ошибка - {msg}')
		exit()


class Value_Error(Excp):
	pass


class Parser_Error(Excp):
	pass


class Type_Error(Excp):
	pass


class Index_Error(Excp):
	pass


class Syntax_Error(Excp):
	pass


class Key_Error(Excp):
	pass


class File_Exists(Excp):
	pass


class OS_Error(Excp):
	pass


class Zero_Error(Excp):
	pass


class File_Connection(Excp):
	pass


class Name_Error(Excp):
	pass


class FileNoEquilibrium(Excp):
	pass

class LibraryClassNoImport(Excp):
	pass
