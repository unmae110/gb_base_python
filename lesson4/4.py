from random import choices, randint

my_list = [randint(-10, 10) for _ in range(30)]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(my_list)
print(new_list)
