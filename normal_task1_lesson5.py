# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.

import os
import easy as my_lib


def manage_folders():
    while True:
        print('''
    1 - Перейти в папку.
    2 - Просмотреть содержимое текущей папки.
    3 - Создать папку.
    4 - Удалить папку.
    0 - Выход.
    ''')

        user_choice = input('Выберите пункт меню: ')

        if user_choice == '0':
            print('\nРабота завершена.')
            break

        elif user_choice == '1':
            my_lib.change_directory(input('Введите имя папки. (Используйте "/" для указания нескольких папок): '))

        elif user_choice == '2':
            print('Содержимое текущей директории:', os.listdir(os.getcwd()))

        elif user_choice == '3':
            my_lib.make_directory(input('Введите имя папки: '))

        elif user_choice == '4':
            my_lib.remove_directory(input('Введите имя папки: '))

        else:
            print('Неверно выбран пункт меню.')


manage_folders()
