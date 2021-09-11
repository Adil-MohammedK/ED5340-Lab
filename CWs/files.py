import os
import shutil

f = open('messages.txt', 'w')
f.write("Hello")
f.close()

print(os.name)
print(os.getcwd())
print(os.listdir('.'))
print(os.listdir('..'))

if os.path.exists('TestDir'):
    print("Exists")
else:
    os.mkdir('TestDir')

os.chdir('TestDir')
print(os.getcwd())

f = open('myfile', 'w')
f.write("Made file")
f.close()
stats = os.stat('myfile')
print(stats.st_size)
