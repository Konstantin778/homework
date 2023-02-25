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


days_order = [(1, "mon"), (2, "tue"), (3, "wed"), (4, "thu"), (5, "fri"), (6, "sat"), (7, "sun")]


def reformat_date(some_list):
    if len(some_list) == 0:
        return []

    ordered_days = []
    for date in days_order:
        for day in some_list:
            try:
                if day["day"] == date[1]:
                    ordered_days.append(day)
            except Exception as e:
                return """Ошибка. Необходимо использовать список словарей установленного формата в качестве
аргумента функции"""


    time_list = []
    for elem in ordered_days:
        time_list.append((elem["day"].upper(), f'{elem["from"]} - {elem["to"]}'))


    mini_list = []
    final_list = []
    for index, elem in enumerate(time_list):

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
