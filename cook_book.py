import os 

file_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_directory, "recipes.txt")

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

for key, values in cook_book.items():
    print(f"{key}:")
    for val in values:
        print(f"{val}")
