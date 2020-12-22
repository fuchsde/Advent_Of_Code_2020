import numpy as np

def identify_machting_food(allergenes, ingredients, food_dictionary):
    unique_allergenes = []

    for each_allergen in allergenes:
        unique_allergenes.extend(each_allergen)

    unique_allergenes = list(set(unique_allergenes))

    while len(food_dictionary) < len(unique_allergenes):
        for each_unique_allergen in unique_allergenes:
            each_allergen_counter, found_matches = 0, 0
            ingredients_with_allergen = []

            for k in range(0, len(allergenes)):
                if each_unique_allergen in allergenes[k]:
                    each_allergen_counter = each_allergen_counter + 1
                    ingredients_with_allergen.extend(ingredients[k])

            for each_ingredients in food_dictionary:
                while each_ingredients in ingredients_with_allergen:
                    ingredients_with_allergen.remove(each_ingredients)

            for each_ingredients in ingredients_with_allergen:
                if ingredients_with_allergen.count(each_ingredients) == each_allergen_counter:
                    found_matches = found_matches + 1

            if found_matches == each_allergen_counter:
                for each_ingredients in ingredients_with_allergen:
                    if ingredients_with_allergen.count(each_ingredients) == each_allergen_counter:
                        food_dictionary[each_ingredients] = each_unique_allergen 

def get_sum_food_without_allergendes(food_list):
    sum_food_without_allergenes = 0
    food_dictionary = {}
    ingredients, allergenes = [], []
    
    for each_food in food_list:
        ingredients.append(each_food.split(" (contains ")[0].split(" "))
        allergenes.append(each_food.split(" (contains ")[1].replace(")", "").split(", "))

    identify_machting_food(allergenes, ingredients, food_dictionary)

    for each_food in ingredients:
        for each_ingredient in each_food:#
            if not each_ingredient in food_dictionary:
                sum_food_without_allergenes = sum_food_without_allergenes + 1
    
    return sum_food_without_allergenes

def get_canonical_dangerous_ingredient(food_list):
    food_dictionary = {}
    ingredients, allergenes, list_allergenes_sorted = [], [], []
    canonical_dangerous_ingredient_sorted = ""
    
    for each_food in food_list:
        ingredients.append(each_food.split(" (contains ")[0].split(" "))
        allergenes.append(each_food.split(" (contains ")[1].replace(")", "").split(", "))

    identify_machting_food(allergenes, ingredients, food_dictionary)

    for each_food in food_dictionary:
        list_allergenes_sorted.append(food_dictionary[each_food])

    list_allergenes_sorted = sorted(list_allergenes_sorted)

    for each_sorted_allergen in list_allergenes_sorted:
        for each_food in food_dictionary:
            if food_dictionary[each_food] == each_sorted_allergen:
                canonical_dangerous_ingredient_sorted += each_food + "," 
    
    return canonical_dangerous_ingredient_sorted[0:-1]

if __name__ == "__main__":

    food_list = []
    with open("Day_21//Data.txt") as data_file:
        for line in data_file:
            food_list.append(line.strip())
    
    test_food_list = []
    with open("Day_21//Test.txt") as data_file:
        for line in data_file:
            test_food_list.append(line.strip())

    test_sum_food_without_allergenes = 5 
    test_canonical_dangerous_ingredient = "mxmxvkd,sqjhc,fvjkl" 
    
    if get_sum_food_without_allergendes(test_food_list) == test_sum_food_without_allergenes:
        print("Solution Part One: " + str(get_sum_food_without_allergendes(food_list)))
    else:
        print("Implementation Part One Wrong")

    if get_canonical_dangerous_ingredient(test_food_list) == test_canonical_dangerous_ingredient:
        print("Solution Part Two: " + str(get_canonical_dangerous_ingredient(food_list)))
    else:
        print("Implementation Part Two Wrong")
        