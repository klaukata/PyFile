import os
import shutil

cwd = os.getcwd()
test_folder = cwd + r"\test"
# path = input('enter path to a folder: ') #implement error handling
files = os.listdir(test_folder)
extensions = []
for file in files:
    names, extension = os.path.splitext(file)
    extension = extension[1:]
    folder_path = test_folder + f'/{extension}'
    folder_path_for_folders = f'{test_folder}/folders'
    proper_folder_path = folder_path_for_folders if extension == "" else folder_path
    os.makedirs(proper_folder_path, exist_ok=True)
    shutil.move(f'{test_folder}\{file}', f'{proper_folder_path}\{file}')