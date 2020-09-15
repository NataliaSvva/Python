def my_func(x, y):
    s=1
    while (y > 0):
        s *= x
        y-=1
    print(s)


x = int(input("Введите действительное положительное число:"))
y = abs(int(input("Введите целое отрицательное число:")))
my_func(x, y)
