list1 = []
newlist = []
pos = 1
quantity = input('кол-во елементов списка:')
for i in range(int(quantity)):
    list1.append(input('input item'))
for i in list1[1::2]:
    newlist.append(i)
for i in list1[::2]:
    newlist.insert(pos, i)
    pos += 2
print(newlist)
