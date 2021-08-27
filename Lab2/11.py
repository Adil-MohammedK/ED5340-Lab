# (11) Create a list of random integers in range(1,100) , find the median of the numbers in the list, later divide the list into two sublists with respect to the median.
import random

n = int(input("Enter how many nums needed: "))

list = []
for i in range(n):
    list.append(random.randint(1, 101))
print("List: ", list)

sorted_list = sorted(list)
print("List: ", sorted_list)
if n % 2 == 0:
    median = (sorted_list[n // 2 - 1] + sorted_list[(n // 2)]) / 2
    left_list = sorted_list[0 : n // 2]
    right_list = sorted_list[n // 2 :]
else:
    median = sorted_list[n // 2]
    left_list = sorted_list[0 : n // 2]
    right_list = sorted_list[n // 2 + 1 :]
print("Median: ", median)

print("two lists: ")
print(left_list)
print(right_list)
