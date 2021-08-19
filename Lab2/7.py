x=int(input("ENter the variable: "))
n=int(input("Enter number of terms: "))

# Exp function
# initialize sum of series
sum = 1.0
for i in range(n, 0, -1):
    sum = 1 + x * sum / i
print ("e^x =", sum)

# Cos series

PI = 3.14

x = x * (PI / 180.0); # Convert degree to radian
result = 1
sign = 1
fact = 1
pow = 1

for i in range(1,n):
    sign = sign * (-1)
    fact = fact * (2 * i - 1) * (2 * i)
    pow = pow * x * x
    result = result + sign * pow / fact

print("cosx = ",result)

# Sin series

sin_result=x
sign=1
fact=1
pow=x

for i in range(2,n):
    sign=sign * (-1)
    fact=fact * (2 * i - 1) * i
    pow = pow * x * x
    sin_result = sin_result + sign * pow / fact

print("sinx = ",sin_result)


