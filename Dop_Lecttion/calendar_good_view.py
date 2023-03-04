"""
СЛОЖНЫЙ УРОВЕНЬ

Функция должна принимать неотсортированный список из 0-7 элементов.
Если список пуст, он просто возвращает пустой массив.
В противном случае он должен составить
отсортированное удобное для человека расписание
рабочего времени и вернуть его как string.

Формат вывода за один
день должен быть ВС: 11:00 - 23:00.

Если два или более дней недели подряд имеют
одинаковые рабочие часы, они должны быть объединены
и иметь следующий формат: ПН - СР: 11:00 - 23:00.
ИНФОРМАЦИЯ
Метод sort у списка переделывает в сортированный список
По стандарту - идёт сортировка от меньшего к большему,
в алфавите от a до z и тд.
Если мы сортируем список из элементов составных типов данных,
то нам нужно указать по какой логике будет идти сортировка
для этого есть аргумент key. Посмотрите файл list_sort в папке info.
"""


def reformat_date(date_list: list):

    for item in date_list:
        if len(item) != 3 and type(item) is not dict:
            return "Ошибка. Необходимо ввести список словарей"
        if {"day", "from", "to"} != item.keys():
                return "Ошибка. Элемент списка должен быть составлен в нужном формате"

    ordered_list = sorted(date_list, key=lambda x: x["day"])
    days_order = {0: "пн", 1: "вт", 2: "ср", 3: "чт", 4: "пт", 5: "сб", 6: "вс"}
    temporary = []

    for key, value in days_order.items():
        for elem in ordered_list:
            if key == elem["day"]:
                elem["day"] = value
                temporary.append((elem["day"].upper(), f'{elem["from"]} - {elem["to"]}'))

    zipped_list = list(zip(temporary, temporary[1:]))

    days_interval = []
    result = []

    for index, elem in enumerate(zipped_list):
        days_interval.append(elem[0][0])
        days_interval.append(elem[1][0])

        if index < len(zipped_list) - 1:
            if elem[0][1] == elem[1][1]:
                continue
            del days_interval[-1]

        else:
            if elem[0][1] != elem[1][1]:

                if len(days_interval) > 2:
                    result.append(f'{days_interval[0]} - {days_interval[-2]}: {elem[0][1]}')
                else:
                    result.append(f'{days_interval[0]}: {elem[0][1]}')

                result.append(f'{days_interval[-1]}: {elem[1][1]}')
                continue
            pass

        if days_interval[0] == days_interval[-1]:
            result.append(f'{days_interval[-1]}: {elem[0][1]}')
        else:
            result.append(f'{days_interval[0]} - {days_interval[-1]}: {elem[0][1]}')

        days_interval.clear()

    return '\n'.join(result)


print(reformat_date([
    {
        "day": 6,
        "from": "10:00",
        "to": "23:00"
    },
    {
        "day": 0,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 1,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 2,
        "from": "11:00",
        "to": "23:00"
    },
    {
        "day": 3,
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": 4,
        "from": "12:00",
        "to": "23:00"
    },
    {
        "day": 5,
        "from": "11:00",
        "to": "23:00"
    }
]))

## На консоле должно быть
# ПН - СР: 11:00 - 23:00
# ЧТ - ПТ: 12:00 - 23:00
# СБ: 10:00 - 23:00
# ВС: 11:00 - 23:00
