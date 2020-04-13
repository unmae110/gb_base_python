my_list = [7, 5, 3, 3, 2]
try:
    usr_num = int(input('Num: '))
    if usr_num in my_list:
        my_list.insert(my_list.index(usr_num), usr_num)
    else:
        pass
except ValueError:
    print("input num: ")
print(my_list)
