""" Файл для сборки eq файла """
import argparse
import sys
from lexer import Lexer
import parserr
import exceptions


cli = argparse.ArgumentParser(description='Equilibrium')
cli.add_argument("--source", default='code.eq', type=str)
cli.add_argument("--interactive", default=0, type=int)

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

class Equilibrium:
    """ Основной класс """
    def __init__(self, source, level):
        self.source = source
        self.level = level

    def run_code(self):
        """ Функция для запуска кода """
        code_read = CodeReader(self.source, self.level).get_code()
        lex = Lexer(code_read)
        parser = parserr.Parser()
        parser.parser(lex.lexer())

try:
    args = cli.parse_args()
    try:
        a = args.source.split('.')[1] != 'eq'
    except IndexError:
        exceptions.FileNoEquilibrium('Файл не имеет расширение .eq')

    if not args.interactive:
        Eq = Equilibrium(args.source,'PROD')
        Eq.run_code()
    else:
        print('Привет!\nЭто интерактивный режим Equilibrium\nВводи команды и когда захочешь запустить программу напиши go')
        command_list = []
        while True:
            command = input('\n>>> ')
            if args.interactive == 1:
                if command == 'go':
                    Eq = Equilibrium(command_list, 'DEBUG')
                    Eq.run_code()
                elif command in ('exit','quit'):
                    sys.exit()
                else:
                    command_list.append(command)
            else:
                Eq = Equilibrium([command], 'DEBUG')
                Eq.run_code()

except FileNotFoundError:
    print('Такого файла нет!')
except KeyboardInterrupt:
    print('\nПрограмма завершена!')
