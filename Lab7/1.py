import csv

fields = ["Students", "Marks"]
rows = [["Name1", "23"], ["Name2", "25"], ["Name3", "21"], ["Name5", "12"], ["Name4", "30"]]

with open("data1.txt", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
csvfile.close()

studData = []
with open("data1.txt") as file:
    reader = csv.DictReader(file, delimiter=",")
    for index, row in enumerate(reader):
        studData.append({"StudName": row["Students"], "Marks": row["Marks"]})
file.close()
# print(studData)
for stud in studData:
    print(stud)
