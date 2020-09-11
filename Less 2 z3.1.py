month = int(input("Введите месяц в виде целого числа от 1 до 12:"))
my_dict = {"Зима":(1,2,12),
           "Весна":(3,4,5),
           "Лето":(6,7,8),
           "Осень":(9,10,11)}
while month <= 0 or month > 12:
    month = int(input("Введите месяц в виде целого числа от 1 до 12:"))
for el in my_dict.keys():
    if month in my_dict[el]:
        print(el)
