# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

days_dict = {1: 'Первое', 2: 'Второе', 3: 'Третье', 4: 'Четвёртое',
             5: 'Пятое', 6: 'Шестое', 7: 'Седьмое', 8: 'Восьмое',
             9: 'Девятое', 10: 'Десятое', 11: 'Одиннадцатое', 12: 'Двенадцатое',
             13: 'Тринадцатое', 14: 'Четырнадцатое', 15: 'Пятнадцатое', 16: 'Шестнадцатое',
             17: 'Семнадцатое', 18: 'Восемнадцатое', 19: 'Девятнадцатое', 20: 'Двадцатое',
             21: 'Двадцать первое', 22: 'Двадцать второе', 23: 'Двадцать третье',
             24: 'Двадацать четвёртое', 25: 'Двадцать пятое', 26: 'Двадцать шестое',
             27: 'Двадцать седьмое', 28: 'Двадцать восьмое', 29: 'Двадцать девятое',
             30: 'Тридцатое', 31: 'Тридцать первое'}

month_dict = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
              7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

# выполняем проверку на корректность ввода даты
while True:
    while True:
        date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
        if len(date) < 7:
            print('Неверный формат даты.')
        else:
            break

    date_list = date.split('.')
    day, month, year = date_list
    day, month, year = int(day), int(month), int(year)

    if day <= 0 or day > 31:
        print('Неверный формат даты (ошибочно введен день)')
    elif month <= 0 or month > 12:
        print('Неверный формат даты (ошибочно введен месяц)')
    elif year <= 0:
        print('Неверный формат даты (ошибочно введен год)')
    elif (day == 30 or day == 31) and month == 2:
        print('Не бывает {} февраля.'.format(day))
    else:
        break

print(days_dict[day], month_dict[month], year, 'года.')

input('\nНажмите Enter, чтобы выйти.')
