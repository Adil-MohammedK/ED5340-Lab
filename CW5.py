tup1 = ("Adil", 21, 176)

print(tup1)

tup1 = ("Adil", 21, 176, "Cool")
print(tup1)

# tup1=([10,20],'Adil',20)

print(tup1)
# tup1.pop()

# tup1[0]=[20,10] Not work

tup_comp = tuple([(x ** 2, x ** 3) for x in range(5)])
print(tup_comp)

tup_comp = (tup_comp, *tup1)
print(*tup_comp)

# Gruoping Tuples

names = ("Ram", "Raja", "Geetha", "Ramya")
gender = ("M", "M", "F", "F")

combi = tuple([(names[i], gender[i]) for i in range(len(names))])
print(combi)

zip_copy = zip(names, gender)
print(*zip_copy)

for x in zip(names, gender):
    print(x)

# Transpose of matrix
mat = [[1, 2, 3], [4, 5, 6]]
ite = zip(*mat)
lst = list(ite)
print(lst)
