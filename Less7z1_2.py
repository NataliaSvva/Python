class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        return str(''.join([''.join([str(k) for k in i]) for i in self.matrix]))

    def __add__(self, other):
        sum_matrix = []
        line_sum = []
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                line_sum.append(self.matrix[i][k] + other.matrix[i][k])
                sum_matrix.append(line_sum)
            return Matrix(' '.join(map(str, sum_matrix[1])))




matrix_1 = Matrix([[31, 22, 0, 0], [37, 43 , 0, 0], [51, 86, 0, 0]])
matrix_2 = Matrix([[3, 5, 32, 0], [2, 4, 6, 0], [-1, 64, -8, 0]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1],[0, 0, 0, 0]])
print(matrix_1 + matrix_2)



