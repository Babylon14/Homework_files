import os 

file_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_directory, "recipes.txt")

def get_cook_book():
    with open(file_path, "r", encoding="utf-8") as file:
        cook_book = {}
        for c in file.read().split("\n\n"):
            lines = c.strip().split("\n")

            headers = lines[0]
            ingredient_count = int(lines[1])
        
            ingredient_list = []
            for line in lines[2:]:
                ingredient_name, quantity, measure = line.split("|")

                ingredient_list.append({
                    "ingredient_name": ingredient_name.strip(),
                    "quantity": quantity.strip(),
                    "measure": measure.strip()
                })

            cook_book[headers] = ingredient_list

    return cook_book

#print(get_cook_book())


def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}

    for dish in dishes:
        if dish in get_cook_book():
            for ingredient in get_cook_book()[dish]:
                name = ingredient["ingredient_name"]
                quantity = int(ingredient["quantity"]) * person_count
                measure = ingredient["measure"]

                if name in shop_dict:
                    shop_dict[name]["quantity"] += quantity
                else:
                    shop_dict[name] = {"measure": measure, "quantity": quantity}

    for key, values in shop_dict.items():
        print(key, values)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
