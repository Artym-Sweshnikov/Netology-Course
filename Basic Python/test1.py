def create_dict_from_file(file_name):
    cook_dict = {}
    with open(file_name, encoding='utf8') as file_work:
        for line in file_work:
            dish_name = line.strip()
            counter = int(file_work.readline())
            list_of_ingredient = []
            for i in range(counter):
                temp_dict = {file_work.readline()}
                x = {'ingredient': temp_dict}
                list_of_ingredient.append(x)
            cook_dict[dish_name] = list_of_ingredient
            file_work.readline()
    print(cook_dict)
    return cook_dict


create_dict_from_file("recipes.txt")
