# Join Tuples if similar initial element
list1 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13), (5, 10)]

print("original list is : " + str(list1))

resList = []
for sub in list1:
    if resList and resList[-1][0] == sub[0]:
        resList[-1].extend(sub[1:])
    else:
        resList.append([ele for ele in sub])
resList = list(map(tuple, resList))

# printing result
print("extracted elements : " + str(resList))
