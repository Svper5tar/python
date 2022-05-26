# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def user_profile(**kwargs):
    return ' '.join(kwargs.values())


print(user_profile(name=input('name - '), surname=input('surname - '),
                   year=(input('year - ')), city=input('city - '),
                   email=input('email - '), phone=input('phone - ')))
