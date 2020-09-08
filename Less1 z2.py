sek = int(input("Введите колличество секунд:"))
h = sek // 3600
m = (sek-h*3600) // 60
s = sek % 60
print(h,":",m,":",s)

print('%02d %s %02d %s %02d' % (h,":",m,":",s))