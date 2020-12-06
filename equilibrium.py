""" Файл для сборки eq файла """
import argparse
import sys
from lexer import Lexer
import parserr
import exceptions


cli = argparse.ArgumentParser(description='Equilibrium')
cli.add_argument("--source", default='code.eq', type=str)

try:
    class Equilibrium:
        """ Основной класс """
        def __init__(self, source):
            self.source = source

        def run_code(self):
            """ Функция для запуска кода """
            lex = Lexer(self.source)
            pars = parserr.Parser()
            pars.parser(lex.lexer())


    args = cli.parse_args()
    try:
        a = args.source.split('.')[1] != 'eq'
    except IndexError:
        exceptions.FileNoEquilibrium('Файл не имеет расширение .eq')

    Eq = Equilibrium(args.source)
    Eq.run_code()

except KeyboardInterrupt:
    print('\nПрограмма завершена!')
    sys.exit()
