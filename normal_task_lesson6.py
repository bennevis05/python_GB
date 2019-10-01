# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Game:
    def __init__(self, creature_1, creature_2):
        self.creature_1 = creature_1
        self.creature_2 = creature_2

    def start(self):
        who_will_attacked = self.creature_1

        while self.creature_1.health > 0 and self.creature_2.health > 0:
            if who_will_attacked == self.creature_1:
                self.creature_1.attack(self.creature_2)
                print('{} нанес {} урона по {}.'
                      .format(self.creature_1.name, self.creature_1.damage, self.creature_2.name))
                self.creature_2.armor -= 0.1
                print('У {} осталось {} здоровья.'.format(self.creature_2.name, self.creature_2.health))
                who_will_attacked = self.creature_2

            else:
                self.creature_2.attack(self.creature_1)
                print('{} нанес {} урона по {}.'
                      .format(self.creature_2.name, self.creature_2.damage, self.creature_1.name))
                self.creature_1.armor -= 0.2
                print('У {} осталось {} здоровья.'.format(self.creature_1.name, self.creature_1.health))
                who_will_attacked = self.creature_1

        if self.creature_1.health > 0:
            print('\nПобедил {}!'.format(self.creature_1.name))
        else:
            print('\nПобедил {}!'.format(self.creature_2.name))


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def __reduce_damage(self, enemy_creature):
        if enemy_creature.armor > 1:
            self.damage //= enemy_creature.armor
            return self.damage
        else:
            return self.damage

    def attack(self, enemy_creature):
        self.__reduce_damage(enemy_creature)
        enemy_creature.health -= self.damage
        return enemy_creature.health


class Player(Person):
    pass


class Enemy(Person):
    pass


player = Player('Gerald', 100.0, 40.0, 1.4)
enemy = Enemy('Troll', 150.0, 35.0, 1.2)

game = Game(player, enemy)
game.start()
