"""
Файл парсер
Обработка логики и её выполнения
"""
import typess
import exceptions
import methods


class Parser:
    def __init__(self):
        self._variables = dict()  # переменные

    def _for(self, lexemes, key, value, line_count):
        """
        Функция которая итерируется по списку лексем и выполняет их
        пока условия condition не будет False
        :param lexemes: лексемы до }
        :param key: ключ из главных лексем
        :param value: значения из главных лексем
        :param line_count: лайн, где распологается for
        :return: None
        """
        name_variable = key.split(' ')[0][4::].split('=')[0]
        value_variable = key.split(' ')[0][4::].split('=')[1]
        condition = ''.join(key.split(' ')[1::])
        step = value

        list_executable_code = self.add_queue(lexemes, line_count)

        self._variables[name_variable] = int(value_variable)
        while eval(condition, self._variables):
            self.parser(list_executable_code)
            self._variables[name_variable] += int(step)

    def add_queue(self, lexemes, line_start):
        """
        Принимает список лексем и формирует список для выполнения команд
        :param lexemes: лексемы
        :param line_start: лайн на котором остановились
        :return: None
        """
        line_start, line_end = line_start, line_start
        list_executable_code = []

        for line in range(line_start, len(lexemes)):
            if lexemes[line] == {'end_if': 0}:
                break
            list_executable_code.append(lexemes[line])
        return list_executable_code

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

                        if key.startswith('def_'):  # вызов функций
                            self.parser(self._variables[value])

                        if key.startswith('for'):  # циклы
                            self._for(lexemes, key, value, line_count)

                        if key == 'def':  # функции
                            list_executable_code = self.add_queue(lexemes, line_count)

                            self._variables[value] = list_executable_code
                            for elem in range(line_count - 1, len(lexemes)):  # проходимся по ифу
                                if lexemes[elem] == {'end_if': 0}:  # если закончился останавливаем цикл
                                    break
                                else:
                                    del lexemes[elem]  # иначе удаляем из лексем

                        if key.startswith('range'):
                            list_executable_code = self.add_queue(lexemes, line_count)
                            self.parser(list_executable_code, int(eval(value, self._variables)) + 1)

                        if key.startswith('if'):
                            if not eval(value, self._variables):  # если условия неверно
                                for elem in range(line_count - 1, len(lexemes) - 1):  # проходимся по ифу
                                    if lexemes[elem] == {'end_if': 0}:  # если закончился останавливаем цикл
                                        break
                                    else:
                                        del lexemes[elem]  # иначе удаляем из лексем

                            elif eval(value, self._variables):
                                line_end = line_count - 1

                                for elem in range(line_count - 1, len(lexemes) - 1):  # находим лайн конца цикла
                                    if lexemes[elem] == {'end_if': 0}:
                                        break
                                    else:
                                        line_end += 1

                                try:
                                    if lexemes[line_end + 1] == {'else': 'else'}:  # если после if идёт else
                                        for elem in range(line_end + 2, len(lexemes) - 1):
                                            if lexemes[elem] == {'end_if': 0}:
                                                break
                                            else:
                                                del lexemes[elem]
                                except IndexError:
                                    pass

                        elif key == 'include':
                            methods.import_library(value)

                        if key.startswith('else'):
                            pass

                        line_count += 1

        except ValueError as e:
            print(e)
            exceptions.Value_Error('Ошибка значения')
        except TypeError as e:
            print(e)
            exceptions.Type_Error('Ошибка типа данных')
        except IndexError as e:
            print(e)
            exceptions.Index_Error('Ошибка индекса')
        except SyntaxError as e:
            print(e)
            exceptions.Syntax_Error('Ошибка синтаксиса')
        except KeyError:
            exceptions.Key_Error('Ошибка key -> value')
        except FileExistsError or FileNotFoundError:
            exceptions.File_Exists('Ошибка отсуствия файла')
        except OSError as e:
            print(e)
            exceptions.OS_Error('Ошибка ОС')
        except ZeroDivisionError:
            exceptions.Zero_Error('Ай ай ай, на 0 делить нельзя')
        except NameError:
            exceptions.Name_Error('Переменной с таким именем не найдено')
        except Exception as error:
            exceptions.Parser_Error(f'Ошибка парсера\n{error}')
