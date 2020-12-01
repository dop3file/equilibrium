import random
import time


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




