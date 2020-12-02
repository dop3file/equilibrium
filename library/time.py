import time


def get_time_minutes():
    return "'" + time.strftime("%H:%M", time.localtime()) + "'"

def get_time_date():
    return "'" + time.strftime("%x", time.localtime()) + "'"

def get_time_unix():
    return "'" + str(round(time.time())) + "'"