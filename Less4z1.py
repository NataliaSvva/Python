def zpl():
    try:
        time = float(input('Выработка в часах '))
        stav = int(input('Ставка в у.е. '))
        bonus = int(input('Премия в у.е. '))
        res = time * stav + bonus
        print(f'Заработная плата сотрудника за период составляет:  {res}')
    except ValueError:
        return print('Not a number')

zpl()