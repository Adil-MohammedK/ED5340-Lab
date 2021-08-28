studlist = {
    "Anand": {"DOB": 1204, "Roll": 25, 'cgpa': 9},
    "Adil": {"DOB": 450, "Roll": 21, 'cgpa': 10},
    "Mahir": {"DOB": 2004, "Roll": 12},
}

print("Initially: ", studlist)

for obj in studlist:
    # print(studlist[obj])
    studlist[obj] = sorted(studlist[obj].items(),
                           key=lambda kv1: kv1[1])  # Sorting inner dict

myDict = {i: studlist[i] for i in sorted(
    studlist, key=str.upper)}  # Sorting outer Dict
print("After sorting: ", myDict)
