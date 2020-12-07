import numpy as np

def find_amount_possible_containers(bag_type, bag_rules, bag_rules_splitword):
    containers = []
    containers.append(bag_type)

    for each_container in containers:
        for each_bag_rule in bag_rules:
            if len(each_bag_rule) > 1:
                bag, rule = each_bag_rule.split(bag_rules_splitword)
                if each_container in rule and not bag.strip() in containers: 
                        containers.append(bag.strip())

    return len(containers) - 1

def convert_list_to_dictionary(bag_rules, bag_rules_splitword):
    bag_rules_dictionary = {}
    for each_bag_rule in bag_rules:
        if len(each_bag_rule) > 1:
            bag, rule = each_bag_rule.split(bag_rules_splitword)
            bag_rules_dictionary[bag.strip()] = []
            for each_rule in rule.replace(".", "").replace("bags", "").replace("bag", "").split(','):
                amount, colour = "", ""
                if not "no other" in each_rule:
                    for each_string in each_rule:
                        if each_string.isdigit():
                            amount = amount + each_string
                        else:
                            colour = colour + each_string
                    bag_rules_dictionary[bag.strip()].append({"colour": colour.strip() , "amount" : int(amount.strip())})
    return bag_rules_dictionary

def count_countainers_recursiv(bag_type, bag_rules_dictionary):
    total_amount_bags = 1
    for each_rule in bag_rules_dictionary[bag_type]:
        total_amount_bags = total_amount_bags + each_rule["amount"] * count_countainers_recursiv(each_rule["colour"], bag_rules_dictionary)
    return total_amount_bags

def find_total_amount_containers_needed(bag_type, bag_rules, bag_rules_splitword):
    bag_rules_dictionary = convert_list_to_dictionary(bag_rules, bag_rules_splitword)
    return count_countainers_recursiv(bag_type, bag_rules_dictionary) - 1

if __name__ == "__main__":

    with open("Day_7//Data.txt") as data_file:
        bag_rules = data_file.readlines()

    with open("Day_7//Test_Part_One.txt") as data_file:
        test_bag_rules_one = data_file.readlines()

    with open("Day_7//Test_Part_Two.txt") as data_file:
        test_bag_rules_two = data_file.readlines()

    bag_type = "shiny gold"
    bag_rules_splitword = "bags contain"
    test_result_one_for_bag_type = 4
    test_result_two_for_bag_type = 126

    if find_amount_possible_containers(bag_type, test_bag_rules_one, bag_rules_splitword) == test_result_one_for_bag_type:
        print("Solution Part One: " + str(find_amount_possible_containers(bag_type, bag_rules, bag_rules_splitword)))
    else:
        print("Implementation Part One Wrong")

    if find_total_amount_containers_needed(bag_type, test_bag_rules_two, bag_rules_splitword) == test_result_two_for_bag_type:
        print("Solution Part Two: " + str(find_total_amount_containers_needed(bag_type, bag_rules, bag_rules_splitword)))
    else:
        print("Implementation Part Two Wrong")
        