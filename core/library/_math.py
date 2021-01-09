class Math:
    @staticmethod
    def ceil(value: str) -> int:
        if int(value.split('.')[1][0]) >= 5:
            return int(value.split('.')[0]) + 1
        elif int(value.split('.')[1][0]) < 5:
            return int(value.split('.')[0])

    @staticmethod
    def math_module(value: str) -> float:
        return float(value) if value[0] != '-' else float(value[1:])

