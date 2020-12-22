"""
Файл лексера, который разбивает файл на лексемы
не обрабатывая их логику
"""
import exceptions as excp


class Lexer:
    """ Класс лексера """
    def __init__(self, source):
        """ Получаем полайново код """
        self.all_code = source
        self.stack = []

    def lexer(self):
        """ Разбиваем на лексемы """
        for line in self.all_code:  # итерирование по строкам
            try:
                line = line.lstrip(' ').rstrip(' ').lstrip('\t').rstrip('\t')
                if line[0] == '>':  # комментарии
                    continue

                elif line.startswith('ufather?'):
                    print('Renat Yakublevich')

                elif line.startswith('def_'):
                    self.stack += [{'def_': line[4:].replace(' ','')}]

                elif line.startswith('include'):
                    self.stack += [{'include': line.split(' ')[1]}]

                elif line.startswith('else'):
                    self.stack += [{'else': line.split(' ')[1][:-1]}]

                elif line == '}':
                    self.stack += [{'end_if': 0}]

                elif line.split(' ')[1] == '=>':  # функции
                    self.stack += [{'f_' + line.split('=>')[0].replace(' ',''): ''.join(line.split('=>')[1::])[1::]}]

                elif line.startswith('if'):
                    self.stack += [{'if': line[3:-1]}]

                elif line.startswith('elif'):
                    self.stack += [{'elif': line[5:-1]}]

                elif line.startswith('range'):
                    self.stack += [{'range': line[6:-1]}]

                elif line.startswith('for'):
                    self.stack += [{'for_' + line.split('for')[1].split(',')[0].replace('(','').replace(' ','') + ' ' + line.split(',')[1] : line.split(',')[2].split(')')[0] + ' ' + line.split(')')[1][:-1].replace(' ','')}]

                elif line.startswith('def'):
                    self.stack += [{'def': line.split(' ')[1] + ' ' + line.split(' ')[2][:-1]}]

                elif line.split(' ')[2] == ':=':  # переменные
                    if line.split(' ')[1].find('+') != -1:
                        self.stack += [
                            {'v_' + line.split(' ')[0] + '_' + line.split(' ')[1].split('+')[1]: ''.join(line.split(':=')[1::])[1::]}]
                    else:
                        self.stack += [{'v_' + line.split(' ')[0] + '_' + line.split(' ')[1]: ''.join(line.split(':=')[1::])[1::]}]

                else:
                    excp.Lexer_Error('Строка не понятна интерпритатору',line)

            except IndexError:
                pass

        return self.stack
