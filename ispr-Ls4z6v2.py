
from itertools import cycle
my_list = [True, 'ABC', 123, None]
n = 0
for el in cycle(my_list):
    if n > 10:
        break
    else:
        print(el)
        n+=1