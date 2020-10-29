class Cell:

    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        return self.cell_number + other.cell_number

    def __sub__(self, other):
        if self.cell_number > other.cell_number:
            return self.cell_number - other.cell_number
        else:
            return 'It is impossible to make a subtraction of these cells'

    def __mul__(self, other):
        return self.cell_number * other.cell_number

    def __truediv__(self, other):
        return self.cell_number // other.cell_number

    def make_order(self, row_len):
        while self.cell_number > 0:
            print('*' * row_len)
            self.cell_number -= row_len
            if self.cell_number < row_len:
                print('*' * self.cell_number)
                break


cell_1 = Cell(10)
cell_2 = Cell(19)
print(cell_2 - cell_1)
print(cell_2 + cell_1)
print(cell_2 * cell_1)
print(cell_2 / cell_1)
cell_2.make_order(7)
print()
cell_1.make_order(3)
