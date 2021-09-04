class Matrix:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix = [[None for j in range(self.rows)]
                       for i in range(self.cols)]

    def getMatrix(self):
        print("Enter the nums:")
        matrix = self.matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(input())
        self.matrix = matrix

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            M = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    M.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return M
        else:
            print("Order not equal")

    def __sub__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            M = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    M.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return M
        else:
            print("Order not equal")

    def __mul__(self, other):
        if isinstance(other, Matrix):

            if self.cols == other.rows:
                M = Matrix(self.rows, other.cols)
                M.matrix = [[sum(a * b for a, b in zip(A_row, B_col))
                             for B_col in zip(*other.matrix)] for A_row in self.matrix]
                return M
            else:
                print("Matrix not in correct order")
        elif isinstance(other, int) or isinstance(other, float):
            M = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    M.matrix[i][j] = self.matrix[i][j]*other
            return M

    def __matmul__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            M = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    M.matrix[i][j] = self.matrix[i][j]*other.matrix[i][j]
            return M
        else:
            print("Order not equal")

    def printMatrix(self):
        print("Matrix is: ", self.matrix)


M1 = Matrix(3, 3)
M1.getMatrix()
M1.printMatrix()
M2 = Matrix(3, 3)
M2.getMatrix()
M3 = M1+M2
M3.printMatrix()
M4 = M1*M2
M4.printMatrix()
M6 = M4*3  # Scalar Multiplication
M6.printMatrix()
M5 = M1 @ M4  # Element by element mult
M5.printMatrix()
