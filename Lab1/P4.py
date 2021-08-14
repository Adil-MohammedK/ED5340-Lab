# Creating a String with double Quotes
str1 = "I'm a Dude"
print("String with the use of Double Quotes: ")
print(str1)
print(type(str1))
   
# Creating String with triple Quotes allows multiple lines
str1 = '''IIT
            Madras
            Life'''
print("\nCreating a multiline String: ")
print(str1)

String1 = 'Strings are strange'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with triple Quotes
String1 = '''I am "strange"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(type(String1))

print("Slicng down \_(\")_/")
print(String1[0:2]) # Slice from char 0 to 1
print(String1[:3]) # Slice from start to 2
print(String1[3:])# Slice from char 3 to end
print(String1[-3:]) # Slice from char 3 from end to end
print(String1[-5:-1])