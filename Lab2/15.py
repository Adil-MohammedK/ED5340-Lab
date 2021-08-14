# WAP to do the following: (a) Create a list of bank accounts with name alone 
# (b) then query for a new account and insert the details wrt alphabetical order of the name 
# (c) query for a name and delete from the list 
# (d) take an input name and append at the beginning 
# (e) identifying  duplicates and remove all but one 
# (f) sort the bank accounts alphabetically. 

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

banks=['Federal','SBI','SIB','Canara','Axis','Citibank']

new_account= input("Enter new account: ")
banks.append(new_account)
banks=sorted(banks)
print(banks)

K=input("Name of bank to delete: ")
banks = [i for i in banks if i != K]
print(banks)

new_account=input("Enter name to add at beginning: ")
banks.insert(0, new_account)
print(banks)
print("removing duplicates:")
banks=duplicate_item(banks)
print(banks)
print("Sorting")
banks=sorted(banks)
print(banks)

