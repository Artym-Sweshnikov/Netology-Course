import netology7_1


def get_shop_list_by_dishes(dishes, person_count):
    '''Функция состовляет список продуктов, необходимых для приготовления блюда.

    Пользователь выбирает блюда и передает количество человек в аргумент функции.'''
    cook_book = netology7_1.create_dict_from_file("recipes.txt")
    new_dict = {}
    for dish in dishes:
        if dish not in cook_book:
            continue
        for ingredient in cook_book[dish]:
            curr_ingredient = ingredient.copy()
            curr_ingredient['quantity'] = int(curr_ingredient['quantity'])
            curr_ingredient['quantity'] *= person_count
            if curr_ingredient['ingredient_name'] in new_dict:
                new_dict[curr_ingredient['ingredient_name']]['quantity'] += curr_ingredient['quantity']
            else:
                new_dict[curr_ingredient.pop('ingredient_name')] = curr_ingredient

    print(new_dict)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
