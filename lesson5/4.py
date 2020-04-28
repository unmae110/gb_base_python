numbers = {"One": "один",
           "Two": "два",
           "Three": "три",
           "Four": "четыре"}
with open("4-nums", "r") as f:
    new = []
    for line in f:
        line = line.split(' ', 1)
        new.append(numbers[line[0]] + '  ' + line[1])
        # вот тут строки получаются нечитаемыми на Win если делать в UTF-8,
        # а на unix-like вероятно будут порблемы с win-1251 (не точно)
    with open("newfile", "w", encoding="windows-1251") as nf:
        for i in new:
            nf.write(i)
