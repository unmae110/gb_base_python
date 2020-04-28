from functools import reduce
5
my_list = [i for i in range(100,1001) if not i & 1]

print(reduce(lambda a,b: a*b, my_list))