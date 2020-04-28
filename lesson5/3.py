with open("employees", "r") as f:
    salary = []
    for line in f:
        salary += [i for i in line.split()]
    res_dct = {salary[i]: int(salary[i + 1]) for i in range(0, len(salary), 2)}
    for key, value in res_dct.items():
        if value < 20:
            print(f'{key} имеет зп меньше 20')
    print(f'средняя зп {sum(res_dct.values()) / len(res_dct.values())}')
