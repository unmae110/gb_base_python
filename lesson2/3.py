month_list = [[1, 2, 12], 'зима', [3, 4, 5], 'весна', [6, 7, 8], 'лето', [9, 10, 11], 'осень']
month_dict = {
    'Зима': (1, 2, 12),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11),
}
while True:
    try:
        usr_input = int(input('введите номер месяца: '))
        break
    except ValueError:
        continue

for i in month_list[:][0::2]:
    if usr_input in i:
        position = int(month_list.index(i)) + 1
        print(month_list[position])

for key, value in month_dict.items():
    if usr_input in value:
        print(key)
