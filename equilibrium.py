""" Файл для сборки eq файла """
import argparse
import sys
from lexer import Lexer
import parserr
import exceptions


cli = argparse.ArgumentParser(description='Equilibrium')
cli.add_argument("--source", default='code.eq', type=str)

class CodeReader:
    def __init__(self, source, level):
        if level == 'PROD':
            self.all_code = []
            with open(source,encoding="utf-8") as source:
                self.all_code = [line.strip() for line in source]
        elif level == 'DEBUG':
            self.all_code = source

    def get_code(self):
        return self.all_code

try:
    class Equilibrium:
        """ Основной класс """
        def __init__(self, source, level):
            self.source = source
            self.level = level

        def run_code(self):
            """ Функция для запуска кода """
            code_read = CodeReader(self.source, self.level).get_code()
            lex = Lexer(code_read)
            pars = parserr.Parser()
            pars.parser(lex.lexer())


    args = cli.parse_args()
    try:
        a = args.source.split('.')[1] != 'eq'
    except IndexError:
        exceptions.FileNoEquilibrium('Файл не имеет расширение .eq')

    Eq = Equilibrium(args.source,'PROD')
    Eq.run_code()

except KeyboardInterrupt:
    print('\nПрограмма завершена!')
    sys.exit()
