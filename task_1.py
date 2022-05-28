# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы
# сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name, time, salary, bonus = argv
print(f'Имя скрипта: "{name}"')
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    result = (time * salary) + bonus
    print(f'Заработная плата сотрудника: {result}')
except ValueError:
    print('Нужно вводить числа')
