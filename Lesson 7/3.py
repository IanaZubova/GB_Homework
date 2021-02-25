class Cell:

    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        return int(self.value + other.value)

    def __sub__(self, other):
        return self.value - other.value if (self.value - other.value) > 0 else print('Negative value')

    def __mul__(self, other):
        return int(self.value * other.value)

    def __truediv__(self, other):
        return round(self.value / other.value)

    def make_order(self, cells_row):
        row = ''
        for i in range(int(self.value / cells_row)):
            row += f'{"*" * cells_row} \n'
        row += f'{"*" * (self.value % cells_row)}'
        return row


first_cell = Cell(11)
second_cell = Cell(33)

print(first_cell + second_cell)
print(first_cell - second_cell)
print(first_cell * second_cell)
print(first_cell / second_cell)
print(first_cell.make_order(7))
print(second_cell.make_order(5))