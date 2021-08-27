# Program to find num is odd/even

def find_even(N):
    if N % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter num: "))
print("The number is: ", find_even(num))
