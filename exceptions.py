class Excp:
	def __init__(self,msg,line_warning):
		print(f'{msg}\n{line_warning}')
		exit()

class interpreter_dontknow(Excp):
	pass