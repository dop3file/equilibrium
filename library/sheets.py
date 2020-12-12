import openpyxl


class Sheets:
    def __init__(self):
        self.sheet = None
        self.wb = None

    def import_sheets_file(self, name_sheet):
        self.wb = openpyxl.reader.excel.load_workbook(filename=name_sheet.replace("'", ""))
        self.wb.active = 0
        self.sheet = self.wb.active

    def read_cell(self, index_cell):
        """
        :param index_cell: номер ячейки, пример : A1
        :return: функция возвращает значение ячейка
        """
        return self.sheet[index_cell.replace("'", "")].value
