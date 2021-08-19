str=input("Enter the string: ")
flag=True
for i in range(0, int(len(str)/2)):
        if str[i].lower() != str[len(str)-i-1].lower():
            flag=False


if(flag):
    print(str+" is palindrome")
else:
    print(str+" is not palindrome")
