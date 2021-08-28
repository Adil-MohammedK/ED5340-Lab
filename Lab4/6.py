# Write a function to find out if a given matrix (of arbitrary order) is symmetric or not.

def isSymmetric(matrix, M, N):
    if M != N:
        print('Not a square matrix')
        return "Not Symmetric"
    matTranspose = [[row[i] for row in matrix]
                    for i in range(len(matrix))]
    print("Transpose is:", matTranspose)
    for i in range(M):
        for j in range(N):
            if (matrix[i][j] != matTranspose[i][j]):
                return 'Not Symmetric'
    return 'Symmetric'


rows = int(input("Enter the num of rows: "))
cols = int(input("Enter the num of columns: "))
mat = []
for i in range(rows):
    subMat = []
    for j in range(cols):
        subMat.append(int(input("Enter num: ")))
    mat.append(subMat)
print('Matrix is: ', mat)
status = isSymmetric(mat, rows, cols)
print('Matrix is ', status)
