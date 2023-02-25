dates = [
    {
        "day": "sat",
        "from": "10:00",
        "to": "23:00"
    },
    {
        "day": "mon",
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": "tue",
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": "wed",
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": "thu",
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": "fri",
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": "sun",
        "from": "11:00",
        "to": "23:00"
    }
]

# Создание списка с упорядоченными днями недели.
days_order = [(1, "mon"), (2, "tue"), (3, "wed"), (4, "thu"), (5, "fri"), (6, "sat"), (7, "sun")]

# Создание функции, принимающей в себя список.
def reformat_date(some_list):
    if len(some_list) == 0:
        return []
    #Цикл проходящий по списку с упорядоченными днями, внутри которого проходит цикл по элементам
    #списка, принятого в функцию в качестве аргумента. В результате элементы принятого списка
    #записываются в порядке дней недели в список ordered_days
    ordered_days = []
    for date in days_order:
        for day in some_list:
            try:
                if day["day"] == date[1]:
                    ordered_days.append(day)
            except Exception as e:
                return """Ошибка. Необходимо использовать список словарей установленного формата в качестве
аргумента функции"""

    # Цикл принимает список словарей, упорядоченных по дням недели. В результате создаётсы список кортежей
    #time_list. В каждом кортеже в формате строк находятся 2 элемента: день недели в верхнем регистре на
    #первой позиции и часы работы в формате 'ЧЧ.ММ - ЧЧ.ММ' на второй позиции.
    time_list = []
    for elem in ordered_days:
        time_list.append((elem["day"].upper(), f'{elem["from"]} - {elem["to"]}'))

    #Цикл принимает данные из списка кортежей time_list и записывает расписание в нужном формате
    #в список final_list, состоящий из строк.
    mini_list = []
    final_list = []
    for index, elem in enumerate(time_list):
        # Если часы работы со 2го дня совпадают предыдущим днём, то название предыдущего дня заносится в mini_list.
        # Иначе название предыдущего дня также заносится в mini_list и если в mini_list было несколько дней,
        # то в final_list заносятся:
        # 1) первый и последний день идущие подряд и имеющие одинаковое расписание;  2)само расписание.
        # если в mini_list один день, то в final_list вносится этот день и расписание
        # mini_list очищается для следующей итерации
            if 0 < index:
                if elem[1] == time_list[index - 1][1]:
                    mini_list.append(time_list[index - 1][0])
                else:
                    mini_list.append(time_list[index - 1][0])
                    if len(mini_list) > 1:
                        final_list.append(f'{mini_list[0]} - {mini_list[-1]}: {time_list[index - 1][1]}')
                    else:
                        final_list.append(f'{mini_list[0]}: {time_list[index - 1][1]}')
                    mini_list.clear()

            # Если это последний элемент списка и часы работы этого дня совпадают предыдущим днём,
            # то в mini_list вносится название предыдущего дня и затем название этого дня
            # в final_list заносятся первый и последний день (текущий) подряд с одинаковым расписанием и само расписание.
            # Если часы работы этого дня не совпадают предыдущим днём, то в final_list заносится этот день и расписание
            # mini_list очищается
            if index == len(time_list) - 1:
                if elem[1] == time_list[index - 1][1]:
                    mini_list.append(time_list[index - 1][0])
                    mini_list.append(elem[0])
                    final_list.append(f'{mini_list[0]} - {mini_list[-1]}: {elem[1]}')
                else:
                    mini_list.append(elem[0])
                    final_list.append(f'{mini_list[0]}: {elem[1]}')
                mini_list.clear()

    output = '\n'.join(final_list)
    return output

print(reformat_date(dates))


# На консоле должно быть
# MON - WED: 11:00 - 23:00
# THU - FRI: 12:00 - 23:00
# SAT: 10:00 - 23:00
# SUN: 11:00 - 23:00
