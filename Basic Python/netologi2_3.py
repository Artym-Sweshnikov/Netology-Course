month = input('Введите месяц: ')
day = int(input('Введите число: '))
print('\nВывод:')

if month == 'март' and day >= 21 or month == 'апрель' and day <= 20:
    print('Овен')
if month == 'апрель' and day >= 21 or month == 'май' and day <= 21:
    print('Телец')
if month == 'май' and day >= 22 or month == 'июнь' and day <= 21:
    print('Близнец')
if month == 'июнь' and day >= 22 or month == 'июль' and day <= 22:
    print('Рак')
if month == 'июль' and day >= 23 or month == 'август' and day <= 23:
    print('Лев')
if month == 'август' and day >= 24 or month == 'сентябрь' and day <= 23:
    print('Дева')
if month == 'сентябрь' and day >= 24 or month == 'октябрь' and day <= 23:
    print('Весы')
if month == 'октябрь' and day >= 24 or month == 'ноябрь' and day <= 22:
    print('Скорпион')
if month == 'ноябрь' and day >= 23 or month == 'декабрь' and day <= 22:
    print('Стрелец')
if month == 'декабрь' and day >= 23 or month == 'январь' and day <= 20:
    print('Козерог')
if month == 'январь' and day >= 21 or month == 'февраль' and day <= 19:
    print('Водолей')
if month == 'февраль' and day >= 20 or month == 'март' and day <= 20:
    print('Рыба')