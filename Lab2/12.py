# WAP to sort the list A=[5,3,1,2,4,0] in descending order i.e [5,4,3,2,1,0] ( dont use any inbuilt function for this)

A=[5,3,1,2,4,0]
print("Old: ",A)
for i in range(len(A)):
    for j in range(len(A) - 1):
        if A[j] < A[j+1]:
            A[j], A[j + 1] = A[j + 1], A[j]
print("new: ",A)
