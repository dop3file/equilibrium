class Math:
    @staticmethod
    def ceil(value: str) -> int:
        """
        Округления числа
        """
        if int(value.split('.')[1][0]) >= 5:
            return int(value.split('.')[0]) + 1
        return int(value.split('.')[0])

    @staticmethod
    def math_module(value: str) -> float:
        """
        Модуль числа
        """
        return float(value) if value[0] != '-' else float(value[1:])

