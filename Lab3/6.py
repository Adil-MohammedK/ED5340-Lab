# Sort lists in tuple

# myTuple = ([7, 5, 4], [8, 2, 4], [0, 7, 5])
subsets = int(input("Enter number of subsets: "))

myTuple = [[int(input()), int(input()), int(input())] for x in range(subsets)]

print("My tuple is : " + str(myTuple))
res = tuple((sorted(sub) for sub in myTuple))

# printing result
print("Sorted tuple : " + str(res))
