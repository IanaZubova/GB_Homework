class Matrix:

    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def __add__(self):

        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.matrix1)):
            for j in range(len(self.matrix2[i])):
                matrix[i][j] = self.matrix1[i][j] + self.matrix2[i][j]
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in matrix])

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in matrix])


new_matrix = Matrix([[3, 2, 4],
                     [3, 1, 6],
                     [1, 1, 1]],
                    [[1, 1, 1],
                     [3, 1, 6],
                     [3, 2, 4]])

print(new_matrix.__add__())