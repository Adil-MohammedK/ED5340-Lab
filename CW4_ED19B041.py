# @author: Adil Mohammed K
# TODO:

list_str = ["hello", "I", "am", "Adil"]

print(len(list_str))
list_str[3:5] = [300, 400, 500]
print(list_str)
# list_str[:]=[]

print("a" in ["a", "e", "i"])

del list_str[2]
print(list_str)

print(list("Hello"))
print(min(list("Hello")))
print(max(list("Hello")))

a, b, c = 1, 2, 3
print(a, b, c, sep="+", end="!")
print(f"a={a},b={b},c={c}")  # Formatted string literals
print("a={},b={},c={}".format(a, b, c))  # Using format()
string = "I am  dope"
print(string.split(" "))

a, b, c = 12, 8, 9
if a > b > c:
    print("big is a:", a)
elif b > c:
    print("big is b:", b)
else:
    print("big is c: ", c)
str = [[1, 2, 3, 4], [5, 6, 7, 8]]
print("arr=: ", str, "*arr=: ", *str)
print("arr[0]", str[0], "arr[1]", str[1])
print("*arr[0]", *str[0])

# lst=[[x,x**2,x**3] for x in range(10)]
# print(lst)
lst = []
for x in range(10):
    lst.append([x, x ** 2, x ** 3])
print(lst)

lst3 = [x for x in range(10) if x % 2 == 0]
print(lst3)

# st5=[int(num) for num in input().split()]
# print(st5)

# List of list
lst4 = [[x, x + 5] for x in range(10)]
print(lst4)

lst5 = []
for x in range(10):
    lst5.append([x, x + 5])
print(lst5)
