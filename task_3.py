class Cell:
    def __init__(self, cells):
        self.cell = int(cells)

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        new_cell = self.cell + other.cell
        return Cell(new_cell)

    def __sub__(self, other):
        if self.cell - other.cell >= 0:
            new_cell = self.cell - other.cell
            return Cell(new_cell)
        else:
            return 'Разность меньше нуля'

    def __mul__(self, other):
        new_cell = self.cell * other.cell
        return Cell(new_cell)

    def __truediv__(self, other):
        new_cell = self.cell // other.cell
        return Cell(new_cell)

    def make_order(self, cells_in_row):
        res = ''
        for i in range(int(self.cell / cells_in_row)):
            res += f'{"*" * cells_in_row} \\n'
        res += f'{"*" * (self.cell % cells_in_row)}'
        return res


x = Cell(50)
y = Cell(12)

print(x)
print(type(y))

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x.make_order(10))
print(y.make_order(1))
