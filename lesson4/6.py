import time
from itertools import count, cycle

for num in count(1):
    if num == 10:
        break
    else:
        print(num)
        time.sleep(0.5)

c = 0
for letter in cycle("string"):
    if c < 10:
        print(letter)
        time.sleep(0.5)
        c += 1
    else:
        break
