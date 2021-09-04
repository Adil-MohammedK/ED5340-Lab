class Employee:
    def __init__(self, name, age, salary, promo=5):
        self.name = name
        self.age = age
        self.salary = salary
        self.promo = promo


class Manager(Employee):
    def __init__(self, name, age, salary, employees, developers):
        super().__init__(name, age, salary)
        self.employees = employees
        self.developers = developers
        self.promo = 30

    def addEmployee(self):
        print("adding employee")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        self.employees.append(Employee(name, age, salary))

    def rmEmployee(self):
        print("removing employee")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        self.employees = [item for item in self.employees if item.name != name]

    def ShowEmp(self):
        for employee in self.employees:
            print(employee.name, employee.age, employee.salary)

    def ShowDev(self):
        for employee in self.developers:
            print(employee.name, employee.age, employee.salary, employee.lang)

    def raiseSal(self, name):
        for employee in self.employees:
            if name == employee.name:
                employee.salary = employee.salary*float(employee.promo+100)/100
                print("New salary: ", employee.salary)
        for dev in self.developers:
            if name == dev.name:
                dev.salary = dev.salary*float(dev.promo+100)/100
                print("New salary: ", dev.salary)


class Developer(Employee):
    def __init__(self, name, age, salary, lang, promo=10):
        super().__init__(name, age, salary)
        self.lang = lang
        self.promo = 20


employees = [Employee('Name1', 21, 21000), Employee(
    'Name2', 22, 21500), Employee('Name3', 25, 21000), Employee('Name4', 21, 200), Employee('Name5', 26, 23400), Employee('Name7', 30, 61000), Employee('Name8', 42, 433000), Employee('Name9', 23, 23000)]
developers = [Developer('Dev1', 21, 21000, "C"), Developer(
    'Dev2', 22, 21500, "Python"), Developer('Dev3', 25, 21000, "C++"), Developer('Dev4', 21, 200, "Java"), Developer('Dev5', 26, 23400, "JS"), Developer('Dev7', 30, 61000, "Ruby"), Developer('Dev8', 42, 433000, 'React'), Developer('Dev9', 23, 23000, "React")]
manager = Manager('Manager1', 43, 210000, employees, developers)
manager.ShowEmp()
manager.ShowDev()
manager.addEmployee()
manager.ShowEmp()

manager.rmEmployee()
manager.ShowEmp()
manager.raiseSal("Dev2")
manager.ShowDev()
