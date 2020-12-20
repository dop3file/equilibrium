"""
Файл парсер
Обработка логики и её выполнения
"""
import typess
import exceptions
import methods


class Parser:
    def __init__(self):
        self._variables = {'ok' : True, 'bad' : False}  # переменные

    def _for(self, lexemes, key, value, line_count):
        """
        Пока condition == True, исполняется код от позиции for до count executions
        :param lexemes: лексемы
        :param key: ключ из главных лексем
        :param value: значения из главных лексем
        :param line_count: лайн, где распологается for
        :return: None
        """
        name_variable = key.split(' ')[0][4::].split('=')[0]
        value_variable = key.split(' ')[0][4::].split('=')[1]
        condition = ' '.join(key.split(' ')[1::])

        step = int(value.lstrip(' ').split(' ')[0].replace(' ',''))
        count_executions = int(value.rstrip(' ').split(' ')[1].replace(' ',''))
        print(step)

        self._variables[name_variable] = int(value_variable)
        while eval(condition, self._variables):
            self.parser(lexemes[line_count: line_count + count_executions + 1])
            self._variables[name_variable] += step

    def parser(self, lexemes, tick=1):
        """
        Функция, где проходит основный цикл выполнения
        key - ключ из лексемы
        value - значения из лексемы
        :param lexemes: лексемы, для выполнения
        :param tick: количество проходов по лексем, по дефолту 1(так как нет цикла for или range)
        :return: None
        """
        line_count = 1
        try:
            for tick in range(tick):
                for el in lexemes:
                    for key, value in el.items():
                        value = str(value)
                        methods.variables = self._variables
                        value = methods.choose_func(value, self._variables)

                        if key[0] == 'v':  # если переменная
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

                        if key.startswith('for'):  # циклы
                            self._for(lexemes, key, value, line_count)

                        if key == 'def':  # функции
                            count_executions = int(value.split(' ')[1])
                            name_def = value.split(' ')[0]

                            list_executable_code = lexemes[line_count: line_count + count_executions + 1]
                            self._variables[name_def] = list_executable_code
                            del lexemes[line_count - 1: line_count + count_executions]

                        if key.startswith('range'):
                            count_execution = value.split(' ')[0]
                            count_lines = int(value.split(' ')[1])
                            self.parser(lexemes=lexemes[line_count: count_lines + line_count + 1], tick=int(eval(count_execution, self._variables)) - 1)

                        if key.startswith('if') or key.startswith('elif'):
                            count_executions = int(value.split(' ')[-1])
                            value = ' '.join(value.split(' ')[0:-1])

                            if not eval(value, self._variables):  # если условия неверно
                                del lexemes[line_count: line_count + count_executions + 1]

                            try:
                                if eval(value, self._variables):
                                    for key_else, value_else in lexemes[line_count + 1 + count_executions].items():
                                        if key_else == 'else':
                                            del lexemes[line_count + 1 + count_executions: int(
                                                value_else) + line_count + count_executions + 2]
                                        elif key_else.startswith('elif'):
                                            del lexemes[line_count + 1 + count_executions: int(
                                                value_else.split(' ')[-1]) + line_count + count_executions + 2]
                            except IndexError:
                                pass

                        if key == 'include':
                            methods.import_library(value)

                        if key.startswith('else'):
                            pass

                        line_count += 1

        except ValueError as e:
            print(e)
            exceptions.Value_Error('Ошибка значения')
        except TypeError as e:
            exceptions.Type_Error('Ошибка типа данных')
        except IndexError as e:
            exceptions.Index_Error('Ошибка индекса')
        except SyntaxError as e:
            exceptions.Syntax_Error('Ошибка синтаксиса')
        except KeyError:
            exceptions.Key_Error('Ошибка key -> value')
        except FileExistsError or FileNotFoundError:
            exceptions.File_Exists('Ошибка отсуствия файла')
        except OSError as e:
            exceptions.OS_Error('Ошибка ОС')
        except ZeroDivisionError:
            exceptions.Zero_Error('Ай ай ай, на 0 делить нельзя')
        except NameError:
            exceptions.Name_Error('Переменной с таким именем не найдено')
        except Exception as error:
            exceptions.Parser_Error(f'Ошибка парсера\n{error}')
