"""
Файл methods
Все функции и методы языка
"""
import random
import os
import time as _time
import typess
import exceptions


# библиотеки
files = None
parser = None
sheet = None
time = None
query = None
db = None
log = None
math = None
robot = None
app_creator = None

#микросервисы
short_link = None
parser_bank = None


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
        sheet = Sheets()
    elif name_library == 'time':
        from library.time import Time
        global time
        time = Time()
    elif name_library == 'query':
        from library.query import Query
        global query
        query = Query()
    elif name_library == 'db':
        from library.txtdb import TxtDB
        global db
        db = TxtDB()
    elif name_library == 'log':
        from library.log import Logger
        global log
        log = Logger()
    elif name_library == 'math':
        from library._math import Math
        global math
        math = Math()
    elif name_library == 'robot':
        from library.robot import Robot
        global robot
        robot = Robot()
    elif name_library == 'app':
        from library.app_create import AppCreator
        global app_creator
        robot = AppCreator()
        robot.start()

def import_microservice(name_microservice):
    if name_microservice == 'shortLink':
        from microservices.short_link import ShortLink
        global short_link
        short_link = ShortLink()
    elif name_microservice == 'parserBank':
        global parser_bank
        parser_bank = True



def get_arguments_without_key(value):
    """
    :param value: функция
    :return: Функция возвращает аргументы, если в
    переданном значении нет ключевых слов
    """
    value = value.rstrip(' ').lstrip(' ')[1:-1]
    return value.split(",")

def route_func(name_func, variables):
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
        elif name_func.split('(')[0] == 'get':
            value = get_arguments_without_key(name_func[3:])
            name_func = query.get_request(value[0],value[1], variables)
        elif name_func.startswith('post'):
            value = get_arguments_without_key(name_func[4:])
            name_func = query.post_request(value[0],value[1], variables)
        elif name_func.startswith('select_all'):
            value = get_arguments_without_key(name_func[10:])
            name_func = db.select_all(value[0].replace("'",''))
        elif name_func.startswith('select_where'):
            value = get_arguments_without_key(name_func[12:])
            name_func = db.select_where(eval(value[0], variables),
                                        eval(value[1], variables),
                                        eval(value[2], variables))
        elif name_func.startswith('ceil'):
            value = get_arguments_without_key(name_func[4:])
            name_func = math.ceil(str(eval(value[0], variables)))
        elif name_func.startswith('module'):
            value = get_arguments_without_key(name_func[6:])
            name_func = math.math_module(str(eval(value[0], variables)))
        elif name_func.split('.')[0] == 'parserBank' and len(name_func.split('.')) >= 2:
            global parser_bank
            from microservices.parser_bank import ParserBank
            try:
                value = ParserBank(name_func[11:])
            except Exception as e:
                exceptions.MicroserviceError('Ошибка микросервиса')

            name_func = value.return_value

        return name_func

    except AttributeError as e:
        print(e)
        exceptions.LibraryClassNoImport('Класс библиотеки не импортирован')

def route_methods(name_method, value, variables):
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

        elif name_method == 'cdatabase':
            arguments = get_arguments_without_key(value)
            db.create_table(eval(arguments[0], variables),eval(arguments[1], variables))

        elif name_method == 'insertdatabase':
            db.insert(list(eval(value[1:-1], variables)))

        elif name_method == 'editcell':
            arguments = get_arguments_without_key(value)
            sheet.edit_cell(eval(arguments[0], variables),eval(arguments[1], variables))

        elif name_method == 'updatewhere':
            arguments = get_arguments_without_key(value)
            db.update_where(eval(arguments[0], variables),
                            eval(arguments[1], variables),
                            eval(arguments[2], variables),
                            eval(arguments[3], variables))

        elif name_method == 'robot':
            robot.route_move(value)

        elif name_method == 'shortLink':
            short_link.add_link(value)



    except AttributeError as e:
        print(e)
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


def echo(value, variables):
    """
    Функция выводит на экран текст
    :param value: значения на вывод
    :param variables: переменные
    :return: None
    """
    try:
        return eval(str(value), variables)
    except SyntaxError:
        return value


def sleep(value, variables):
    """
    Программа "спит" указанное время
    :param value: количество времени для сна
    :param variables: переменные для eval
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


def create_file(name_file, variables):
    """
    :param name_file: названия файла
    :param variables: переменные
    :return: None
    """
    files.create_file(eval(name_file, variables))


def write_file(value, variables):
    """
    :param value: значения для записи в файл
    :param variables: переменные
    :return: None
    """
    files.write_file(eval(value, variables))


def delete_file(name_file, variables):
    """
    :param name_file: названия файла
    :param variables: переменные
    :return: None
    """
    files.delete_file(eval(name_file, variables))


def update_file(value, variables):
    """
    :param value: значения для обновления
    :param variables: переменные
    :return: None
    """
    files.update_file(line=eval(get_arguments_without_key(value)[0], variables),
                      value_for_edit=eval(get_arguments_without_key(value)[1], variables))


def create_connection(url, variables):
    """
    Функция создаёт подключения с сайтом
    :param url: ссылка на сайт
    :param variables: переменные
    :return: None
    """
    parser.create_connection(eval(url, variables))


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