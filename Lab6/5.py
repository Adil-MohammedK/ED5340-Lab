import os


class Complex:
    def __init__(self, real=0, imag=0) -> None:
        self.real = real
        self.imag = imag

    def getComplex(self, filename):
        with open(filename) as file:
            item = file.read()
            self.complex = item.split()
            self.real, self.imag = int(self.complex[0]), int(self.complex[1])

    def writeComplement(self, filename):
        self.imag = -self.imag
        with open(filename, 'a') as file:
            file.write('\n')
            file.write(str(self.real)+' '+str(self.imag))


class Matrix:
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[None for j in range(self.cols)]
                       for i in range(self.rows)]

    def getMatrix(self, filename):
        with open(filename) as file:
            contents = file.read()
            self.matrix = [item.split() for item in contents.split('\n')]
            self.rows = len(self.matrix)
            self.cols = len(self.matrix[0])
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] = int(self.matrix[i][j])

    def __mul__(self, other):
        M = Matrix(rows=self.rows, cols=self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                M.matrix[i][j] = self.matrix[i][j]*other
        return M

    def putMatrix(self, filename):
        with open(filename, 'a') as file:
            file.write('\n')
            for i in range(self.rows):
                for j in range(self.cols):
                    file.write(str(self.matrix[i][j])+' ')
                file.write('\n')


if os.path.exists('Lab6'):
    print("Exists")
    os.chdir('Lab6')

Mat = Matrix()
Mat.getMatrix('matdata.txt')
print(Mat.matrix)
Mat = Mat*3
print(Mat.matrix)
Mat.putMatrix('matdata.txt')

Comp = Complex()
Comp.getComplex('compdata.txt')
Comp.writeComplement('compdata.txt')
