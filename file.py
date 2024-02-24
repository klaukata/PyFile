import os
import shutil

cwd = os.getcwd()
test_folder_path = cwd + r"\test"
# path = input('enter path to a folder: ') #implement error handling
files = os.listdir(test_folder_path)
extensions = []
for file in files: # folers???
    names, extension = os.path.splitext(file)
    extension = extension[1:]
    os.makedirs(test_folder_path + f'/{extension}', exist_ok=True)
    # print(f'{test_folder_path}\{file}')
    shutil.move(f'{test_folder_path}\{file}', f'{test_folder_path}\{extension}\{file}')
# for extension in extensions:
    # print(extension)
    # os.makedirs(test_folder_path + f'/{extension}', exist_ok=True)

# print(files)