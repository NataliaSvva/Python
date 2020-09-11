a = list(input(("Введите произвольный список:")))
print(a)

step = 0
for el in range(int(len(a)/2)):
    a[step], a[step+1] = a[step+1], a[step]
    step +=2

print(a)