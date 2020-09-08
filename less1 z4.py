a = int(input("Введите целое число:"))
max1= a % 10
a = a // 10
while a > 0:
    if a % 10 > max1:
        max1 = a % 10
    a = a // 10
print('%s %d' %("Максимальная цифра в Вашем числе:",max1))

