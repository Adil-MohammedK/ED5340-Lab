# For a dictionary, arrange them in the alphabetical order of the 'keys'.
# Insert a few key: value pair following(i) the alphabetical order of keys. (ii) sort using 'values

myDict = {'name': 12, 'age': 24, 'dob': 1244}
print('Original dict: ', myDict)

# Use Dict comprehension for soring
myDict = {i: myDict[i] for i in sorted(myDict)}
print("Ordered dict by key:", myDict)

# updating
myDict.update([('Austria', 43), ('Russia', 7), ('India', 1), ('Qatar', 2)])
print('New dict: ', myDict)
# Use Dict comprehension for soring
myDict = {i: myDict[i] for i in sorted(myDict, key=str.upper)}
print("Ordered dict by key:", myDict)

# Sort according to values
myDict = sorted(myDict.items(), key=lambda kv1: kv1[1])
print(myDict)
