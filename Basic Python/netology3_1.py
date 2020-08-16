boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys_rang = sorted(boys)
girls_rang = sorted(girls)
if len(boys) != len(girls):
    print('Внимание! Кто-то может остаться без пары')
else:
    for guis, woman in zip(boys_rang, girls_rang):
        print(guis,'и', woman)