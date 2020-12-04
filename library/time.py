import time


def get_time_minutes():
    """
    Возвращает время в формате часы:минуты
    """
    return "'" + time.strftime("%H:%M", time.localtime()) + "'"

def get_time_date():
    """
    Возвращает дату в формате месяц/число/2 последних цифры года
    """
    return "'" + time.strftime("%x", time.localtime()) + "'"

def get_time_unix():
    """

    """
    return "'" + str(round(time.time())) + "'"