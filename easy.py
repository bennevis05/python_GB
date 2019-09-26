# Файл для импорта в задание normal

import os
import shutil


def make_directory(dir_name):
    try:
        os.mkdir(dir_name)
        print('Была создана директория с именем {}'.format(dir_name))
    except FileExistsError:
        print('Невозможно создать файл, так как он уже существует:'
              ' {}.'.format(dir_name))


def remove_directory(*args):
    for i in args:
        try:
            os.rmdir(i)
            print('Была удалена директория с именем {}'.format(i))
        except FileNotFoundError:
            print('Не удается найти указанный для удаления файл:'
                  ' {}.'.format(i))
        except OSError:
            print('Удаление невозможно. Папка не пуста.')


def change_directory(path):
    if path != '..':
        try:
            os.chdir(path)
            print('Выполнен переход в директорию {}.'.format(path))
        except FileNotFoundError:
            print('Файл с именем {} не найден.'.format(path))
    else:
        os.chdir(path)
        print('Успешно выполнен переход в директорию.')


def show_folders_only():
    current_dir_contents = [new_path for new_path in os.listdir(os.getcwd()) if os.path.isdir(new_path)]
    return current_dir_contents


def copy_file(file_name):
    try:
        root, ext = os.path.splitext(file_name)
        shutil.copy2(file_name, file_name[0:-len(ext)] + '_copy.py')
        print('Файл успешно скопирован.')
    except FileNotFoundError:
        print('Файл с именем {} не найден.'.format(file_name))
