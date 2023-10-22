import os
import shutil

# Here are gathered the files from the folder based on the input

files = os.listdir(input("The path of the selected files: "))

# List to string plus replacing jpg to nef
f = '-'.join(files)
fJPG2NEF = f.replace(".JPG", ".NEF")

# String to List
data = []
for line in fJPG2NEF.split('-'):
    first_part = line[:+12]
    data.append(first_part)
print("")
# Copy of the files from the main NEF folder to a new one with only the selected photos
src = input("\nThe source folder: ")
trg = input("\nTahe destination folder: ")

filles = data
for fname in filles:
    shutil.copy2(os.path.join(src, fname), trg)

print("\nCopy completed")
# Print stuff only to see if they are working
"""print()
print(files)
print(' ')
print(f)
print(' ')
print(fJPG2NEF)
print(' ')
print(data)
print(' ')"""