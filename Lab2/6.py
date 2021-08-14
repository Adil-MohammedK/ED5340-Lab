# Continue 
# This statement is used to skip over the execution part of the loop on a certain condition.
#  Basically, it skips its following statements and continues with the next iteration of the loop

for i in range(1,15):
    if i==9:
        continue # Printing 9 is skipped but goes into next loop
    print(i)

# Pass
# We use pass statement to write empty loops.
# use it when starting a new project to create functions that I will use later, but I will have no need for them at the moment.

str='Indian Institute'
for x in str:
    if x=='n':
        pass
    print(x)