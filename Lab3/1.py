name=('Adil','Rohit','Ramshid','Ram','John','Aysha')
age=(21,25,30,50,15,22)
salary=(50000,15000,30000,150000,35000,40000)

ite=zip(name,age,salary)

print(*ite)

list=[]
for names,ages,salaries in zip(name,age,salary):
    print ("Name : ",names," Age: ",ages," Salary: ",salaries)
    list.append([names,ages,salaries])

print(list) # list is indexed
print(list[1])
print(list[1][0])

