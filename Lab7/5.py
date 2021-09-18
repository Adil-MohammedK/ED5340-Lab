import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.misc import derivative


def Jfun(w):
    return w ** 2 + 54 / w


# calculating its derivative
def deriv(x):
    return derivative(Jfun, x, dx=1e-6)


def dubderiv(x):
    return derivative(deriv, x, dx=1e-6)


# w!=0
a, b = 0.1, 11
n = 100
error = 0.001

delW = (b - a) / n
print(delW)
vals = np.linspace(a, b, n)
plt.plot(vals, Jfun(vals))
# plt.show()
w1 = a
w2 = w1 + delW
w3 = w2 + delW
criticalStatus = True


while True:
    if Jfun(w1) > Jfun(w2) and Jfun(w2) < Jfun(w3):
        minA, maxA, pointA = w1, w3, w2
        print("Min: ", minA, " max: ", maxA)
        break
    else:
        w1 = w2
        w2 = w3
        w3 = w2 + delW
        if w3 <= b:
            continue
        else:
            print("No min/max")
            criticalStatus = False
            break

print("Bracketed value: ", Jfun(pointA))
plt.scatter(pointA, Jfun(pointA))  # Plotting point on the curve
print("Beginning Interval Halving")
minB, maxB = minA, maxA

if criticalStatus == True:
    while True:
        wM = (minB + maxB) / 2
        Length = maxB - minB
        w1 = minB + Length / 4
        w2 = maxB - Length / 4
        if Jfun(w1) < Jfun(wM):
            maxB = wM
            wM = w1
        else:
            if Jfun(w2) < Jfun(wM):
                minB = wM
                wM = w2
            else:
                minB = w1
                maxB = w2
        if math.fabs(Length) < error:
            break
    print("MinB: ", minB, " MaxB: ", maxB)
    print("New Optimal point: ", wM)
    print("Optimal value: ", Jfun(wM))
    plt.scatter(wM, Jfun(wM))  # Plotting point on the curve


print("Newton=Raphson Method")
w1 = 0.1
k = 1
wk = w1
iterations = 1000
for x in range(0, iterations):
    wk1 = wk - (deriv(wk) / dubderiv(wk))
    if math.fabs(deriv(wk1)) < 0.0001:
        break
    else:
        k += 1
        wk = wk1
print("wk: ", wk)
print("Value: ", Jfun(wk))
plt.scatter(wk, Jfun(wk))  # Plotting point on the curve
plt.show()
