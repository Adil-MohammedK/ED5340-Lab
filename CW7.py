# Recursive Functions

def PrintNum(N):
    if N>0:
        print(N)
        PrintNum(N-1)
def PrintNumOpp(N):
    if N>0:
        PrintNumOpp(N-1)
        print(N)

PrintNum(3)
print("PrintOPP")
PrintNumOpp(3)

avg = lambda a,b: (a+b)/2
print(avg(2,4))

dc1 = {'oil': 3,'stud': 2,'abc': 1}
dc2 = sorted(dc1.items(),key = lambda kv1: kv1[1]) # Sort according to values
print(dc2)

# Functions as first class values

def f():
    return 10

def sum1(a,b,f):
    return print("Sum: ",a+b+f())

f1 = sum1 # Takes it as pointer
print(f1)
f1(10,20,f)