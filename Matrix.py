import random


class InverseMatrix:
    def __init__(self):
        self.n = int(input())
        self.determinant = 0
        self.matrix = []
        self.matrix_identity = [[1 if i == j else 0 for j in range(self.n)] for i in range(self.n)]

    # генерация рандомной матрицы
    def generate_random_matrix(self):
        self.matrix = [[random.randint(0, 100) for j in range(self.n)] for i in range(self.n)]

        # проверка критерия обратимости
        if self.determinant_matrix(self.matrix) == 0:
            self.generate_random_matrix()
        else:
            self.print_matrix(self.matrix)

    # ввод матрицы
    def matrix_input(self):
        self.matrix = [[int(j) for j in input().split()] for i in range(self.n)]

        # проверка критерия обратимости
        if self.determinant_matrix(self.matrix) == 0:
            print("Критерий обратимости не выполняется \n")
            print("Введите матрицу снова \n")
            self.matrix_input()

    # минор
    def minor_matrix(self, matrix, i, j):
        tmp = [row for k, row in enumerate(matrix) if k != i]
        tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
        return tmp

    # нахождение определителя матрицы
    def determinant_matrix(self, matrix):
        size = len(matrix)
        if size == 2:
            self.determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return self.determinant

        self.determinant = sum((-1) ** j * matrix[0][j] * self.determinant_matrix(self.minor_matrix(matrix, 0, j)) for j in range(size))
        return self.determinant

    # нахождение обратной матрицы
    def get_reverse_matrix(self):
        for i in range(self.n):
            if self.matrix[i][i] == 0:
                self.permutation_lines(i, i + 1)
            self.division_line(i, self.matrix[i][i])
            for j in range(i + 1, self.n):
                self.difference_lines(j, i, self.matrix[j][i])

        for i in range(self.n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.difference_lines(j, i, self.matrix[j][i])

        self.print_matrix(self.matrix_identity)

    # разность строк
    def difference_lines(self, first_term, second_term, factor=1):
        for i in range(self.n):
            self.matrix_identity[first_term][i] -= self.matrix_identity[second_term][i] * factor
            self.matrix[first_term][i] -= self.matrix[second_term][i] * factor

    # деление строки
    def division_line(self, line, divider):
        for i in range(self.n):
            self.matrix_identity[line][i] /= divider
            self.matrix[line][i] /= divider
            if self.matrix[line][i] == 0.0:
                self.matrix[line][i] = abs(self.matrix[line][i])
            if self.matrix_identity[line][i] == 0.0:
                self.matrix_identity[line][i] = abs(self.matrix_identity[line][i])

    # перестановка строк
    def permutation_lines(self, first_term, second_term):
        for i in range(self.n):
            self.matrix[second_term][i], self.matrix[first_term][i] = self.matrix[first_term][i], self.matrix[second_term][i]
            self.matrix_identity[second_term][i], self.matrix_identity[first_term][i] = self.matrix_identity[first_term][i], self.matrix_identity[second_term][i]

        for i in range(self.n):
            for j in range(self.n):
                self.matrix[i][j] *= -1
                self.matrix_identity[i][j] *= -1

    # печать матрицы
    def print_matrix(self, matrix):
        for i in range(self.n):
            print(matrix[i])


matrix = InverseMatrix()
matrix.matrix_input()
matrix.get_reverse_matrix()