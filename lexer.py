import re
import exceptions as excp


class lexer:

    def __init__(self,source):
        ''' Получаем полайново код '''
        self.all_code = []
        with open(source,encoding="utf-8") as source:
            for el in source:
                self.all_code.append(el[0:]) #с помощью шага убираем \n
        self.stack = []

    def lexer(self):
        ''' Разбиваем на лексемы '''
        for line in self.all_code: #итерирование по строкам
            
            if line.split(' ')[2] == ':=': #переменные 
                self.stack += [{'v_' + line.split(' ')[0] + '_' + line.split(' ')[1] : ''.join(line.split(':=')[1::])[1::]}]
 
            elif line.split(' ')[1] == '=>': #функции
                self.stack += [{'f_' + line.split(' ')[0] : ''.join(line.split('=>')[1::])[1::]}]
                
            else:
                excp.lexer_error('Строка не понятна интерпритатору',line)

        return self.stack


lex = lexer('code.eq')
#print(lex.lexer())

