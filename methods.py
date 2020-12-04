import random
import library.time as time
from library.files import Files
import typess
import time as _time


files = Files()
variables = 0

def stop_iteration():
    raise StopIteration

def get_arguments_without_key(value):
    value = value.rstrip(' ').lstrip(' ')[1:-1]
    return value.split(",")

def get_arguments_with_key(value):
    value = value.rstrip(' ').lstrip(' ')
    value_prefix = ''
    for char in value:
        if char == '(':
            break
        else:
            value_prefix += char
    value = value[len(value_prefix):]
    return get_arguments_without_key(value)


def choose_func(value, variables):
    if value.startswith('scan'):  # ввод данных от пользователя
        value = input()

    elif value == 'coinflip()':
        value = coin_flip()

    elif value == 'time_day()':
        value = time.get_time_minutes()

    elif value == 'time_month()':
        value = time.get_time_date()

    elif value == 'time_unix()':
        value = time.get_time_unix()

    elif value.replace(' ', '').startswith('random'):  # рандом
        value = random_int(value, variables)

    elif value.startswith('rfile()'):
        return typess.Array(files.read_file(), variables).return_value()

    return value


def choose_methods(name_func, value, variables):
    if name_func == 'write':  # функция вывода в консоль
        write(value, variables)

    elif name_func == 'sleep':  # ожидания
        sleep(value)

    elif name_func == 'cfile':
        create_file(value)

    elif name_func == 'wfile':
        write_file(value)

    elif name_func == 'dfile':
        delete_file(value)

    elif name_func == 'ufile':
        update_file(value)



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
    return random.randint(int(eval(first_num,variables)),int(eval(second_num,variables)))



def create_file(value):
    files.create_file(value)

def write_file(value):
    files.write_file(value)

def delete_file(value):
    files.delete_file(value)

def update_file(value):
    files.update_file(line=get_arguments_without_key(value)[0], value_for_edit=get_arguments_without_key(value)[1])








