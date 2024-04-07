def read_cook_book(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(f.readline())
            ingredients_list = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            f.readline()
            cook_book[dish_name] = ingredients_list
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


def count_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return len(f.readlines())

def sort_files_by_line_count(file_names):
    return sorted(file_names, key=count_lines)

def merge_files(sorted_file_names, result_file_name):
    with open(result_file_name, 'w', encoding='utf-8') as result_file:
        for file_name in sorted_file_names:
            line_count = count_lines(file_name)
            result_file.write(f'{file_name}\n{line_count}\n')
            with open(file_name, 'r', encoding='utf-8') as f:
                result_file.write(f.read() + '\n')

file_names = ['1.txt', '2.txt']
sorted_file_names = sort_files_by_line_count(file_names)
merge_files(sorted_file_names, 'result.txt')