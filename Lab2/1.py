old_str = "Light is faster than sound"
print(old_str.split())
new_str = ""
for x in old_str.split():
    if x == "Light" or x == "sound":
        print(x.upper())
        new_str += x.upper() + " "
    else:
        new_str += x.capitalize() + " "
print(new_str)
