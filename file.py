import os
import shutil

def get_path():
    user_path = input('enter an absolute path to a folder that you want to organize: ')
    try:
        files_arr = os.listdir(user_path)
        organize(files_arr, user_path)
        print('Done!')
    except OSError:
        print('Incorrect folder path. Try again')
        get_path()

def organize(files, path):
    for file in files:
        names, extension = os.path.splitext(file)
        extension = extension[1:]
        folder_path = path + f'/{extension}'
        folder_path_for_folders = f'{path}/folders'
        proper_folder_path = folder_path_for_folders if extension == "" else folder_path
        os.makedirs(proper_folder_path, exist_ok=True)
        shutil.move(f'{path}\{file}', f'{proper_folder_path}\{file}')

get_path()