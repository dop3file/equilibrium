"""
Файл methods
Все функции и методы языка
"""
import random
import os
import time as _time
import typess
import exceptions


files = None
parser = None
sheet = None
time = None


def import_library(name_library):
    """
    Импортирует библиотеки
    :param name_library: имя библиотеки
    :return: None
    """
    if name_library == 'files':
        from library.files import Files
        global files
        files = Files()
    elif name_library == 'parser':
        from library.parser import Parser
        global parser
        parser = Parser()
    elif name_library == 'sheets':
        from library.sheets import Sheets
        global sheet
        parser = Sheets()
    elif name_library == 'time':
        from library.time import Time
        global time
        time = Time()



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
    try:
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

        elif name_func.startswith('random'):  # рандом
            name_func = random_int(name_func, variables)

        elif name_func.startswith('rfile()'):
            global files
            name_func = typess.Array(files.read_file(), variables).return_value()

        elif name_func == 'get_title()':
            name_func = parser.title_page()

        elif name_func.startswith('get_xpath'):
            value = get_arguments_without_key(name_func[9:])

            name_func = parser.get_xpath(eval(value[0], variables))

        elif name_func == 'get_link()':
            name_func = parser.get_link()

        elif name_func.startswith('get_cell'):
            value = get_arguments_without_key(name_func[8:])

            name_func = sheet.read_cell(eval(value[0], variables))

        return name_func

    except AttributeError:
        exceptions.LibraryClassNoImport('Класс библиотеки не импортирован')


def choose_methods(name_method, value, variables):
    """
    Функция агругирует методы
    Методы, это когда cfile => 'Hello,World'!, cfile - функция, а random нет
    :param name_method: названия метода
    :param value: значения, для передачи в функцию
    :param variables: переменные
    :return: None
    """
    try:
        if name_method == 'write':  # функция вывода в консоль
            write(value, variables)

        elif name_method == 'sleep':  # ожидания
            sleep(value, variables)

        elif name_method == 'cfile':
            create_file(value, variables)

        elif name_method == 'wfile':
            write_file(value, variables)

        elif name_method == 'dfile':
            delete_file(value, variables)

        elif name_method == 'ufile':
            update_file(value, variables)

        elif name_method == 'cparser':
            create_connection(value, variables)

        elif name_method == 'mkdir':
            mkdir(value, variables)

        elif name_method == 'csheet':
            import_sheet(value, variables)


    except AttributeError:
        exceptions.LibraryClassNoImport('Класс библиотеки не импортирован')


def coin_flip():
    """
    :return: возвращает рандомно Орёл или решка
    """
    value = random.randint(1, 2)

    return "'Решка'" if value == 1 else "'Орёл'"


def write(value, variables):
    """
    Функция выводит на экран текст
    :param value: значения на вывод
    :param variables: переменные
    :return: None
    """
    try:
        print(eval(str(value), variables), end='')
    except SyntaxError:
        print(value)


def sleep(value, variables):
    """
    Программа "спит" указанное время
    :param value: количество времени для сна
    :return: None
    """
    _time.sleep(float(eval(value, variables)))


def random_int(value, variables):
    """
    :param value: значения
    :param variables: переменные
    :return: рандомное число в диапозоне от first_num до second_num
    """
    first_num = get_arguments_without_key(value)[0][6:]
    second_num = get_arguments_without_key(value)[1]
    return random.randint(int(eval(first_num, variables)), int(eval(second_num, variables)))


def create_file(value, variables):
    files.create_file(eval(value, variables))


def write_file(value, variables):
    files.write_file(eval(value, variables))


def delete_file(value, variables):
    files.delete_file(eval(value, variables))


def update_file(value, variables):
    files.update_file(line=eval(get_arguments_without_key(value)[0], variables),
                      value_for_edit=eval(get_arguments_without_key(value)[1], variables))


def create_connection(value, variables):
    parser.create_connection(eval(value, variables))


def mkdir(name_dir, variables):
    """
    Создаёт папку с названием name_dir, путь указывается от файла скрипта
    :param name_dir: названия файла
    :param variables: переменные
    :return: None
    """
    os.mkdir(eval(name_dir.replace("'", ''), variables))


def import_sheet(name_sheet, variables):
    """
    Инициалзиация класса sheets
    :param name_sheet: названия таблицы, файл должен быть с расширением .xlsx
    :param variables: переменные
    :return: None
    """
    sheet.import_sheets_file(eval(name_sheet, variables))
