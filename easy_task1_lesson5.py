# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os


def make_directory(dir_name, total_num_of_dir=1):
    for i in range(1, (int(total_num_of_dir) + 1)):
        try:
            os.mkdir('{}_{}'.format(dir_name, i))
            print('Была создана директория с именем {}'.format('{}_{}'.format(dir_name, i)))
        except FileExistsError:
            print('Невозможно создать файл, так как он уже существует:'
                  ' {}.'.format('{}_{}'.format(dir_name, i)))


def remove_directory(*args):
    for i in args:
        try:
            os.rmdir(i)
            print('Была удалена директория с именем {}'.format(i))
        except FileNotFoundError:
            print('Не удается найти указанный для удаления файл:'
                  ' {}.'.format(i))


if __name__ == '__main__':
    make_directory('dir', 9)
    print('\nСодержание текущей директории:', os.listdir(os.getcwd()))

    input('\nНажмите Enter, чтобы продолжить.')

    remove_directory('dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9')
    print('\nСодержание текущей директории:', os.listdir(os.getcwd()))
