# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('file_task_5.txt', 'w') as file:
    user_numbers = input('Введите числа через пробел:\n')
    file.write(user_numbers)
with open('file_task_5.txt') as file:
    numbers = file.read()
    total = sum(map(int, numbers.split()))
    print('Сумма чисел: ', total)
