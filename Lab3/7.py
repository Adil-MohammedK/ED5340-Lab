# Part A

myList = [1,6,9,12,13]
print("my list: ",myList)


lists = [[]]
for i in range(len(myList) + 1):
    for j in range(i):
        lists.append(myList[j: i])

print(lists)

# Part B

order = int(input("ENter on which numbered sublist to add: "))
nums = int(input("Enter how many to add: "))
# print(lists[order])
for x in range(nums):
    lists[order].append(int(input()))
print(lists)

replace = int(input("Enter which number to replace in which order to what number: "))
order = int(input("order: "))
nums = int(input("Numer to add: "))
lists[order] = [nums if x==replace else x for x in lists[order]]
print(lists)

order = int(input("ENter on sublist to make empty: "))
lists[order].clear()
print(lists)



