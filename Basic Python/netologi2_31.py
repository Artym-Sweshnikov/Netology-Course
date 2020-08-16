month = input('Введите месяц: ')
day = int(input('Введите число: '))
print('\nВывод:')

if month == 'март':
    if day >= 21:
        print('Овен')
    elif day <= 20:
        print('Рыба')
if month == 'апрель' and day >= 21:
    print('Телец')
elif month == 'апрель' and day <= 20:
    print('Овен')
if month == 'сентябрь' and day >= 24 or month == 'октябрь' and day <= 23:
    print('Весы')
elif month == 'декабрь' and day >= 23 or month == 'январь' and day <= 20:
    print('Козерог')
if month == 'май' and day >= 22:
    print('Близнец')
if month == 'июнь':
    if day >= 22:
        print('Рак')
    else:
        print('Близнец')
if month == 'октябрь' and day >= 24 or month == 'ноябрь' and day <= 22:
    print('Скорпион')
elif month == 'январь' and day >= 21 or month == 'февраль' and day <= 19:
    print('Водолей')
if month == 'июль' and day <= 22:
    print('Рак')
elif month == 'июль' and day >= 23:
    print('Лев')
if month == 'август':
    if day >= 23:
        print('Лев')
    else:
        print('Дева')
if month == 'ноябрь' and day >= 23 or month == 'декабрь' and day <= 22:
    print('Стрелец')
elif month == 'февраль' and day >= 20 or month == 'март' and day <= 20:
    print('Рыба')
if month == 'сентябрь' and day <= 23:
    print('Дева')
