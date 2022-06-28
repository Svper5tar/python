# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a):
        self.a = int(a)

    def __add__(self, other):
        return ComplexNumber(self.a + other.a)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a)

    def __str__(self):
        return f'Number is: {self.a}'


x = ComplexNumber(24)
print(x)
print(type(x))

y = ComplexNumber(2)
print(y)
print(type(y))

z = x + y
print(z)
print(type(z))

c = x * y
print(c)
print(type(c))
