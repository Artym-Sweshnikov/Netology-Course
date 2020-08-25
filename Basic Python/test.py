cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


def get_shop_list_by_dishes(dishes, person_count):
    '''Функция состовляет список продуктов, необходимых для приготовления блюда.

    Пользователь выбирает блюда и передает количество человек в аргумент функции.'''
    new_dict = {}
    list_of_ingredients = []
    list_of_quantity = []
    list_of_last_quantity = []
    list_measure = []
    for dish in dishes:
        if dish in cook_book:
            recipe = cook_book[dish]
            for j in recipe:
                list_of_ingredients.append(j['ingredient_name'])
                list_of_quantity.append(j['quantity'])
                list_measure.append(j['measure'])
            for amount_of_person in list_of_quantity:
                list_of_last_quantity.append(int(amount_of_person) * person_count)
            for ingredients, measure, quantity in zip(list_of_ingredients, list_measure, list_of_last_quantity):
                dict_of_necessary_ingredients = dict.fromkeys([ingredients], dict(measure=measure, quantity=quantity))
                print(dict_of_necessary_ingredients)



get_shop_list_by_dishes(['Омлет','Омлет'], 1)
