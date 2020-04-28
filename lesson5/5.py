import random

rand_nums = random.sample(range(-100, 5), 3)
with open("5-nums", "w") as fw:
    for i in rand_nums:
        fw.write(f'{i} ')
with open("5-nums", "r") as fr:
    sum_num = [int(i) for i in fr.readline().split()]
print(sum(sum_num))
