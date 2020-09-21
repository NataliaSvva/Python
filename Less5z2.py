my_file = open('my_file_Ls5z2.txt', 'r')
line = 0
for i in my_file:
    line +=1
    word = 0
    flag = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print(i, word,'слов(а).')
print(f'Всего {line} строк(и)')
my_file.close()