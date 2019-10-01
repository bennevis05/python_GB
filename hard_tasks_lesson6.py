# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class ToyFactory:
    def __init__(self, variable_name, name, color, kind):
        self.variable_name = variable_name
        self.name = name
        self.color = color
        self.kind = kind

    def create_toy(self, class_name):
        self.variable_name = class_name(self.name, self.color, self.kind)
        return self.variable_name


class Toy:
    def __init__(self, name, color, kind):
        self.name = name
        self.color = color
        self.kind = kind

    def purchase_materials(self):
        print('Закуплено сырье. Цвет {}.'.format(self.color))

    def making(self):
        print('Пошита игрушка: {}'.format(self.kind))

    def paint(self):
        print('Игрушка {} окрашена в {} цвет.'.format(self.name, self.color))

    def toy_info(self):
        print('Была создана игрушка. Имя: {}. Цвет: {}. Тип: {}.'
              .format(self.name, self.color, self.kind))


toy_1 = Toy('Банни', 'белый', 'кролик')
toy_1.toy_info()
