"""
Файл лексера, который разбивает файл на лексемы
не обрабатывая их логику
"""
import exceptions as excp
import re


class Lexer:
    """ Класс лексера """
    def __init__(self, source):
        """ Получаем полайново код """
        self.all_code = source
        self.stack = []
        self.lexemes_instructions = {
            'delete': lambda line: [{'delete': line.split(' ')[1]}],
            'def_': lambda line: [{'def_': line[4:].replace(' ', '')}],
            'include': lambda line: [{'include': line.split(' ')[1]}],
            'else': lambda line: [{'else': line.split(' ')[1][:-1]}],
            '}': lambda line: [{'end_if': 0}],
            'if': lambda line: [{'if': line[3:-1]}],
            'run': lambda line: [{'run': line[4::]}],
            'elif': lambda line: [{'elif': line[5:-1]}],
            'range': lambda line: [{'range': line[6:-1]}],
            'for': lambda line: [{'for_' + line.split('for')[1].split(',')[0].replace('(', '').replace(' ', '') + ' ' + line.split(',')[1]: line.split(',')[2].split(')')[0] + ' ' + line.split(')')[1][:-1].replace(' ', '')}],
            'def': lambda line: [{'def': line.split('(')[0].split(' ')[1] + ' ' + line.split(' ')[-1][:-1] + ' ' + line.split('(')[1].split(')')[0]}],
            'import': lambda line: [{'import': line[7:]}],
            'quit': lambda line: [{'quit': 'quit'}],
            'while': lambda line: [{f'while_{line[-3:-1]}': line[6:-3]}],
            'do': lambda line: [{f'do while_{line[-3:-1]}': line[9:-3]}],
            'use': lambda line: [{'use': line[4:]}]
        }

    def lexer(self):
        """ Разбиваем на лексемы """
        for line in self.all_code:
            try:
                line = line.lstrip(' ').rstrip(' ').lstrip('\t').rstrip('\t')
                if line.split(' ')[0] in self.lexemes_instructions:
                    self.stack.extend(self.lexemes_instructions[line.split(' ')[0]](line))
                elif line.startswith('ufather?'):
                    print('Renat Yakublevich')
                elif re.findall(r'\S+ =>',line) or re.findall(r'\S+=>',line):  # функции
                    self.stack += [{'f_' + line.split('=>')[0].replace(' ',''): ''.join(line.split('=>')[1::])[1::]}]
                elif re.findall('\S+ \S+ :=',line) or re.findall('\S+ \S+:=',line):  # переменные
                    if line.split(' ')[1].find('+') != -1:
                        self.stack += [
                            {'variable_' + line.split(' ')[0] + '_' + line.split(' ')[1].split('+')[1]: ''.join(line.split(':=')[1::])[1::]}]
                    else:
                        self.stack += [{'variable_' + line.split(' ')[0] + '_' + line.split(' ')[1]: ''.join(line.split(':=')[1::])[1::]}]
                elif not line or line.startswith('>'):
                    continue
                else:
                    excp.Lexer_Error('Строка не понятна интерпритатору',line)
            except IndexError as e:
                print(e)

        return self.stack