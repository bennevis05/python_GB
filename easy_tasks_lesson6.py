# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('{} автомобиль {} начал ехать. Скорость: {} км/ч.'
              .format(self.color, self.name, self.speed))

    def stop(self):
        print('{} автомобиль {} остановился.'.format(self.color, self.name))

    def turn(self, location):
        print('{} автомобиль {} повернул {}.'.format(self.color, self.name, location))

    def info(self):
        print('Автомобиль - {}. Цвет - {}.'.format(self.name, self.color))
        if self.is_police:
            print('{} полицейский автомобиль.'.format(self.name))


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


car_1 = TownCar('BMW', 'Белый', 60,)
car_2 = SportCar('Porsche 911', 'Красный', 100)
car_3 = WorkCar('JCB 3CX', 'Желтый', 40)
car_4 = PoliceCar('Tesla S 85', 'Черный', 100, True)

car_1.info()
car_2.info()
car_3.info()
car_4.info()
