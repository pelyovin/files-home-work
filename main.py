# Задача 1
def open_cook_book(recipes):
    """Функция принимает файл с рецептами и формирует из него словарь, где ключи - названия блюд, а
    значениями является словарь с необходимыми продуктами, их количеством и мерой."""
    cook_book = {}
    with open(recipes) as f:
        for i in f:
            dish_name = i.strip()
            ingredients_count = f.readline()
            ingredients = []
            for j in range(int(ingredients_count)):
                name, quantity, measure = f.readline().strip().split(' | ')
                ingredients.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
            f.readline()
            cook_book[dish_name] = ingredients
    return cook_book


# Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    """Функция, принимает на вход список блюд из cook_book и количество персон для кого мы будем готовить
    и возвращает словарь с названием ингредиентов и его количества для блюда"""
    result = {}
    for dish in dishes:
        for ingredient in open_cook_book('recipes.txt')[dish]:
            if ingredient['ingredient_name'] not in result:
                result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                         'quantity': ingredient['quantity'] * person_count}
            else:
                result[ingredient['ingredient_name']]['quantity'] *= 2
    return result


# Задача 3
def sorted_files(path):
    """Функция формирует один новый файл, где содержимое файлов сортируется
    по количеству строк от меньшего к большему"""
    import os
    dict_of_files = {}
    for file in os.listdir(path):
        with open(path + file) as f:
            if file.endswith('.txt'):
                count = len(f.readlines())
                f.seek(0)
                dict_of_files[count] = [file, f.read()]
    with open(path + 'sorted_file.txt', 'a') as f:
        for k, v in sorted(dict_of_files.items()):
            f.write(f'{v[0]}\n{k}\n{v[1]}\n')


sorted_files('/Users/alex/netology/files-home-work/sorted/')
