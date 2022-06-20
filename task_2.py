# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, weight=25, thickness=5):
        result = self._length * self._width * weight * thickness
        if result > 1000:
            result = result // 1000
            return f'Mass of asphalt required to cover the entire road: {result} t'
        else:
            return f'Mass of asphalt required to cover the entire road: {result} kg'


road = Road(5000, 20)
print(f'Values: lenght - {road._length}m, width - {road._width}m')
print(road.calculate_mass())
