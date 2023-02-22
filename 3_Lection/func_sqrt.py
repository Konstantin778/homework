"""
Задние
Сделать функцию, которая определяет: число в аргументе квадрат или нет
"""


def is_square(number):
    if type(number) is not int:
        return "Ошибка. Необходимо ввести целое число"

    if number ** 0.5 != int(number ** 0.5):
        return False
    else:
        return True

print(is_square(25)) # True
print(is_square(30)) # False
