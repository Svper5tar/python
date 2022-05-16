# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = abs(int(input('Введите целое положительное число: ')))
max_number = number % 10
while True:
    number = number // 10
    if number % 10 > max_number:
        max_number = number % 10
    if number > 9:
        continue
    else:
        print(max_number)
        break
