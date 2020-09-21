zp = []
with open("text_3.txt", "r", encoding="utf-8") as my_f:
    zp = []
    name = []
    my_list = my_f.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            name.append(i[0])
        zp.append(i[1])
        sred = sum(map(float, zp)) / len(zp)
print('%s %s %s %d %s'%("Оклад меньше 20.000:\n", ('\n'.join(name,)),"\nCредний оклад", sred, "руб."))
my_f.close()