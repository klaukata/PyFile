import os

cwd = os.getcwd()
# path = input('enter path to a folder: ')
files = os.listdir(cwd)

for file in files:
    name, extension = os.path.splitext(file)
    if extension.startswith('.'): extension = extension[1:]

# print(dir(os.path))