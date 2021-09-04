

class StudentDetail:
    def __init__(self, n='', r=1, s=1):
        self.name = n
        self.roll = r
        self.sem = s
        self._total = r + s
        self.__total1 = self._total+5

    def datainput(self, n, r, s):
        self.name = n
        self.roll = r
        self.sem = s

    def printData(self):
        print(self.name, self.roll, self.sem, self._total, self.__total1)


s1 = StudentDetail()
s1.datainput('Adil', 1, 5)
print(s1.name)
s1.printData()
s2 = StudentDetail('Adil', 2, 4)
# print(s2.__total1)
s2.__total1 = 10  # Stored in a separte name
print(s2.__total1)
s2.printData()


class Complex:

    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    def __add__(self, other):
        c = Complex()
        c._real = self._real+other._real
        c._imag = self._imag+other._imag
        return c

    def print_comp(self):
        print('real:', self._real, " imag:", self._imag)


c1 = Complex(4.5, 5.45)

c1.print_comp()

c2 = Complex(2.3, 3.4)
# c3 = c1+c2
# c3.print_comp()


class Department:
    def __init__(self, dname='ED'):
        self._deptname = dname

    def print_dept(self):
        print(self._deptname)


class Faculty:
    def __init__(self, name, roll, dept):
        self._fname = name
        self._fid = roll
        self._dobj = Department(dept)


class Student:
    def __init__(self, name, roll, dept):
        self._sname = name
        self._sid = roll
        self._sdobj = Department(dept)

    def print_student(self):
        print(self._sname, self._sid)
        print(self._sdobj.print_dept())


s1 = Student('Adil', 41, 'ED')
s2 = Student('Name2', 42, 'EE')
s1.print_student()
s2.print_student()


class Base:
    def __init__(self, name):
        self.name = name
        print("inside base init")

    def printname(self):
        print(self.name)


class Derived(Base):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        print("Inside derived")

    def printRoll(self):
        print(self.name)
        print(self.roll)


d1 = Derived('Name1', 2)
d1.printRoll()
