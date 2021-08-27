import math

# Using math module
a, b = 2, 3

print("a=", a, "b=", b)

print("We are using pow(),abs(),min() and max() functions as built in functions")
c = min(-8, 14, 2)
d = max(8, 32, 14)
print("Max of 8,32,14 is:", d)
print("Min of 8,14,2 is:", c)

print("value of c*d is:", (c * d))
print("abs value of c*d is:", abs(c * d))

print("a power b is: ", pow(a, b))

print("Using math module functions")
print("square root of a is: ", math.sqrt(a))
print("b power a:", math.pow(b, a))
print("Floor of -3.5: ", math.floor(-3.5))
print("b! is:", math.factorial(b))
print("log(d) is:", math.log(b))

print("Using rounding fucntions:")
# when the (ndigit+1)th digit is =5
print(round(2.665, 2))

# when the (ndigit+1)th digit is >=5
print(round(2.676, 2))

# when the (ndigit+1)th digit is <5
print(round(2.673, 2))

print("The difference between built in functions and libary functions are:")
print(
    "Built in functions dont need to import the module. They are already present and can be called simply by function_name(). eg: print()"
)
print(
    "They are not linked to a any objects. But to call module functions, you have to first import the module. eg: import os"
)
print(
    "To use the functions in the module, we have to first refer or call the module and then use its fucntion object by (.) operator. eg: math.sin(a)"
)
