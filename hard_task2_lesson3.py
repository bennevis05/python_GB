# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


def reduce_damage(attacker, attacked):
    attacker['damage'] = float(attacker['damage'])
    attacked['armor'] = float(attacked['armor'])
    attacker['damage'] = round(attacker['damage'] / attacked['armor'], 1)
    return attacker


def attack(attacker, attacked):
    attacked['health'] = float(attacked['health'])
    attacked['health'] = round(attacked['health'] - attacker['damage'], 1)
    return attacked


def read_file(path):
    creature_info = {}
    with open(path) as f:
        for string in f.readlines():
            keys, val = string.strip().split(':')
            creature_info[keys] = val
    return creature_info


# записываем в файл данные игрока
player = {'name': input('Введите имя: '), 'health': 100, 'damage': 20, 'armor': 1.4}
with open('user_creature.txt', 'w') as file:
    for key, value in player.items():
        file.write('{}:{}\n'.format(key, value))

# записываем в файл данные противника
enemy = {'name': 'Black Troll', 'health': 150, 'damage': 15, 'armor': 1.2}
with open('enemy_creature.txt', 'w') as file:
    for key, value in enemy.items():
        file.write('{}:{}\n'.format(key, value))

# считываем из файлом информанию и записываем в словари
user_creature = read_file('user_creature.txt')
enemy_creature = read_file('enemy_creature.txt')

# снижаем урон в зависимости от показателя брони
user_creature = reduce_damage(user_creature, enemy_creature)
enemy_creature = reduce_damage(enemy_creature, user_creature)

# используем переменную-счетчик для смены ходов
players_turn = 1

while True:
    if float(enemy_creature['health']) >= 0 and players_turn == 1:
        print('\nАтакует {} и наносит {} урона.'.format(user_creature['name'], user_creature['damage']))
        attack(user_creature, enemy_creature)
        print('У {} {} здоровья.'.format(enemy_creature['name'], enemy_creature['health']))
        players_turn = 2

        # в случае победы выводим сообщение
        if float(enemy_creature['health']) <= 0:
            print('\nУ {} не осталось здоровья, чтобы продолжать битву.'.format(enemy_creature['name']))
            print('\nПобедил {}! У него осталось {} здоровья.'.format(user_creature['name'], user_creature['health']))
            break

    elif float(user_creature['health']) >= 0 and players_turn == 2:
        print('\nАтакует {} и наносит {} урона.'.format(enemy_creature['name'], enemy_creature['damage']))
        attack(enemy_creature, user_creature)
        print('У {} {} здоровья.'.format(user_creature['name'], user_creature['health']))
        players_turn = 1

        # в случае победы выводим сообщение
        if float(user_creature['health']) <= 0:
            print('\nУ {} не осталось здоровья, чтобы продолжать битву.'.format(user_creature['name']))
            print('\nПобедил {}! У него осталось {} здоровья.'.format(enemy_creature['name'], enemy_creature['health']))
            break

    else:
        break

input('\nНажмите Enter, чтобы выйти.')
