class Excp_lexer:
	def __init__(self,msg,line_warning):
		print(f'{msg}\n{line_warning}')
		exit()

class Excp:
	def __init__(self,msg):
		print(f'Ошибка - {msg}')
		exit()

class lexer_error(Excp_lexer):
	pass

class type_string_error(Excp):
	pass

class type_error(Excp):
	pass

class Value_Error(Excp):
	pass

class Parser_Error(Excp):
	pass

class Type_Error(Excp):
	pass
class Index_Error(Excp):
	pass
