mes = int(input("Введите месяц в виде целого числа от 1 до 12:"))
my_list = ["зима", "весна", "лето", "осень"]
mes1 = 0
while mes <= 0 or mes > 12:
    mes = int(input("Введите месяц в виде целого числа от 1 до 12:"))
if mes == 12 or mes == 1 or mes == 2:
    mes1 = 0
elif mes == 3 or mes == 4 or mes == 5:
    mes1 = 1
elif mes == 6 or mes == 7 or mes == 8:
    mes1 = 2
elif mes == 9 or mes == 10 or mes == 11:
           mes1 = 3
else: mes1 = "null"
print(my_list[mes1])


