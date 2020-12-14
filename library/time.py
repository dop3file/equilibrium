"""
Файл библиотеки time
"""
import time


class Time:
    @staticmethod
    def get_time_minutes():
        """
        Возвращает время в формате часы:минуты
        """
        return f"'{time.strftime('%H:%M')}'"

    @staticmethod
    def get_time_date():
        """
        Возвращает дату в формате месяц/число/2 последних цифры года
        """
        return f"'{time.strftime('%x')}'"

    @staticmethod
    def get_time_unix():
        """
        Возращает время в формате unix(отсчёт с 1970 по секундам)
        """
        return f"'{str(round(time.time()))}'"
