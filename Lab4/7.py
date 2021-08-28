# Using Recursion, do the following:
# (a) Given a number, print the reverse.
# (b) Given a number, print the summation of the digits. for a floating point type, split it after the decimal point and do the summation).
# (c) To obtain Fibonacci numbers of first n numbers
# (d) Factorial of n.
# (e) Sum of 'n' digits
import math

Reverse = 0


def reverse(num):
    global Reverse
    if num > 0:
        Reminder = num % 10
        Reverse = (Reverse * 10) + Reminder
        reverse(num // 10)
    return Reverse


fibo_series = [0, 1]


def fibonacci(num):
    if num <= len(fibo_series) and num > 0:
        return fibo_series[num - 1]
    else:
        fn = fibonacci(num - 1) + fibonacci(num - 2)
        if num > len(fibo_series):
            fibo_series.append(fn)
        return fn


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


def numSum(n):

    if n < 10:
        return n
    else:
        return n % 10 + numSum(n // 10)


# def limNumSum(n):
#     global limit
#     limit = limit-1
#     print(limit)
#     if limit > 0:
#         if n < 10:
#             return n
#         else:
#             return n % 10 + limNumSum(n // 10)


# Reverse of number
number = int(input("Enter the number: "))
print(reverse(number))

# Fibonacci series
number = int(input("Enter the n for fibonacci: "))
fibonacci(number)
print(fibo_series)

# Factorial
number = int(input("Enter the factorial to find: "))
print(factorial(number))

# Sum of digits
number = input("Enter the num to sum: ").split(".")
print(number)
# print(int(number[0]), int(number[1]))
if len(number) > 1:
    print("Sum of digits: ", numSum(int(number[0])) + numSum(int(number[1])))
else:
    print("Sum of digits: ", numSum(int(number[0])))

# Sum of 'n' digits
number = input("Enter the num to sum: ").split(".")
print(number)
limit = int(input("Enter n or limit: "))
if len(number) > 1:
    num = number[0]+number[1]
    num = num[0:limit]
    # print(num)
    print("Sum of digits: ", numSum(int(num)))
else:
    num = number[0]
    num = num[0:limit]
    # print(num)
    print("Sum of digits: ", numSum(int(num)))
