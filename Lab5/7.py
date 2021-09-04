print("Operator overloading:")
print("+ __add__(self, other)")
print("–	__sub__(self, other)")
print("* __mul__(self, other)")
print("/ __truediv__(self, other)")
print("// __floordiv__(self, other)")
print("% __mod__(self, other)")
print("** __pow__(self, other)")


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x-2*other.y
        y = self.y-2*other.x
        return Point(x, y)

    def __mul__(self, other):
        x = self.x*2*other.y
        y = self.y*2*other.x
        print(x, y)

    def __pow__(self, other):
        x = str(self.x)*other
        return x


print()
p1 = Point(1, 2)
p2 = Point(2, 3)
print("+ operator overloaded")
print((p1+p2).x, (p1+p2).y)
# Do the same for ‘-’, ‘*’ and ‘**’  operators.
print()
print("- operator overloaded")
print((p1-p2).x, (p1-p2).y)
print()
print("* operator overloaded")
print(p1*p2)
print()
print("** operator overloaded")
print(p2**5)

print()
