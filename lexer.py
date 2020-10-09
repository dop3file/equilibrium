import re
import exceptions as excp


class lexer:

    def __init__(self,source):
        ''' Получаем полайново код '''
        self.all_code = []
        with open(source,encoding="utf-8") as source:
            for el in source:
                if el[-1] == '\n':
                    self.all_code.append(el[:-1]) #с помощью шага убираем \n
                else:
                    self.all_code.append(el)
        self.stack = []


    def lexer(self):
        ''' Разбиваем на лексемы '''
        line_count = 0
        for line in self.all_code: #итерирование по строкам
            try:

                line = line.lstrip(' ')
                if line[0] == '>': #комментарии
                    continue

                elif line.replace(' ','') == '}':
                    self.stack += [{'end_if' : 0}]

                elif line.split(' ')[2] == ':=': #переменные
                    self.stack += [{'v_' + line.split(' ')[0] + '_' + line.split(' ')[1] : ''.join(line.split(':=')[1::])[1::]}]

                elif line.split(' ')[1] == '=>': #функции
                    self.stack += [{'f_' + line.split(' ')[0] : ''.join(line.split('=>')[1::])[1::]}]

                elif line.startswith('if'):
                    index_start = self.all_code.index(line) + 1
                    index_end = self.all_code.index('}') + 1

                    self.stack += [{'if_' + line[3:-2] : str(index_start) + '_' + str(index_end)}]

                else:
                    excp.lexer_error('Строка не понятна интерпритатору',line)

                line_count += 1

            except IndexError:
                pass

        return self.stack

lex = lexer('code.eq')
#print(lex.lexer())
