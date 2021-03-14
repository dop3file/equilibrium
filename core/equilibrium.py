""" Файл для сборки eq файла """
import argparse
import sys
from lexer import Lexer
import parserr
import exceptions
from datetime import datetime
import time


cli = argparse.ArgumentParser(description='Equilibrium')
cli.add_argument("--source", default='code.eq', type=str)
cli.add_argument("--interactive", default=0, type=int)
cli.add_argument("--compile", default=False, type=bool)
cli.add_argument("--speed", default=False, type=bool)
cli.add_argument("--support", default=False, type=bool)

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
        code_read = CodeReader(self.source, self.level).get_code() # код разбитый по лайнам
        lex = Lexer(code_read) # лексер, возвращающий лексемы
        parser = parserr.Parser() # парсер, обрабатывающий логику
        parser.parser(lex.lexer())

class SpeedTest:
    def __init__(self, source):
        self.source = source

    def analysis_speed(self):
        before_start = time.time()
        eq = Equilibrium(self.source, 'PROD')
        eq.run_code()
        after_end = time.time()
        return datetime.utcfromtimestamp(after_end - before_start).strftime('%H часов %M минут %S секунд %f микросекунд')

def route_args(args):
    """
    Функция отвечате за режимы сборки программы на Equilibrium
    --compile True/False default - компилируемый режим, где нужно указать путь к файлу в консоле
    --interactive 0 default/1/2 - интерактивный режим,1 - режим когда ты пишешь команды, а когда
    хочешь запустить их на выполения пишешь go/run.2 - каждая команда запускается на выполнения
    автоматически
    --source - обычное выполнение программы, для запуска нужно указать путь к файлу с .eq
    default значения - code.eq
    --speed - если True, то выводит скорость выполнения программы из source
    default значения - False
    """
    if args.support:
        help_string = """
Привет, это справочная информация об языке Equilibrium
------------------------------------------------------
Методы:
write - вывод информации в консоль
sleep - ожидания определённое количество секунд
cfile - создания файла
wfile - запись файла
        """
        print(help_string)
    if args.speed:
        speed_test = SpeedTest(args.source)
        print(f'Программа отработала за {speed_test.analysis_speed()}')
    if args.source:
        eq = Equilibrium(args.source,'PROD')
        eq.run_code()
    elif args.compile:
        print('Привет,это компилируемый режим Equilibrium')
        way_to_file = input('Введи путь к файлу: ')
        eq = Equilibrium(way_to_file, 'PROD')
        eq.run_code()
    elif args.interactive:
        print('Привет!\nЭто интерактивный режим Equilibrium\nВводи команды и когда захочешь запустить программу напиши go')
        command_list = []
        while True:
            command = input('\n>>> ')
            
            if command.lower() in ('exit','quit'):
                sys.exit()
            if args.interactive == 1:
                if command.lower() in ('run', 'go'):
                    Eq = Equilibrium(command_list, 'DEBUG')
                    Eq.run_code()
                else:
                    command_list.append(command)
            elif args.interactive == 1:
                eq = Equilibrium([command], 'DEBUG')
                eq.run_code()
            else:
                exceptions.BuildError('Ошибка сборки')


try:
    args = cli.parse_args()
    try:
        a = args.source.split('.')[1] != 'eq'
    except IndexError:
        exceptions.FileNoEquilibrium('Файл не имеет расширение .eq')

    route_args(args)
except FileNotFoundError:
    print('Такого файла нет!')
except KeyboardInterrupt:
    print('\nПрограмма завершена!')
except Exception as e:
    print(e)
    print('Ошибка..')
