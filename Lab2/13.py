def duplicate_item(x):
    size = len(x)
    duplicate = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in duplicate:
                duplicate.append(x[i])
            elif x[i] not in duplicate:
                duplicate.append(x[i])
    return duplicate

list=[]
n=int(input("How many nums needed: "))

print("Enter number for list: ")
for i in range(1,n+1):
    list.append(int(input()))
print("List: ",list)
print("Removing repeated numbers")
new_list = duplicate_item(list)
# for i in list:
#     if i not in list[i:]:
#         new_list.append(i)

# for i in range(0,n):
#     comp=list[i]
#     for x in range(i,n):
#         if list[x]==comp:
#             del list[i]

# for i in range(0,n):
#     flag=True
#     comp=list[i]
#     for x in range(i+1,n):
#         if list[x]==comp:
#             flag=False
#             break
#     if flag==True:
#         new_list.append(comp)

print("new list: ",new_list)