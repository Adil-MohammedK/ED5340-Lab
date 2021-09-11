import math


class Complex:
    def __init__(self, real, imag) -> None:
        self.real = real
        self.imag = imag


class Matrix:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix = [[None for j in range(self.cols)]
                       for i in range(self.rows)]

    def getMatrix(self, vector=0, real=0, imag=0):
        if vector == 0:
            print("Enter the nums:")
            matrix = self.matrix
            for i in range(self.rows):
                for j in range(self.cols):
                    matrix[i][j] = int(input())
            self.matrix = matrix
        elif vector == 1:
            matrix = self.matrix
            matrix[1][0], matrix[1][1] = real, imag


class Vector(Matrix):
    def __init__(self, i, j) -> None:
        super().__init__(2, 2)
        print("Type 0,0,0 for first line and then enter vector values")
        self.getMatrix(vector=1, real=i, imag=j)
        self.matrix[0][0], self.matrix[0][1] = "i", "j"

    def showVector(self):
        print("Vector is: ")
        for x in range(2):
            print(str(self.matrix[1][x])+self.matrix[0][x], end=' ')


class Eigen(Vector, Complex):
    def __init__(self, real, imag) -> None:
        Complex.__init__(self, real, imag)
        Vector.__init__(self, real, imag)
        self.matrix[1][0], self.matrix[1][1] = self.real, self.imag
        self.angle = math.degrees(math.atan(float(self.imag) / self.real))

    def showEigen(self):
        print("Complex in Euler form: e^", self.angle)
        print("Complex in vector form: ")
        self.showVector()


# V1 = Vector()
# # TODO:
# V1.showVector()

E1 = Eigen(2, 3)
E1.showEigen()
