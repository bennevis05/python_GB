# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def max_number(a, b, c):
    # return max(a, b, c)
    if b < a > c:
        return a
    elif a < b > c:
        return b
    else:
        return c


print('Максимальное число из 9, 7 и 5, это:', max_number(9, 7, 5))
