rawstr=r"I'm Adil"
print(rawstr)

# String Slicing
name1 = "Hello from Adil"
name = "Hi from Adil"
print('Name: ',name)
print('Name1: ',name1)

print(name1[0:2])
print(name1[:3])
print(name1[3:])
print(name1[-3:])
print(name1[-1:-5:-1])
print(name1[-5:-1])

#Strings are immutable
print(id(name))
print(id(name1))

# String operations
print(name+" "+name1)
print('Haha! '*100)
print(name)

print('el' in 'hello')
print('Hello' in 'Hello')