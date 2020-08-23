import netology7_1

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = netology7_1.create_dict_from_file("recipes.txt")
    # amount_product = cook_book['quantiy'] * person_count
    list_of_ingredients = []
    list_of_quantity = []
    list_of_last_quantity = []
    list_measure = []

    for product_of_dish in dishes:
        our_list = cook_book
        print(our_list)
        for values in our_list.values():
            print(values)



get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 4)