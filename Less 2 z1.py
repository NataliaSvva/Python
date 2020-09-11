a = []
c = int(4)
b = str("строка")
d = tuple("кортеж")
f = list("список")
g = set("множество")
h = dict(словарь="мой")
z = bool("bool")
v = None
m = bytes(11)

a.append(b)
a.append(c)
a.append(d)
a.append(f)
a.append(g)
a.append(h)
a.append(z)
a.append(v)
a.append(m)
print([a])
for el in a:
    el1 = type(el)
    print('%s %s %s %s'%("Тип данных:",(el),"равен:",(el1)))





