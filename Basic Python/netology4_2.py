ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
a = ids.values()
# Создаем общий список для переменных
common_ids_list = []
for values in a:
    for j in values:
        common_ids_list.append(j)
# Находим уникальные значения
unique_values_list = list(set(common_ids_list))
print(unique_values_list)
