from pprint import pprint

def prepare_dict(file_name: str):
    result: dict = dict()

    with open("recipes.txt", 'r', encoding='utf-8') as file:
        for line in file:
            name_dishes = line.strip()
            record_quantity = int(file.readline())
            dish_list = []
            for dish in range(record_quantity):
                ingredient_name, quantity, measure = file.readline().split('|')
                dish_list.append(
                    {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure}
                )
            result[name_dishes] = dish_list
            file.readline()
    return result

cook_book = prepare_dict("recipes.txt")
# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr in (cook_book[dish]):
            itm_list = dict([(ingr['ingredient_name'], {'measure': ingr['measure'],
                                                        'quantity': int(ingr['quantity']) * person_count})])
            if shop_list.get(ingr['ingredient_name']):
                item = (int(shop_list[ingr['ingredient_name']]['quantity']) +
                              int(itm_list[ingr['ingredient_name']]['quantity']))
                shop_list[ingr['ingredient_name']]['quantity'] = item

            else:
                shop_list.update(itm_list)


    pprint(shop_list)

get_shop_list_by_dishes(['Фахитос', 'Запеченный картофель', 'Омлет'], 2)