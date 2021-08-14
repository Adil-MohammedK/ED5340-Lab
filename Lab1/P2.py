import random

a=random.randint(1,6)
print(a)

random.seed(random.randint(1,10))

print(random.randint(1,10))

random.seed(random.randint(1,10))
print(random.randint(1,10))

random.seed(random.randint(1,10))
print(random.randint(1,10))

random.seed(random.randint(1,10))
b=random.randint(1,6)
print(b)

print("number on Dice 1 : ",a)
print("number on Dice 2 : ",b)
sum=a+b
print("Sum on dice: ",sum)

if a==6 and b==6:
    print("Double")