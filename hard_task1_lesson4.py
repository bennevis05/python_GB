person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    # введена дополнительная проверка на отрицательное число
    if money < 0:
        return 'Введено отрицательное число.'
    elif person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    # в if и elif было сравнение со строками, а не с числами. Исправлено
    if choice == 1:
        print(check_account(person))
    elif choice == 2:
        count = float(input('Сумма к снятию:'))
        print(withdraw_money(person, count))


def start():
    while True:
        try:
            card_number, pin_code = input('Введите номер карты и пин код через пробел: ').split()
            card_number = int(card_number)
            pin_code = int(pin_code)
            break
        # перехватываем ошибку если введены буквы, не цифры или неверное количество пробелов
        except ValueError:
            print('Необходио ввести только цифры. 16 цифр в номере карты и 4 цифры пин код.')

    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            try:
                choice = int(input('\nВыберите пункт:\n'
                                   '1. Проверить баланс\n'
                                   '2. Снять деньги\n'
                                   '3. Выход\n'
                                   '---------------------\n'
                                   'Ваш выбор: '))
                if choice == 3:
                    break
                elif choice > 3 or choice < 1:
                    print('Выбран неверный пункт меню.')
                else:
                    process_user_choice(choice, person)
            # перехватываем ошибку если введены буквы или не цифры
            except ValueError:
                print('Неверный ввод.')
    else:
        print('Номер карты или пин код введены не верно!')


start()
