# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("\nhelp - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаление указанного файла")
    print("cd <full_path or relative_path> - смена текущей директории на указанную")
    print('ls - отображение полного пути текущей директории')
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("Директория {} создана". format(dir_name))
    except FileExistsError:
        print("Директория {} уже существует". format(dir_name))


def copy_files():
    try:
        root, ext = os.path.splitext(file_name)
        shutil.copy2(file_name, '{}_copy{}'.format(file_name[0:-len(ext)], ext))
        print('Файл успешно скопирован.')
    except FileNotFoundError:
        print('Файл с именем {} не найден.'.format(file_name))


def remove_files():
    user_choice = input('Подтвердите удаление файла (Y/N) ')
    user_choice = user_choice.lower()
    if user_choice == 'y':
        try:
            os.remove(file_name)
            print('Был удален файл с именем {}'.format(file_name))
        except FileNotFoundError:
            print('Не удается найти указанный для удаления файл:'
                  ' {}.'.format(file_name))
    elif user_choice == 'n':
        print('Отмена удаления файла.')
        return
    else:
        print('Неверный ввод.')
        return


def change_directory():
    if path_name != '..':
        try:
            os.chdir(path_name)
            print('Выполнен переход в директорию {}.'.format(path_name))
        except FileNotFoundError:
            print('Файл с именем {} не найден.'.format(path_name))
    else:
        os.chdir(path_name)
        print('Успешно выполнен переход в директорию.')


def current_directory():
    print(os.getcwd())


def ping():
    print("pong")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_files,
    "rm": remove_files,
    "cd": change_directory,
    "ls": current_directory}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None
try:
    path_name = sys.argv[2]
except IndexError:
    path_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
else:
    print("Задан неверный ключ.")
    print("Укажите ключ help для получения справки.")
