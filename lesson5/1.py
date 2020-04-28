with open("file.txt", "w") as f:
    while True:
        if f.write(input("какой-то текст: ")):
            f.write("\n")
            continue
        else:
            break
