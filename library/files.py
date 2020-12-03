import os
import exceptions


class Files:
    def __init__(self):
        pass

    def create_file(self, name_file):
        self.name_file_prev = name_file.replace("'","")
        self.name_file = open(name_file.replace("'",""),'a',encoding='utf-8')
        return self.name_file

    def write_file(self, text):
        self.name_file.write(text.replace("'",""))

    def read_file(self):
        self.name_file.close()
        with open(self.name_file_prev, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
        self.name_file = open(self.name_file_prev, 'a', encoding='utf-8')

    def delete_file(self, value):
        try:
            self.name_file.close()
        except AttributeError:
            exceptions.File_Connection('Файл не подключён')
        os.remove(value.replace("'",""))

    def update_file(self, line, value_for_edit):
        try:
            self.name_file.close()
        except AttributeError:
            exceptions.File_Connection('Файл не подключён')
        with open(self.name_file_prev,'r', encoding='utf-8') as file:
            all_files = [line.strip() for line in file]
            all_files[int(line)] = value_for_edit.replace("'","")

        with open(self.name_file_prev,'w', encoding='utf-8') as file:
            file.write('\n'.join(all_files))
        self.name_file = open(self.name_file_prev,'a',encoding='utf-8')







