# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list_1 = input('Введите элементы списка через пробел: ').split()
print(list_1)
index = 0

if len(list_1) % 2 == 0:
    while index < len(list_1):
        x = list_1[index]
        list_1[index] = list_1[index + 1]
        list_1[index + 1] = x
        index += 2
else:
    while index < len(list_1) - 1:
        x = list_1[index]
        list_1[index] = list_1[index + 1]
        list_1[index + 1] = x
        index += 2

print(list_1)
