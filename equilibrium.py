from lexer import Lexer
import parserr
import argparse


cli = argparse.ArgumentParser(description='Equilibrium')
cli.add_argument("--source", default='code.eq', type=str)

try:

	class Equilibrium:
		""" Основной класс """

		def __init__(self,source):
			self.source = source

		def run_code(self):
			lex = Lexer(self.source)
			pars = parserr.Parser()
			pars.parser(lex.lexer())

	args = cli.parse_args()

	Eq = Equilibrium(args.source)
	Eq.run_code()

except KeyboardInterrupt:
	print('\nПрограмма завершена!')
	exit()
