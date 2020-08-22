def create_dict_from_file(file_name):
    cook_dict = {}
    with open(file_name, encoding='utf8') as file_work:
        for line in file_work:
            dish_name = line.strip()
            counter = int(file_work.readline())
            list_of_ingredient = []
            for i in range(counter):
                set_of_product = file_work.readline().split('|')
                temp_dict = dict(zip(['ingredient_name', 'quantity', 'measure'], set_of_product))
                list_of_ingredient.append(temp_dict)
            cook_dict[dish_name] = list_of_ingredient
            file_work.readline()
    return cook_dict


create_dict_from_file("recipes.txt")
