def s_func(**kwargs):
    print(f"name - {name}, soname - {soname}, year - {year}, sity - {sity}, email - {email}, pfone - {pfone}")
    return kwargs

name = input(("Введите Ваше Имя: "))
soname = input(("Введите Вашу Фамилию: "))
year = input(("Введите год Вашего рождения: "))
sity = input(("Введите город Вашего проживания: "))
email = input(("Введите Ваш email: "))
pfone = input(("Введите номер Вашего телефона: "))
s_func()
