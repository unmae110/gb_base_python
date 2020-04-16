result = 0
while True:
    nums = input('Введите строку чисел: ')
    try:
        for i in nums.split():
            i = int(i)
            result += i
        print(result)
    except ValueError:
        print(result)
        break
