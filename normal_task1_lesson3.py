# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: John - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь).
# Есть условие, не отображать людей получающих более зарплату 500000.
# Так же при выводе имя должно быть полностью в верхнем регистре!

names_list = ['Jacob', 'Mason', 'Ethan', 'Noah', 'William', 'Liam', 'Daniel']
salary_list = [400000, 300000, 350000, 750000, 380000, 600000, 450000]

salary_dict = {}

# формируем словарь из двух списков
for i in zip(names_list, salary_list):
    key, value = i
    salary_dict[key] = value

# записываем данные из словаря в файл
with open('salary.txt', 'w') as f:
    for key, value in salary_dict.items():
        f.write('{} - {}\n'.format(key, value))

# выводим содержимое файла
with open('salary.txt') as f:
    strings = f.readlines()
    for i in strings:
        name, salary = i.split(' - ')
        salary = int(salary)
        if salary < 500000:
            salary *= 0.87
            print('{} - {}'.format(name.upper(), str(salary)))

input('\nНажмите Enter, чтобы выйти.')
