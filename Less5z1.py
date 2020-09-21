f_1 = open("my_file_Ls5z1.txt", 'w')
line = input("Введите текст\n")
while line:
    f_1.writelines(f'{line}\n')
    line = input("ведите текст\n")
    if not line:
        break
f_1.close()

