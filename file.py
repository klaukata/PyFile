import os
import shutil

cwd = os.getcwd()
test_folder_path = cwd + r"\test"
# path = input('enter path to a folder: ')
files = os.listdir(test_folder_path)
extensions = []
for file in files:
    names, extension = os.path.splitext(file)
    extension = extension[1:]
    # file_path =
    os.makedirs(test_folder_path + f'/{extension}', exist_ok=True)
    print(test_folder_path)

# for extension in extensions:
    # print(extension)
    # os.makedirs(test_folder_path + f'/{extension}', exist_ok=True)

# print(files)