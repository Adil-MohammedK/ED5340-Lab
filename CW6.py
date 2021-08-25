from typing import Dict


setA = set()

setA = {20,30,40,50,14,15,20}
print(setA)
setA.add(23)
print(setA)
setA.add(15)
print(setA)
setA.remove(20)
print(setA)
setA.discard(14)
print(setA)
setA.clear()
print(setA)

set2={2,3,6,5,4}
setA = {45,67,54}

print(setA)

setC = set([x**2 for x in range(1,10)])
print(setC)

setA = {10,20,30,40,50}
setB = {30,40,50,60}

print(setA | setB)
print(setA & setB)
print(setA - setB)
print(setB - setA)

setA-=setB
print(setA)

# Dictionary

dct1 = {20: 100, 10:200,'ED2':'name1','ED1':'name2'}
print(dct1)
# print(dct1[0])
print(dct1[20])
print('Via keyvalue pair: ')
for k,v in dct1.items():
    print(k,v)

print('Via key pair: ')
for k in dct1.keys():
    print(k)

print('Via dict: ')
for k in dct1:
    print(k)

print('Via keys pair: ')
for k in dct1.keys():
    print(k,dct1[k])

lst = [10,35,'name']
dct2 = dict.fromkeys(lst,24)
print(dct2)

tup = (('name',15),('hello',23),('boy',12))
dct3 = dict.fromkeys(tup,24)
print(dct3)
dct2['part'] = 20
print(dct2)
del(dct2[10])
print(dct2)
# for k in dct2.keys():  RuntimeErrors
#     del(dct2[k])

studlist = {'Anand':{'DOB':'211255','ROll':25},
            'Adil':{'DOB':'45421','Roll':21}}
print(studlist)
print('Via keys pair: ')
for k in studlist.keys():
    print(k,studlist[k])

print('Only DOB')
for k in studlist.values():
    print(k['DOB'])

print(*studlist)
print(**studlist)