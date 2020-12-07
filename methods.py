"""
Файл methods
Все функции и методы языка
"""
import random
import time as _time
import library.time as time
from library.files import Files
from library.parser import Parser
import typess


files = None
parser = None


def get_arguments_without_key(value):
    """
    :param value: функция
    :return: Функция возвращает аргументы, если в
    переданном значении нет ключевых слов
    """
    value = value.rstrip(' ').lstrip(' ')[1:-1]
    return value.split(",")

def get_arguments_with_key(value):
    """
    :param value: функция
    :return: Функция возвращает аргументы, если в
    переданном значении есть ключевые слова
    """
    value = value.rstrip(' ').lstrip(' ')
    value_prefix = ''
    for char in value:
        if char == '(':
            break
        else:
            value_prefix += char
    value = value[len(value_prefix):]
    return get_arguments_without_key(value)


def choose_func(name_func, variables):
    """
    Функция агрегирует функции языка
    :param name_func: строка вызова
    :param variables: переменные
    :return: None
    """
    if name_func.startswith('scan'):  # ввод данных от пользователя
        name_func = input()

    elif name_func == 'coinflip()':
        name_func = coin_flip()

    elif name_func == 'time_day()':
        name_func = time.get_time_minutes()

    elif name_func == 'time_month()':
        name_func = time.get_time_date()

    elif name_func == 'time_unix()':
        name_func = time.get_time_unix()

    elif name_func.replace(' ', '').startswith('random'):  # рандом
        name_func = random_int(name_func, variables)

    elif name_func.startswith('rfile()'):
        global files
        name_func = typess.Array(files.read_file(), variables).return_value()

    elif name_func.startswith('rparser(all)'):
        name_func = parser.get_all_html()

    elif name_func == 'get_title()':
        name_func = parser.title_page()
    

    return name_func


def choose_methods(name_method, value, variables):
    """
    Функция агругирует методы
    Методы, это когда cfile => 'Hello,World'!, cfile - функция, а random нет
    :param name_method: названия метода
    :param value: значения, для передачи в функцию
    :param variables: переменные
    :return: None
    """
    if name_method == 'write':  # функция вывода в консоль
        write(value, variables)

    elif name_method == 'sleep':  # ожидания
        sleep(value)

    elif name_method == 'cfile':
        create_file(value)

    elif name_method == 'wfile':
        write_file(value)

    elif name_method == 'dfile':
        delete_file(value)

    elif name_method == 'ufile':
        update_file(value)

    elif name_method == 'cparser':
        create_connection(value)


def coin_flip():
    value = random.randint(1,2)

    return "'Решка'" if value == 1 else "'Орёл'"


def write(value,variables):
    print(eval(str(value),variables),end='')


def sleep(value):
    _time.sleep(int(value))


def random_int(value,variables):
    first_num = get_arguments_without_key(value)[0][6:]
    second_num = get_arguments_without_key(value)[1]
    return random.randint(int(eval(first_num, variables)), int(eval(second_num, variables)))


def create_file(value):
    global files
    files = Files()
    files.create_file(value)


def write_file(value):
    global files
    files.write_file(value)


def delete_file(value):
    global files
    files.delete_file(value)


def update_file(value):
    global files
    files.update_file(line=get_arguments_without_key(value)[0],
                      value_for_edit=get_arguments_without_key(value)[1])


def create_connection(value):
    global parser
    parser = Parser()
    parser.create_connection(value)




