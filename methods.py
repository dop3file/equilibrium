import random
import library.time as time
from library.files import Files
import typess


files = Files()
variables = 0

def get_arguments(value):
    value = value.rstrip().lstrip()[1:-1]
    return value.split(",")


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


    else:
        return value

    return value



def coin_flip():
    value = random.randint(1,2)

    return "'Решка'" if value == 1 else "'Орёл'"


def write(value,variables):
    print(eval(str(value),variables),end='')


def sleep(value):
    time.sleep(int(value))


def random_int(value,variables):
    return random.randint(int(eval(str(value.split(',')[0].replace('random','').replace('(','')),variables)),
                          int(eval(str(value.split(',')[1][:-1]),variables)))


def cfile(value):
    files.create_file(value)

def wfile(value):
    files.write_file(value)





