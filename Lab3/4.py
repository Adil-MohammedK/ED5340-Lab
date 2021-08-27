matrix1 = [[x, x + 5] for x in range(1, 10) if x % 2 == 0]
matrix2 = [[x, x + 7] for x in range(1, 10) if x % 2 != 0]

print("Original matrices: ")
print(matrix1)
print(matrix2)

# interchanging rows
zipped = zip(matrix1, matrix2)
list1 = list(zipped)
a = list(list1[0][0])
b = list(list1[0][1])
a, b = b, a
list1[0] = a, b

mat1, mat2 = zip(*list1)
print("Swapped rows: ")
print(mat1)
print(mat2)


matrix1 = [[1, 4, 4], [45, 15, 53], [65, 13, 12]]
matrix2 = [[31, 13, 45], [51, 13, 35], [56, 38, 9]]
print("Original matrices: ")
print(matrix1)
print(matrix2)

zipped1 = zip(matrix1[0], matrix1[1], matrix1[2])
list2 = list(zipped1)
zipped2 = zip(matrix2[0], matrix2[1], matrix2[2])
list3 = list(zipped2)

zipped3 = zip(list2, list3)
list5 = list(zipped3)

# interchanging columns
a = list(list5[0][0])
b = list(list5[0][1])
a, b = b, a
list5[0] = a, b


mat1, mat2 = zip(*list5)
rect1 = zip(mat1[0], mat1[1], mat1[2])
rect2 = zip(mat2[0], mat2[1], mat2[2])
list_11 = list(rect1)
list_22 = list(rect2)
print("Swapped columns: ")
print(list_11)
print(list_22)
