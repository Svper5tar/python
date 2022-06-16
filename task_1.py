# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

file = open('file_task_1.txt', 'w')
print('File is open')
data = input('Enter data:\n')
while data != '':
    file.write(data + "\n")
    data = input('Enter data (send empty string for close the file):\n')
file.close()
