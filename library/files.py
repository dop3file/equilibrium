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




