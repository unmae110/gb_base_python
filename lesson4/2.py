my_list = [32, 25, 87, 14, 489]

new_list = []
for idx, itm in enumerate(my_list[:]):
    if itm > my_list[idx - 1]:
        new_list.append(itm)
print(new_list)

result = [itm for idx, itm in enumerate(my_list) if itm > my_list[idx - 1]]
print(result)
