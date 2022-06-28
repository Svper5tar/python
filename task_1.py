# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        day, month, year = date.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def is_valid(day, month, year):
        if 0 < day < 32:
            if 0 < month < 13:
                if 0 < year < 2023:
                    return f'Date {day}.{month}.{year} is valid'
                else:
                    return f'Date {day}.{month}.{year} is NOT valid'
            else:
                return f'Date {day}.{month}.{year} is NOT valid'
        else:
            return f'Date {day}.{month}.{year} is NOT valid'






x = Data('14-03-1995')
print(x.extract('14-03-1995'))
print(Data.is_valid(33, 13, 2025))
print(Data.is_valid(14, 3, 1995))
