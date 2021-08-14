num=int(input("Enter the number: "))
flag=False
for i in range(2,int(num/2)):
    if (num % i) == 0:
        flag = True
        break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
