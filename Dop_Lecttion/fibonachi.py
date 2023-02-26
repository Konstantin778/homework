"""
Написать функцию, которая выдаёт n-ное число последовательности
фибоначчи
Последовательность:
1, 1, 2, 3, 5, 8, 13, 21 ....
Правило последовательности:
Каждое следующее число - это сумма двух предыдущих
fibo(8) - должно вернуть 21
fibo(3) - должно вернуть 2

Дополнительно!
Добавьте проверки на ввод именно натурального числа
"""

def fibo(n):
    if n <= 0 or type(n) is not int:
        return "Ошибка. Необходимо ввести натуральное число."

    i_start = 1
    i_next = 1
    list_result = [i_start, i_next]
    for _ in range(2, n):
        addition = i_start + i_next
        list_result.append(addition)
        i_start = i_next
        i_next = addition

    return list_result[-1]


print(fibo(8)) # 21
print(fibo(80)) # 23416728348467685
print(fibo(5)) #5


