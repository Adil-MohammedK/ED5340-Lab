class Polygon:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length


class Square(Polygon):
    def __init__(self, length):
        super().__init__(4, length)

    def findarea(self):
        area = self.length**2
        return area


shape = Square(4)
area = shape.findarea()

print("Area is: ", area)
# TODO: Is this, simple??
