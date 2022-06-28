# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Cloth(ABC):
    total_cons = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.size = size
        Cloth.total_cons += self.consumption

    def __str__(self):
        return f'Coat size: {self.size}'

    @property
    def consumption(self):
        cons = self.size / 6.5 + 0.5
        return float(f'{cons:.02f}')


class Costume(Cloth):
    def __init__(self, growth):
        self.growth = growth
        Cloth.total_cons += self.consumption

    def __str__(self):
        return f'Costume growth: {self.growth}'

    @property
    def consumption(self):
        cons = 2 * self.growth + 0.3
        return float(f'{cons:.02f}')


x = Coat(2)
print(f'{x}, consumption: {x.consumption}')

y = Costume(5)
print(f'{y}, consumption: {y.consumption}')

print(f'Total fabric consumption: {Cloth.total_cons:.02f}')
