setA = set()

# Set Methods
setA = {20, 30, 40, 50, 14, 15, 20}
print(setA)
setA.add(23)
print(setA)
setA.add(15)
print(setA)
setA.remove(20)
print(setA)
setA.discard(14)
print(setA)
setA.clear()
print(setA)

setA = {10, 20, 30, 40, 50}
setB = {30, 40, 50, 60}

print(setA | setB)
print(setA & setB)
print(setA - setB)
print(setB - setA)

setA -= setB
print(setA)
# Printing Squares
setC = set([x ** 2 for x in range(1, 10)])
print(setC)
