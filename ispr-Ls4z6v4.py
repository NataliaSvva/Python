from itertools import cycle
my_list = [True, 'ABC', 123, None]
iter = cycle(my_list)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))



