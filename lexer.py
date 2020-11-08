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
        for line in self.all_code: #итерирование по строкам
            try:
                line = line.lstrip(' ').rstrip(' ')

                if line[0] == '>': #комментарии
                    continue

                elif line.startswith('else'):
                    self.stack += [{'else' : 'else'}]

                elif line.replace(' ','') == '}':
                    self.stack += [{'end_if' : 0}]

                elif line.startswith('def_'):
                    self.stack += [{'def_' : line[4:].replace(' ','').replace('{','')}]

                elif line.split(' ')[2] == ':=': #переменные
                    self.stack += [{'v_' + line.split(' ')[0] + '_' + line.split(' ')[1] : ''.join(line.split(':=')[1::])[1::]}]

                elif line.split(' ')[1] == '=>': #функции
                    self.stack += [{'f_' + line.split('=>')[0].replace(' ','')  : ''.join(line.split('=>')[1::])[1::]}]

                elif line.startswith('if'):
                    self.stack += [{'if' : line[3:-1]}]

                elif line.startswith('range'):
                    self.stack += [{'range' : line.split('range')[1].replace('{','').replace(' ','')}]

                elif line.startswith('for'):
                    self.stack += [{'for_' + line.split('for')[1].split(',')[0].replace('(','').replace(' ','') + ' ' + line.split(',')[1] : line.split(',')[2].split(')')[0]}]

                elif line.startswith('def'):
                    self.stack += [{'def' : line.split(' ')[1]}]

                else:
                    excp.lexer_error('Строка не понятна интерпритатору',line)

            except IndexError:
                pass

        return self.stack

lex = lexer('code.eq')
print(lex.lexer()) #FOR DEBUG
