# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.


class IsNumbers(Exception):
    def __int__(self, text):
        self.text = text


lst = []
x = input('Enter the element: ')

while x != 'exit':
    try:
        if not x.isdigit():
            raise IsNumbers('It is not a number')
    except IsNumbers as error:
        print(error)
        x = input('Enter the element or "exit" for exit: ')
    else:
        x = int(x)
        lst.append(x)
        print(lst)
        x = input('Enter the element or "exit" for exit: ')
    if x == 'exit':
        print(f'List: {lst}')
        print('Program is closed')
