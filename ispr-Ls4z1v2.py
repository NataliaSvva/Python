from sys import argv
def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'{"Отработано:",time,"Тарифная ставка:", rate,"Премия:",bonus}')
        print(f'Salary - {time * rate + bonus}')
    except ValueError:
        print('Not a number')
salary()