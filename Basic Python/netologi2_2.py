age = int(input('Введите ваш возраст: '))
height = int(input('Введите ваш рост: '))
weight = int(input('Введите ваш вес: '))
children = int(input('Введите количество детей: '))
education = input('Вы сейчас учитесь: ')
print('')

if age >= 30 or children >= 2:
    print('Ты навсегда освобожден от службы.')
elif education == 'да':
    print('К счастью для тебя, мы дадим тебе отсрочку,' +
          ' чтобы ты закончил учиться. Не дай бог отчислят!.')
if age <= 29 and height >= 160 and weight >= 65 and education != 'да' and children < 2:
    print('Поздравляю! Вы являетесь призывником и вас ждет ' +
          'год веселья.')
    if height <= 170 and weight <= 70:
        print('Вы попали в ВМФ')
    elif height <= 180 and weight <= 80:
        print('Вы годны к службе в ВДВ')
    elif height <= 190 and weight <= 100:
        print('Скорей всего ты попадешь в РВСН')
    elif height > 160 and weight > 100:
        print('С такими параметрами тебе только в ВКС')
