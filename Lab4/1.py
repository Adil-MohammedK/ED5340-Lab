from ordered_set import OrderedSet


str = input("Enter the string: ")
res = ""

# Without Sets

n = len(str)

# Traverse through all characters
for i in range(0, n):
    # Check if str[i] is present before it
    for j in range(0, i + 1):
        if (str[i] == str[j] or str[i] == ' '):
            break
    # If not present, then add it to
    # result.
    if (j == i):
        res = res + str[i]
print("after remvoving duplicates: ", res)

# Using Sets
setString = OrderedSet(str)
print(setString)
