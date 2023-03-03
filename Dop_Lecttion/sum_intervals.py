"""
Напишите функцию с именем sum_len_intervals,
которая принимает несортированный массив интервалов
и возвращает сумму всех длин интервалов.

Напишите функцию sum_intervals, которая выводит
сумму полученных интервалов

Интервалы
Интервалы представлены парой целых чисел в виде массива.
Первое значение интервала всегда будет меньше второго значения.
Пример интервала:
[1, 5] это интервал от 1 до 5.
Длина этого интервала равна 4.
Сумма этого интервала равна 10.

!!!!!!!------------ТЕОРИТИЧЕСКАЯ ВАЖНАЯ ИНФОРМАЦИЯ-------------!!!!!!!
Так как питон - это язык с динамической типизацией,
то функциям не будет известно,
какого типа переменные мы подаём в аргументы,
поэтому можно ЯВНО указать тип аргумента через символ
двоеточия. Это даёт возможность в ИДЕ видеть методы
именно того типа, которые мы указали для аргумента.
Попробуйте убрать ": list" из функции и обратиться к
"intervals" через точку "intervals."
Вы не увидите методов списка, таких как append или sort
Теперь верните ": list" в аргументы функции и вы дадите функции
понимание, что сюда будет передаваться именно список
Попробуйте теперь обратиться к intervals через точку

Дополнительно.
Написать функцию валидности интервалов check_intervals.
Правил два:
1. каждый интервал - это список из двух элементов
2. в каждом интервале второй элемент больше или равен первому
"""


def is_list(intervals: list):
    if type(intervals) is not list:
        return "Ошибка. Необходимо ввести список"

    for interval in intervals:
        if type(interval) is not list or len(interval) != 2:
            return "Ошибка. Интервал должен являться списком и состоять из 2х элементов"

        if interval[0] > interval[-1]:
            return "Ошибка. Второй элемент интервала должен быть больше первого"

        else:
            continue

    return intervals


def sum_len_intervals(intervals: list):
    if is_list(intervals) == intervals:
        interval_lens = [i[-1] - i[0] for i in intervals]
        return sum(interval_lens)

    else:
        return is_list(intervals)


def sum_intervals(intervals: list):
    if is_list(intervals) == intervals:
        interval_sums = [i[-1] + i[0] for i in intervals]
        return sum(interval_sums)

    else:
        return is_list(intervals)


interval_1 = [
    [1, 2],
    [6, 10],
    [11, 15]
]
print(sum_len_intervals(interval_1))  # 9
print(sum_intervals(interval_1))  # 45

interval_2 = [
   [1, 4],
   [7, 10],
   [3, 5]
]
print(sum_len_intervals(interval_2))  # 8
print(sum_intervals(interval_2))  # 30

interval_3 = [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
]
print(sum_len_intervals(interval_3))  # 28
print(sum_intervals(interval_3))  # 94

