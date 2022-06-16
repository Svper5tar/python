# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.


import json


av_prof_list = []
main_list = []
dict_firms = dict()
dict_av_prof = dict()
i = 0
with open('file_task_7.txt') as file:
    for line in file:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        dict_firms[name] = profit
        if profit > 0:
            av_prof_list.append(profit)
            i = i + 1
        else:
            continue
    total_a_p = sum(av_prof_list) / i
    dict_av_prof["average_profit"] = total_a_p
    main_list.append(dict_firms)
    main_list.append(dict_av_prof)

with open('file_task_7_1.json', 'w') as file_1:
    json.dump(main_list, file_1)
