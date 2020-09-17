my_list = [22, 18, 22, 12, 33, 22, 8, 13, 8, 13]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)

