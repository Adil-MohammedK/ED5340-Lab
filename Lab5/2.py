class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def Add(self, other):
        c = Complex()
        c.imag = self.imag + other.imag
        c.real = self.real + other.real
        return c

    def subtract(self, other):
        c = Complex()
        c.imag = self.imag - other.imag
        c.real = self.real - other.real
        return c

    def mult(self, other):
        c = Complex()
        c.imag = self.real * other.imag + self.imag * other.real
        c.real = self.real * other.real - self.imag * other.imag
        return c

    def divide(self, other):
        divisor = (other.real**2 + other.imag**2)
        c = Complex()
        c.real = (self.real * other.real) - (self.imag * other.imag)/divisor
        c.imag = (self.imag * other.real) + (self.real * other.imag)/divisor
        return c

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.real)

    def __truediv__(self, other):
        divisor = (other.real**2 + other.imag**2)
        return Complex((self.real * other.real) - (self.imag * other.imag)/divisor, (self.imag * other.real) + (self.real * other.imag)/divisor)

    def printComp(self):
        print(str(self.real)+" + "+str(self.imag)+"i")


c1 = Complex(2, 3)
c2 = Complex(4, -5)
c3 = c1.Add(c2)
c3.printComp()
c4 = c3.subtract(c2)
c4.printComp()
c5 = c1.mult(c2)
c5.printComp()
c6 = c4.divide(c2)
c6.printComp()
print()

c3 = c2+c4
c3.printComp()
c4 = c1-c2
c4.printComp()
c5 = c3*c4
c5.printComp()
c2 = c5/c6
c2.printComp()
