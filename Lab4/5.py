# (5)(a) find a number is even or odd
# (b) To find the number of vowels / consonants(use single function to do both).

def DoBoth(Num, str):
    vowels = 0
    consonants = 0
    if Num % 2 == 0:
        NumStatus = 'Even'
    else:
        NumStatus = 'Odd'
    for i in str:
        if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
            vowels += 1
        elif i == ' ':
            pass
        else:
            consonants += 1
    return NumStatus, vowels, consonants


num = int(input("Enter the num: "))
string = input("Enter String: ")
OddEven, vowels, cons = DoBoth(num, string)

print('The number ', num, " is: ", OddEven)
print('NUmber of vowels: ', vowels)
print('NUmber of consonants: ', cons)
