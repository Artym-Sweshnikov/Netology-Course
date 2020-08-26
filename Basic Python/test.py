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
    for dish in dishes:
        if dish in cook_book:
            recipe = cook_book[dish]
            for dict_of_recipe in recipe:
                amount_of_product = (dict_of_recipe['quantity'] * person_count)
                dict_of_dish = dict(dish=dish, dict_of_recipe=dict_of_recipe)
                new_dict = dict.fromkeys([dish], dict(measure=dict_of_recipe['measure'], quantity=dict_of_recipe['quantity']))
                if dish in dict_of_dish['dish']:
                    new_dict[dish]['quantity'] = amount_of_product
                    print(new_dict)
                else:
                    new_dict[dish]['quantity'] += dict_of_recipe['quantity']
                    print(new_dict)


get_shop_list_by_dishes(['Омлет','Запеченный картофель'], 3)
