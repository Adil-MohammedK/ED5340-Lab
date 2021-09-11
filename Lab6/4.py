import os

print(os.getcwd())
lst = []
tup = ()
st = {2, 3}
with open('data.txt', 'r') as file:
    for line in file:
        lst.append(line.split())
        tup += tuple(line.split())
        st.add(int(line.replace('\n', '')))

print(lst)
print(tup)
print(st)
