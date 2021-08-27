# Python’s built-in mutable collections like lists, dicts, and sets can be copied by calling their factory functions on an existing collection:

# new_list = list(original_list)
# new_dict = dict(original_dict)
# new_set = set(original_set)

# A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. In essence, a shallow copy is only one level deep
# Example

import copy

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("list1: ", list1)
list2 = list(list1)
print("List2: ", list2)
list1.append([3, 4])
print("list1: ", list1)
print("List2: ", list2)
# Here changes to list1 doesn not change list2

list1[1][0] = "X"
print("list1: ", list1)
print("List2: ", list2)
# Here the child of the list changes
# Deep copying


list3 = copy.deepcopy(list1)
print("list1: ", list1)
print("list3: ", list3)
list1.append(14)
print("list1: ", list1)
print("list3: ", list3)
list1[2][0] = "X"
print("list1: ", list1)
print("List3: ", list3)

# Here no change happens to list3
