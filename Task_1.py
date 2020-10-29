class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.usual_matrix = ''
        for i in self.matrix:
            for el in i:
                self.usual_matrix += f'{str(el)}\t'
            self.usual_matrix += '\n'
        return self.usual_matrix

    def __add__(self, other):
        return [[(self.matrix[ind][num] + other.matrix[ind][num]) for num, el in enumerate(i)]
            for ind, i in enumerate(self.matrix)]


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
print(matrix_1)
print(matrix_2)
matrix_3 = Matrix(matrix_1 + matrix_2)
print(matrix_3)


