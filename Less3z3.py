def my_funs():
    min_1 = (min(arg_1, arg_2, arg_3))
    sum_max = (arg_1 + arg_2 + arg_3) - min_1
    print('%s %d ' %("Сумма максимальных чисел, равна: ",sum_max))

arg_1 = int(input("Введите 1 число:"))
arg_2 = int(input("Введите 2 число:"))
arg_3 = int(input("Введите 3 число:"))
my_funs()

