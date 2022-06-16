# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open('file_task_3.txt') as file:
    poor = []
    all_salary = []
    workers = file.read().split('\n')
    for salary in workers:
        salary = salary.split()
        if float(salary[1]) < 20000:
            poor.append(salary[0])
        all_salary.append(salary[1])
print(f'Фамилии сотрудников, имеющих оклад ниже 20.000: \n', poor)
mid_sal = sum(map(float, all_salary)) / len(all_salary)
print('Средняя величина дохода всех сотрудников -', format(mid_sal, '.2f'))
