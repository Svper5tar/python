# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк

user_time = int(input('Введите время в секундах: '))

hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = user_time - (hours * 3600 + minutes * 60)

print('Введённое вами время в формате чч:мм:сс - {}:{:02d}:{:02d}'.format(hours, minutes, seconds))
