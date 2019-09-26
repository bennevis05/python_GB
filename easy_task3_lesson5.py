# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil


def copy_file(file_name):
    try:
        root, ext = os.path.splitext(file_name)
        shutil.copy2(file_name, file_name[0:-len(ext)] + '_copy.py')
        print('Файл успешно скопирован.')
    except FileNotFoundError:
        print('Файл с именем {} не найден.'.format(file_name))


if __name__ == '__main__':
    copy_file(__file__)
