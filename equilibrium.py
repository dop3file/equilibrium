from lexer import lexer
import parserr
import argparse

cli = argparse.ArgumentParser(description='Equilibrium')
cli.add_argument("--source", default='code.eq', type=str)

class Equilibrium:
	''' Основной класс '''

	def __init__(self,source):
		self.source = source

	def run_code(self):
		lex = lexer(self.source)
		pars = parserr.Parser(lex.lexer())
		pars.parser()

args = cli.parse_args()

Eq = Equilibrium(args.source)
Eq.run_code()
