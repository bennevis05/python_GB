# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_list_1 = ['Яблоко', 'Груша', 'Ананас', 'Персик', 'Банан', 'Арбуз']
fruits_list_2 = ['Банан', 'Персик', 'Авокадо', 'Груша', 'Слива', 'Яблоко', 'Дыня']

fruits_list_3 = [i for i in fruits_list_2 if i in fruits_list_1]

print('Первый список фруктов:', fruits_list_1)
print('Второй список фруктов:', fruits_list_2)
print('Фрукты присутствующие в обоих списках:', fruits_list_3)
