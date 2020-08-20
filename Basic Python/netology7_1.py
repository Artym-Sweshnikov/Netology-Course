file = open("recipes.txt")
onstring = file.read().split("\n")[:-1]

omelet = onstring[0]  # Омлет
three_omlets = onstring[1]  # 3
egg = onstring[2][0:4]  # Яйцо
egg_amount = onstring[2][7]  # 2
egg_unit = onstring[2][11:13]  # шт
milk = onstring[3][0:7]  # Молоко
milk_amount = onstring[3][9:13]  # 100
milk_unit = onstring[3][15:18]  # мл
tomato = onstring[4][0:7]  # Помидор
tomato_amount = onstring[4][10]  # 2
tomato_unit = onstring[4][14:17]  # шт
peking_duck = onstring[6]  # Утка по-пекински
four_peking_duck = onstring[7]  # 4
duck = onstring[8][0:4]  # Утка
duck_amount = onstring[8][7]  # 1
duck_unit = onstring[8][11:13]  # шт
water = onstring[9][0:4]  # Вода
water_amount = onstring[9][7]  # 2
water_unit = onstring[9][11]  # л
honey = onstring[10][0:3]  # Мед
honey_amount = onstring[10][6]  # 3
honey_unit = onstring[10][10:14]  # ст.л
soy_sauce = onstring[11][0:11]  # Соевый соус
soy_sauce_amount = onstring[11][14:16]  # 60
soy_sauce_unit = onstring[11][19:21]  # мл
baked_potato = onstring[13]  # Запеченный картофель
three_backed_potato = onstring[14]  # 3
potato = onstring[15][0:9]  # Картофель
potato_amount = onstring[15][12]  # 1
potato_unit = onstring[15][16:18]  # кг
garlic = onstring[16][0:6]  # Чеснок
garlic_amount = onstring[16][9]  # 3
garlic_unit = onstring[16][13:17]  # зубч
gouda_cheese = onstring[17][0:9]  # Сыр гауда
gouda_cheese_amount = onstring[17][12:16]  # 100
gouda_cheese_unit = onstring[17][18]  # гр
fajitos = onstring[19]  # Фахитос
five_fajitos = onstring[20]  # 5
beef = onstring[21][0:8]  # Говядина
beef_amount = onstring[21][11:14]  # 500
beef_unit = onstring[21][17]  # г
sweet_pepper = onstring[22][0:13]  # Перец сладкий
sweet_pepper_amount = onstring[22][16]  # 1
sweet_pepper_unit = onstring[22][20:22]  # шт
pita = onstring[23][0:5]  # Лаваш
pita_amount = onstring[23][8]  # 2
pita_unit = onstring[23][12:14]  # шт
wine_vinegar = onstring[24][0:12]  # Винный уксус
wine_vinegar_amount = onstring[24][15]  # 1
wine_vinegar_unit = onstring[24][19:23]  # ст.л

cook_book = {
    omelet: [
        {'ingredient_name': egg, 'quantity': egg_amount, 'measure': egg_unit},
        {'ingredient_name': milk, 'quantity': milk_amount, 'measure': milk_unit},
        {'ingredient_name': tomato, 'quantity': tomato_amount, 'measure': tomato_unit}
    ],
    peking_duck: [
        {'ingredient_name': duck, 'quantity': duck_amount, 'measure': duck_unit},
        {'ingredient_name': water, 'quantity': water_amount, 'measure': water_unit},
        {'ingredient_name': honey, 'quantity': honey_amount, 'measure': honey_unit},
        {'ingredient_name': soy_sauce, 'quantity': soy_sauce_amount, 'measure': sweet_pepper_unit}
    ],
    baked_potato: [
        {'ingredient_name': potato, 'quantity': pita_amount, 'measure': potato_unit},
        {'ingredient_name': garlic, 'quantity': garlic_amount, 'measure': garlic_unit},
        {'ingredient_name': gouda_cheese, 'quantity': gouda_cheese_amount, 'measure': gouda_cheese_unit},
    ]
}
print(cook_book)

file.close()
