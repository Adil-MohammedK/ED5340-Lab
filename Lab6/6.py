import shutil
import os

print("Mode	Function Description")
print(" “r”	It opens a file in reading mode")
print(" “w”	It opens a file in write mode")
print(" “a”	Opens a file in append mode(adding text at the end of the file)")
print(" “x”	Creates a specified file, returns an error if the file already exists")
print(" “r +”   	It opens a file in both reading and writing mode")
print("   “b”	Opens a file in binary mode (in case of images, .exe files")
print(" “t”	It opens a file in text mode")


print(os.getcwd())  # Current Dir
os.mkdir('Original')  # Make dir
print(os.path.exists('Original'))  # Check if directory exist
print(os.listdir('.'))
os.chdir('Original')
os.chdir('..')
shutil.copy('sample.txt', 'Temp.txt')  # COpy
shutil.copytree('Original', 'Original-Copy')  # Copy Dir
shutil.move('sample.txt', 'Temp')  # Move file
shutil.move('Original', 'Original-Copy1')  # Move Dir
shutil.rmtree('Original-Copy')  # Remove Dir
os.remove('Temp.txt')  # Remove file
