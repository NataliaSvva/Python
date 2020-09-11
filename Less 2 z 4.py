speak = input("Введите несколько слов через пробел:")
s = speak.split()
for ind, el in enumerate(s, 1):
    print(ind, (el[0:10]))

