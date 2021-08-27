lst = ["Hello", "I", "am", "Adil", "Mohammed", "Kizhakkethil"]

len_list = []
total = 0

for x in lst:
    # print(x)
    len_list.append(len(x))
    total += len(x)

print("Length of strings in list is: ", len_list)
print("Total chars in list: ", total)
