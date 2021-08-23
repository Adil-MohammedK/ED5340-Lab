firstMatrix = ((1,1,1),(1,1,1),(1,1,1))
secondMatrix = ((4,4,4),(5,8,5),(6,6,6))
# print(firstMatrix)

# Addition

sumMatrix = tuple([[firstMatrix[i][j]+secondMatrix[i][j] for j in range (len(firstMatrix[0]))] for i in range(len(firstMatrix))])
print("SUM: ")
print(sumMatrix)
for r in sumMatrix:
    print (r)

# Subraction

subMatrix = tuple([[firstMatrix[i][j]-secondMatrix[i][j] for j in range (len(firstMatrix[0]))] for i in range(len(firstMatrix))])
print("DIFF: ")
print(subMatrix)
for r in subMatrix:
    print (r)

# Multiplication
multMatrix = ((0,0,0),(0,0,0),(0,0,0))
multMatrix = tuple([[multMatrix[i][j]+firstMatrix[i][k]*secondMatrix[k][i] for k in range(len(secondMatrix))] for j in range(len(secondMatrix[0])) for i in range(len(firstMatrix)) ])
print("MULT: ")
print(multMatrix)

# TODO: Finsih Multiplication

# Multiplication old way using loops
multMatrix=[[0,0,0],
            [0,0,0],
            [0,0,0]]
for i in range(len(firstMatrix)):
    for j in range(len(secondMatrix[0])):
        for k in range(len(secondMatrix)):
            multMatrix[i][j] += firstMatrix[i][k] * secondMatrix[k][j]
 
for r in multMatrix:
    print(r)

# Transpose
print("TRANS: ")
matTranspose = [[row[i] for row in secondMatrix] for i in range(len(secondMatrix))]
for r in matTranspose:
    print (r)

# Trace
trace=[0]
traceVar = [secondMatrix[i][j] for j in range(len(secondMatrix)) for i in range(len(secondMatrix[0])) if i==j ]
print("Trace: ",sum(traceVar))

# Using zip Addition
sumZip = [map(sum, zip(*i)) for i in zip(firstMatrix, secondMatrix)] 
print("SUM(zip): ")
for r in sumZip:
    print (*r)

# TODO: Subtraction

Ziped = zip(firstMatrix,secondMatrix)
count = 0
for item in Ziped:
    print(item[0][count]-item[1][count])
    count+=1
# print("Sub(zip): ",subZip)


# Multiplication
multZip = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*secondMatrix)]
                                for A_row in firstMatrix]
print("Mult (zip): ")
for r in multZip:
    print(r)

# Transpose

ite=zip(*secondMatrix)
transZip=list(ite)
print("Trans (zip): ")
for r in transZip:
    print(r)

# Trace

traceItem=zip(secondMatrix)
# print(*ite)
trace=0
i=0
for x in traceItem:
    # print(x[0][i])
    trace+=x[0][i]
    i+=1
print(trace)
