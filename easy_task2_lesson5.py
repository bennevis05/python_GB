# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os


def show_folders_only():
    current_dir_contents = [new_path for new_path in os.listdir(os.getcwd()) if os.path.isdir(new_path)]
    return current_dir_contents


if __name__ == '__main__':
    print('В данной директории есть следующие папки:', show_folders_only())
