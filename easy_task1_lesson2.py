# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruits = ['Яблоко', 'Банан', 'Киви', 'Арбуз', 'Апельсин']
max_length = 0

for word in fruits:  # находим самое длинное слово в нашем списке
    length = len(word)
    if length > max_length:
        max_length = length

i = 1

for fruit in fruits:
    print('{}.'.format(i), fruit.rjust(max_length))
    i += 1

input('\nНажмите Enter, чтобы выйти.')
