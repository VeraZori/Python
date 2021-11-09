class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(my_row, other_row)]
                       for my_row, other_row in zip(self.matrix, other.matrix)])


matrix1 = Matrix([
    [1, 2, 3],
    [4, 5, 6]])
matrix2 = Matrix([
    [6, 5, 4],
    [3, 2, 1]])

print(matrix1 + matrix2)
