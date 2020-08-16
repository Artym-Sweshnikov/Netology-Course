queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]


def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1


lst = []
dct = {}
data = len(list(queries))

for teg in queries:
    amount_of_word = len(teg.split())
    lst.append(amount_of_word)

analysis(lst, dct)

print('Поисковые запросы из:', end=' ')
for item in sorted(dct):
    value = int(dct[item])
    percentage_value = round((value / data) * 100)
    print(f'{item} слов - {percentage_value}%', end=', ')
