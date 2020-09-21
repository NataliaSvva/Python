f_1 = open("my_file_Ls5z5.txt", 'w')
line = input("Введите цифры разделяя их пробелом:")
f_1.writelines(line)
def summary():
    try:
        my_numb = line.split()
        print(f'Сумма чисел:{sum(map(int, my_numb))}')
    except IOError:
        print('IOError')
    except ValueError:
        print('ValueError')
summary()
f_1.close()