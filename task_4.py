# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} in motion'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_left(self):
        return f'{self.name} turned left'

    def turn_right(self):
        return f'{self.name} turned right'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Current speed {self.name}: {self.speed}, speed is exceeded!'
        else:
            return f'Current speed {self.name}: {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Current speed {self.name}: {self.speed}, speed is exceeded!'
        else:
            return f'Current speed {self.name}: {self.speed}'


class PoliceCar(Car):
    pass


car_1 = TownCar(80, 'Grey', 'KIA Sportage', False)
print(f'Model: {car_1.name}, color: {car_1.color}, is police car: {car_1.is_police}')
print(car_1.go())
print(car_1.show_speed())
car_2 = WorkCar(25, 'White', 'GAZ-3302', False)
print(f'Model: {car_2.name}, color: {car_2.color}, is police car: {car_2.is_police}')
print(car_2.stop())
car_3 = SportCar(120, 'Red', 'Lamborghini Diablo', False)
print(f'Model: {car_3.name}, color: {car_3.color}, is police car: {car_3.is_police}')
print(car_3.turn_right())
print(car_3.turn_left())
car_4 = PoliceCar(100, 'Black and white', 'Lada Granta', True)
print(f'Model: {car_4.name}, color: {car_4.color}, is police car: {car_4.is_police}')
print(car_4.show_speed())
