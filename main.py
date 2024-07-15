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


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
