# Задача 1
with open('recipes.txt') as f:
    cook_book = {}
    for i in f:
        dish_name = i.strip()
        ingredients_count = f.readline()
        ingredients = []
        for j in range(int(ingredients_count)):
            name, quantity, measure = f.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
        f.readline()
        cook_book[dish_name] = ingredients


# Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    """Функция, принимает на вход список блюд из cook_book и количество персон для кого мы будем готовить
    и возвращает словарь с названием ингредиентов и его количества для блюда"""
    result = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in result:
                result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                         'quantity': ingredient['quantity'] * person_count}
            else:
                result[ingredient['ingredient_name']]['quantity'] *= 2
    return result


# Задача 3
with open('sorted/1.txt') as f1, open('sorted/2.txt') as f2, open('sorted/3.txt') as f3:
    nums_of_lines = len(f1.readlines()), len(f2.readlines()), len(f3.readlines())

with open('sorted/1.txt') as f1, open('sorted/2.txt') as f2, open('sorted/3.txt') as f3:
    dict_of_files = {}
    dict_of_files[nums_of_lines[0]] = f'1.txt\n{nums_of_lines[0]}\n{f1.read()}'
    dict_of_files[nums_of_lines[1]] = f'2.txt\n{nums_of_lines[1]}\n{f2.read()}'
    dict_of_files[nums_of_lines[2]] = f'3.txt\n{nums_of_lines[2]}\n{f3.read()}'
    sorted_dict = {}
    for key, value in sorted(dict_of_files.items()):
        sorted_dict[key] = value

with open('sorted/sorted-file.txt', 'a') as f:
    for k, v in sorted_dict.items():
        f.write(v + '\n')
