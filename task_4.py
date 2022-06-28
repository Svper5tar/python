# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


class Storage:
    def __init__(self, title):
        self.title = title
        self.lst = []

    def __getitem__(self, index):
        return self.lst[index]

    def __str__(self):
        return f'{self.title} \n {self.lst}'

    def to_get(self, equipment):
        self.lst.append([equipment.__class__.__name__,
                         [equipment.name, equipment.model, equipment.inv_numb,
                          equipment.quantity, equipment.kind]])
        return print(f'Оборудование {equipment.name} {equipment.model} получено в {self.title}')

    def to_send(self, equipment, other):
        self.lst.remove([equipment.__class__.__name__,
                         [equipment.name, equipment.model, equipment.inv_numb,
                          equipment.quantity, equipment.kind]])
        other.lst.append([equipment.__class__.__name__,
                         [equipment.name, equipment.model, equipment.inv_numb,
                          equipment.quantity, equipment.kind]])
        return print(f'Оборудование {equipment.name} {equipment.model} перемещено из {self.title} в {other.title}')


class OfficeEquipments:
    def __init__(self, name, model, inv_numb, quantity):
        self.name = name
        self.model = model
        self.inv_numb = inv_numb
        self.quantity = quantity


class Printer(OfficeEquipments):
    def __init__(self, name, model, inv_numb, kind, quantity):
        super().__init__(name, model, inv_numb, quantity)
        self.kind = kind

    def __str__(self):
        return f'{self.__class__.__name__}: Название - {self.name}, Модель - {self.model}, ' \
               f'Инвентарный номер - {self.inv_numb}, Тип печати - {self.kind}, Кол-во - {self.quantity} шт.'


class Scaner(OfficeEquipments):
    def __init__(self, name, model, inv_numb, kind, quantity):
        super().__init__(name, model, inv_numb, quantity)
        self.kind = kind

    def __str__(self):
        return f'{self.__class__.__name__}: Название - {self.name}, Модель - {self.model}, ' \
               f'Инвентарный номер - {self.inv_numb}, Тип сканера - {self.kind}, Кол-во - {self.quantity} шт.'


class Copier(OfficeEquipments):
    def __init__(self, name, model, inv_numb, kind, quantity):
        super().__init__(name, model, inv_numb, quantity)
        self.kind = kind

    def __str__(self):
        return f'{self.__class__.__name__}: Название - {self.name}, Модель - {self.model}, ' \
               f'Инвентарный номер - {self.inv_numb}, Поддерж. цвета - {self.kind}, Кол-во - {self.quantity} шт.'


storage1 = Storage('Главный склад')
storage2 = Storage('Магазин ул. Мира 64')

x = Printer('HP', 'AS234X', 12345, 'laser', 3)
storage1.to_get(x)
print(storage1)
y = Scaner('Samsung', 'E23Q', 555555, 'slide-scaner', 6)
print(y)
print(type(y))
storage2.to_get(y)
print(storage2)
z = Copier('Xerox', 'AH2', 222222, 'ч/б', 3)
storage1.to_get(z)
storage1.to_send(z, storage2)
print(storage1)
print(storage2)

# ----------------------- с последним заданием не справился, при попытке совершить to_get или to_send
# введёнными пользователем данными возникала ошибка AttributeError: 'list' object has no attribute 'name',
# я понял что дело в том что эти методы создают список из элементов экземпляра, но из-за дедлайна я не смог успеть понять
# что с этим можно сделать.

# x = input('Что нужно добавить? (printer, scaner, copier): ')
# while x != 'exit':
#     if x == 'printer':
#         x = input('Введите данные через пробел (Производитель, модель, инв. номер, '
#                   'тип принтера(лазерный или порошковый), кол-во товаров: \n')
#         name, model, inv_numb, kind, quantity = x.split(' ')
#         try:
#             if not inv_numb.isdigit() or not quantity.isdigit():
#                 raise ValueError
#         except ValueError:
#             print('Неверно введены инв. номер и/или кол-во, повторите ввод')
#             x = 'printer'
#         else:
#             inv_numb = int(inv_numb)
#             quantity = int(quantity)
#             product = Printer(name, model, inv_numb, kind, quantity)
#             storage1.to_get(product)
#             x = input('Что нужно добавить? (printer, scaner, copier): ')
#     if x == 'scaner':
#         x = input('Введите данные через пробел (Производитель, модель, инв. номер, '
#                   'тип сканера(планшетный, протяжной, слайд-сканер), кол-во товаров: \n')
#         name, model, inv_numb, kind, quantity = x.split(' ')
#         try:
#             if not inv_numb.isdigit() or not quantity.isdigit():
#                 raise ValueError
#         except ValueError:
#             print('Неверно введены инв. номер и/или кол-во, повторите ввод')
#             x = 'printer'
#         else:
#             inv_numb = int(inv_numb)
#             quantity = int(quantity)
#             product = Scaner(name, model, inv_numb, kind, quantity)
#             storage1.to_get(product)
#             x = input('Что нужно добавить? (printer, scaner, copier): ')
#     if x == 'copier':
#         x = input('Введите данные через пробел (Производитель, модель, инв. номер, '
#                   'поддерж. цвета(цветной, чб), кол-во товаров: \n')
#         name, model, inv_numb, kind, quantity = x.split(' ')
#         try:
#             if not inv_numb.isdigit() or not quantity.isdigit():
#                 raise ValueError
#         except ValueError:
#             print('Неверно введены инв. номер и/или кол-во, повторите ввод')
#             x = 'printer'
#         else:
#             inv_numb = int(inv_numb)
#             quantity = int(quantity)
#             product = Copier(name, model, inv_numb, kind, quantity)
#             storage1.to_get(product)
#             x = input('Что нужно добавить? (printer, scaner, copier): ')
#     if x == 'exit':
#         print('Ввод товаров окончен')
#         break
#
# storage1.to_send(storage1[0], storage2)
# print(storage1)
# print(storage2)
