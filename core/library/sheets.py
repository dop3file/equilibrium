"""
Файл библиотеки sheets для работы с таблицами xls
"""
import openpyxl


class Sheets:
    def __init__(self):
        self.sheet = None
        self.wb = None

    def import_sheets_file(self, name_sheet):
        """
        Инициализация таблицы
        :param name_sheet: названия файла таблицы
        :return: None
        """
        self.name_sheet = name_sheet.replace("'", "")
        self.wb = openpyxl.reader.excel.load_workbook(filename=self.name_sheet)
        self.wb.active = 0
        self.sheet = self.wb.active

    def read_cell(self, index_cell):
        """
        :param index_cell: номер ячейки, пример : A1
        :return: функция возвращает значение ячейка
        """
        value = self.sheet[index_cell.replace("'", "")].value
        return f"'{value}'"

    def edit_cell(self, index_cell, value_for_edit):
        """
        :param index_cell: номер ячейки, пример : A1
        :param value_for_edit: значения для изменение ячейки
        :return: None
        """
        self.sheet[index_cell.replace("'",'')] = value_for_edit.replace("'",'')
        self.wb.save(filename=self.name_sheet)