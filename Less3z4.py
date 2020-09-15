def my_func(x, y):
    s = x ** (abs(y))
    print(s)

x = int(input("Введите действительное положительное число:"))
y = int(input("Введите целое отрицательное число:"))
my_func(x, y)

