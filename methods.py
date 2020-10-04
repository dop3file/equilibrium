import random


def coin_flip():
    value = random.randint(1,2)
    if value == 1:
        value = "'Решка'"
    else:
        value = "'Орёл'"

    return value
