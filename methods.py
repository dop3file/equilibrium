import random
import time


def choose_func(value, variables):
    if value.startswith('scan'):  # ввод данных от пользователя
        value = input()

    if value == 'coinflip()':
        value = coin_flip()

    if value == 'time_day()':
        value = get_time_minutes()

    if value == 'time_month()':
        value = get_time_date()

    if value == 'time_unix()':
        value = get_time_unix()

    if value.replace(' ', '').startswith('random'):  # рандом
        value = random_int(value, variables)

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

def get_time_minutes():
    return "'" + time.strftime("%H:%M", time.localtime()) + "'"

def get_time_date():
    return "'" + time.strftime("%x", time.localtime()) + "'"

def get_time_unix():
    return "'" + str(round(time.time())) + "'"




