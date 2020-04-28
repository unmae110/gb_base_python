with open("file.txt", "r") as f:
    lines = 0
    for line in f:
        lines += 1
        print(f'в строке {len(line.split(" "))} слов')
print(f'всего {lines} строк')
