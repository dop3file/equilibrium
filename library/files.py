"""
Файл библиотеки files
"""
import os
import exceptions


class Files:
    def __init__(self):
        self.name_file = ''
        self.name_file_prev = ''

    def create_file(self, name_file):
        """
        Создаёт файл, и инициализирует файл в классе
        :param name_file: названия файла с расширением
        :return: возвращает название файла
        """
        self.name_file_prev = name_file.replace("'", "")
        self.name_file = open(name_file.replace("'", ""), 'a', encoding='utf-8')

    def write_file(self, text):
        """
        Записывает text в иницилиазированный файл
        :param text: текст для записи
        :return: None
        """
        self.name_file.write(text.replace("'", ""))

    def read_file(self):
        """
        Читает инициализированный файл
        :return: возвращает весь файл, разбитый по строчкам на список
        """
        self.name_file.close()
        with open(self.name_file_prev, 'r', encoding='utf-8') as file:
            all_lines = [line.strip() for line in file]
        self.name_file = open(self.name_file_prev, 'a', encoding='utf-8')
        return all_lines

    def delete_file(self, name_file):
        """
        Удаляет выбранный файл
        :param name_file: названия файла с расширением
        :return: None
        """
        try:
            self.name_file.close()
        except AttributeError:
            exceptions.File_Connection('Файл не подключён')
        os.remove(name_file.replace("'", ""))

    def update_file(self, line, value_for_edit):
        """
        Обновляет инициализрованный файл
        :param line: лайн на котором нужно инициализировать(с учётом что подсчёт с 0)
        :param value_for_edit: текст для обновления
        :return: None
        """
        try:
            self.name_file.close()
        except AttributeError:
            exceptions.File_Connection('Файл не подключён')
        with open(self.name_file_prev, 'r', encoding='utf-8') as file:
            all_files = [line.strip() for line in file]
            all_files[int(line)] = value_for_edit.replace("'","")

        with open(self.name_file_prev, 'w', encoding='utf-8') as file:
            file.write('\n'.join(all_files))
        self.name_file = open(self.name_file_prev,'a',encoding='utf-8')
