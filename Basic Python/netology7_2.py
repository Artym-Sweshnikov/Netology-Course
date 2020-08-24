import netology7_1


def get_shop_list_by_dishes(dishes, person_count):
    '''Функция состовляет список продуктов, необходимых для приготовления блюда.

    Пользователь выбирает блюда и передает количество человек в аргумент функции.'''
    cook_book = netology7_1.create_dict_from_file("recipes.txt")
    list_of_ingredients = []
    list_of_quantity = []
    list_of_last_quantity = []
    list_measure = []

    if len(dishes) == len(set(dishes)):
        for product_of_dish in dishes:
            print(product_of_dish)
            our_list = cook_book[product_of_dish]
            for key in our_list:
                list_of_ingredients.append(key['ingredient_name'])
                list_of_quantity.append(key['quantity'])
                list_measure.append(key['measure'])
            for amount_of_person in list_of_quantity:
                list_of_last_quantity.append(int(amount_of_person) * person_count)
        for ingredients, measure, quantity in zip(list_of_ingredients, list_measure, list_of_last_quantity):
            dict_of_necessary_ingredients = dict.fromkeys([ingredients], dict(measure=measure, quantity=quantity))
            print(dict_of_necessary_ingredients)
    else:
        our_list = cook_book[dishes[0]]
        for key in our_list:
            list_of_ingredients.append(key['ingredient_name'])
            list_of_quantity.append(key['quantity'])
            list_measure.append(key['measure'])
        for amount_of_person in list_of_quantity:
            list_of_last_quantity.append(int(amount_of_person) * person_count * len(dishes))
        for ingredients, measure, quantity in zip(list_of_ingredients, list_measure, list_of_last_quantity):
            dict_of_necessary_ingredients = dict.fromkeys([ingredients], dict(measure=measure, quantity=quantity))
            print(dict_of_necessary_ingredients)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
