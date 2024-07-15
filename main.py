from pprint import pprint

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
