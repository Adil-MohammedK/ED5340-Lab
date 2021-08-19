# Part a

a,b,c=input("Enter the nums: ").split()
# print(a,b,c)
a=int(a)
b=int(b)
c=int(c)
print(a,b,c)

if a>b>c:
    print("a is greater")
elif a>c>b:
    print("a is greater")
elif b>c:
    print('b is greater')
else:
    print("c is greater")

# Part b

if a>b and a>c:
    print("A is greater")
elif b>c:
    print('B is greater')
else:
    print("C is greater")

if a>b:
    if a>c:
        print("Alpha is greater") # Alpha ,beta, gamma just different names
elif b>c:
    print('Beta is greater')
else: 
    print("Gamma is greater")
    



