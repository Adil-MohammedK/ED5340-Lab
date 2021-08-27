# Given an integer, find out the sum of its digits.

num = int(input("Enter the number: "))
x = num
sum = 0

while x > 0:
    sum += x % 10
    x = int(x / 10)

print("sum of ", num, "is: ", sum)
