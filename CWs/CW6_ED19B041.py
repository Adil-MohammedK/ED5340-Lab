class Department:
    def __init__(self, dname='ED'):
        self.deptname = dname

    def print_dept(self):
        print(self.deptname)


class Faculty:
    def __init__(self, name, roll, dept):
        self._fname = name
        self._fid = roll
        self._dobj = Department(dept)

    def print_faculty(self):
        print("Faculty:", self._fname, self._fid)
        print(self._dobj.print_dept())


class Student:
    def __init__(self, name, roll, dept):
        self._sname = name
        self._sid = roll
        self._sdobj = Department(dept)

    def print_student(self):
        print("Student:", self._sname, self._sid)
        print(self._sdobj.print_dept())


s1 = Student('Adil', 41, 'ED')
s2 = Student('Name2', 42, 'EE')
s1.print_student()
s2.print_student()

f1 = Faculty('RMN', 1, 'ED')
f2 = Faculty('CVK', 2, 'PH')
f1.print_faculty()
f2.print_faculty()
