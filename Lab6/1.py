# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple

x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(x)


class myObj:
    name = "John"


y = myObj()

x = isinstance(y, myObj)
print(x)
x = isinstance(y, str)
print(x)


# The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.

class myAge:
    age = 36


class myObj(myAge):
    name = "John"
    age = myAge


x = issubclass(myObj, myAge)
print(x)
