# The map() function in python has the following syntax:
# map(func, *iterables)
# Where func is the function on which each element in iterables(as many as they are) would be applied on.
# In Python 3, however, the function returns a map object which is a generator object. To get the result as a list, the built-in list() function can be called on the map object. i.e. list(map(func, *iterables))
# The number of arguments to func must be the number of iterables listed.

from functools import reduce
friends = ['Adil', 'Malay', 'Ramshid', 'Dude']

uppered_friends = list(map(str.upper, friends))

print(uppered_friends)

# reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an initial argument. It has the following syntax:
# reduce(func, iterable[, initial])
# Where func is the function on which each element in the iterable gets cumulatively applied to,
# and initial is the optional value that gets placed before the elements of the iterable in the calculation,
# and serves as a default when the iterable is empty


def custom_sum(first, second):
    return first + second


numbers = [3, 4, 6, 9, 34, 12]
result = reduce(custom_sum, numbers, 10)  # Here 10 taken as initial argument
print(result)
