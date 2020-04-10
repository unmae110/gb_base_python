str_num = input('input num: ')
# print(max(str_num))


maxnum = 0
for i in str_num:
    while int(i) > maxnum:
        maxnum = int(i)
print(maxnum)
