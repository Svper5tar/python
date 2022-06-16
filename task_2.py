# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

i = 0
with open('file_task_2.txt') as file:
    for line in file:
        i += 1
        words = len(line.split())
        print(f'Строка номер {i}: \n', line, f'Кол-во слов в строке: {words}')
