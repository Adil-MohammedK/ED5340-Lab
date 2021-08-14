list_str= ['hello','I','am','Adil']

print(len(list_str))
list_str[3:5]=[300,400,500]
print(list_str)
# list_str[:]=[]

print('a' in ['a','e','i'])

del(list_str[2])
print(list_str)

print(list("Hello"))
print(min(list("Hello")))
print(max(list("Hello")))

a,b,c=1,2,3
print(a,b,c,sep='+',end='!')
print(f'a={a},b={b},c={c}') # Formatted string literals
print("a={},b={},c={}".format(a,b,c)) # Using format()
string="I am  dope"
print(string.split(" "))

a,b,c=12,8,9
if a>b>c:
    print("big is a:",a)
elif b>c:
    print("big is b:",b)
else:
    print("big is c: ",c)