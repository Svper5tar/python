# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroError(Exception):
    def __init__(self, text):
        self.text = text


x = input('Введите делимое число: ')
y = input('Введите делитель: ')

try:
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroError('0 в качестве делителя недопустим')
except ZeroError as error:
    print(error)
else:
    print(x / y)


