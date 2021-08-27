A = [1, 3, 2]
B = [6, -1, -2]

zipItem = zip(A, B)
sortedList = [[y, x] for y, x in sorted(zipItem)]

print(sortedList)
print("Making seperate...")
A = [x[0] for x in sortedList]
B = [x[1] for x in sortedList]

print("A: ", A)
print("B: ", B)
