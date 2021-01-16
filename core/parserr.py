"""
Файл парсер
Обработка логики и её выполнения
"""
import typess
import exceptions
import methods
import math
from lexer import Lexer


class Parser:
    def __init__(self):
        # переменные
        self._variables = {
            'ok' : True,
            'bad' : False,
            'pi' : math.pi,
            'e' : math.e
            }
        self.web_output = [] 

    def get_web_output(self):
        return self.web_output

    def _for(self, lexemes, key, value, line_count):
        """
        Пока condition == True, исполняется код от позиции for до count executions
        :param lexemes: лексемы
        :param key: ключ из главных лексем
        :param value: значения из главных лексем
        :param line_count: лайн, где распологается for
        :return: None

        name_variable - имя переменной цикла
        value_variable - значения переменной цикла
        condition - значения, если True - цикл продолжает итерироваться, False - прекращает
        step - значения, который прибавляется к переменной(может быть отрицательным)
        count_lines - поле видимости цикла(сколько команд из лексем заключено в цикле)
        """
        name_variable = key.split(' ')[0][4::].split('=')[0].lstrip(' ').rstrip(' ')
        value_variable = key.split(' ')[0][4::].split('=')[1].lstrip(' ').rstrip(' ')
        condition = ' '.join(key.split(' ')[1::]).lstrip(' ').rstrip(' ')

        step = value.lstrip(' ').split(' ')[0].replace(' ','')
        count_lines = int(value.split(' ')[1])

        self._variables[name_variable] = int(value_variable)
        while eval(condition, self._variables):
            self.parser(lexemes[line_count: line_count + count_lines])
            self._variables[name_variable] += int(eval(step, self._variables))


    def parser(self, lexemes, tick=1):
        """
        Функция, где проходит основный цикл выполнения
        key - ключ из лексемы
        value - значения из лексемы
        :param lexemes: лексемы, для выполнения
        :param tick: количество проходов по лексем, по дефолту 1(так как нет цикла for или range)
        :return: None
        """
        # print(lexemes) # FOR DEBUG
        line_count = 1
        lexemes = lexemes
        try:
            for tick in range(tick):
                for el in lexemes:
                    for key, value in el.items():
                        value = str(value)
                        key = str(key)
                        methods.variables = self._variables
                        value = methods.choose_func(value, self._variables)

                        if key[0] == 'v':  # переменные
                            '''
                            Типы данных
                            Каждое из ветвлений записывает в переменную значения
                            Тип значения определяет функция choose_type
                            '''
                            if key.split('_')[1] == 'string':  # тип данных
                                if value[0] != "'" and value[-1] != "'":
                                    value = "'" + str(value) + "'"
                                self._variables[key.split('_')[2]] = typess.choose_type(value, self._variables, 'string')

                            elif key.split('_')[1] == 'int':
                                self._variables[key.split('_')[2]] = typess.choose_type(value, self._variables, 'int')

                            elif key.split('_')[1] == 'array':
                                self._variables[key.split('_')[2]] = typess.choose_type(value, self._variables, 'array')

                            elif typess.choose_type(value, self._variables, 'array') == value:
                                self._variables[key.split('_')[2]] = self._variables[value]

                            elif key.split('_')[1] == 'float':
                                self._variables[key.split('_')[2]] = typess.choose_type(value, self._variables, 'float')

                            elif key.split('_')[1] == 'char':
                                self._variables[key.split('_')[2]] = typess.choose_type(value, self._variables, 'char')

                            elif key.split('_')[1] == 'bool':
                                self._variables[key.split('_')[2]] = typess.choose_type(value, self._variables, 'bool')

                        if key[0] == 'f':  # если функция
                            methods.choose_methods(key.split('_')[1], value, self._variables)

                        if key == 'def_':  # вызов функций
                            self.parser(self._variables[value])

                        if key == 'run':
                            """
                            Команда отвечает за вывод информации в веб версии
                            """
                            self.web_output.append(methods.echo(value, self._variables))

                        if key.startswith('for'):  # циклы
                            self._for(lexemes, key, value, line_count)

                        if key == 'import': # импортирования файлов .eq
                            with open(f'{value}.eq', encoding='utf-8') as file:
                                all_code = [line.strip() for line in file]
                            all_code = Lexer(all_code).lexer()
                            all_d_code = dict()
                            for dict_el in all_code:
                                all_d_code.update(dict_el)
                            lexemes.insert(line_count, all_d_code)

                        if key == 'def':  # функции
                            count_lines = int(value.split(' ')[1]) # поле видимости функции(сколько команд из лексем заключено в функции)
                            name_def = value.split(' ')[0] # имя функции

                            list_executable_code = lexemes[line_count: line_count + count_lines + 1] # исполняемый код
                            self._variables[name_def] = list_executable_code
                            del lexemes[line_count - 1: line_count + count_lines] # удаляем строки функции

                        if key.startswith('range'):
                            count_execution = value.split(' ')[0] # количество выполнений кода(tick)
                            count_lines = int(value.split(' ')[1]) # поле видимости цикла(сколько команд из лексем заключено в цикле)
                            self.parser(lexemes=lexemes[line_count: count_lines + line_count + 1],
                                        tick=int(eval(count_execution, self._variables)) - 1)

                        if key.startswith('if') or key.startswith('elif'):
                            count_executions = int(value.split(' ')[-1]) # поле видимости ветвления(сколько команд из лексем заключено в ветвлении)
                            value = ' '.join(value.split(' ')[0:-1]) # значения

                            if not eval(value, self._variables):  # если условия неверно
                                del lexemes[line_count: line_count + count_executions + 1]

                            try:
                                if eval(value, self._variables): # если условия верно
                                    for key_else, value_else in lexemes[line_count + 1 + count_executions].items():
                                        if key_else == 'else':
                                            del lexemes[line_count + 1 + count_executions: int(
                                                value_else) + line_count + count_executions + 2]
                                        elif key_else.startswith('elif'):
                                            del lexemes[line_count + 1 + count_executions: int(
                                                value_else.split(' ')[-1]) + line_count + count_executions + 2]
                            except IndexError:
                                pass

                        if key == 'include': # импортирования библиотек
                            methods.import_library(value)

                        if key == 'quit': # выход из программы
                            exit()

                        if key == 'delete': # удаление из области видимости(_variables)
                            del self._variables[value]

                        if key.startswith('else'):
                            pass

                        line_count += 1

        except ValueError:
            exceptions.Value_Error('Ошибка значения')
        except TypeError as e:
            print(e)
            exceptions.Type_Error('Ошибка типа данных')
        except IndexError as e:
            exceptions.Index_Error('Ошибка индекса')
        except SyntaxError:
            exceptions.Syntax_Error('Ошибка синтаксиса')
        except KeyError as e:
            print(e)
            exceptions.Key_Error('Ошибка key -> value')
        except FileExistsError or FileNotFoundError:
            exceptions.File_Exists('Ошибка отсуствия файла')
        except OSError:
            exceptions.OS_Error('Ошибка ОС')
        except ZeroDivisionError:
            exceptions.Zero_Error('Ай ай ай, на 0 делить нельзя')
        except NameError:
            exceptions.Name_Error('Переменной с таким именем не найдено')
        except Exception:
            exceptions.Parser_Error(f'Ошибка парсера\n{error}')
