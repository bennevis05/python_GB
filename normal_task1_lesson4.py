# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки,
# имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате:
# текст в нижнем регистре, допускается
# нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.

import re

pattern_name_surname = '[А-ЯA-Z]'
pattern_email = '[a-z_\.0-9]+@[a-z]+\.(ru|com|org)'

while True:
    while True:
        name = input('Введите имя: ')
        if not re.match(pattern_name_surname, name):
            print('Введите имя с большой буквы.')
        else:
            break
    while True:
        surname = input('Введите фамилию: ')
        if not re.match(pattern_name_surname, surname):
            print('Введите фамилию с большой буквы.')
        else:
            break
    while True:
        email = input('Введите адрес эл. почты: ')
        if not re.fullmatch(pattern_email, email):
            print('Неверный формат эл. почты.')
        else:
            break
    break
