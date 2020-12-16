import numpy as np

def process_file_input(provided_train_tickets, ticket_class, ticket_class_lower_limit, ticket_class_upper_limit, nearby_tickets):
    for j in range(0, provided_train_tickets.index("")):
        rule, limits = provided_train_tickets[j].split(": ")
        ticket_class.append(rule)
        ticket_class_lower_limit.append(limits.split(' or ')[0])
        ticket_class_upper_limit.append(limits.split(' or ')[1])

    for j in range(provided_train_tickets.index("nearby tickets:") + 1, len(provided_train_tickets)):
            nearby_tickets.append(provided_train_tickets[j].split(','))

def find_invalid_numbers(ticket_class_lower_limit, ticket_class_upper_limit, nearby_tickets, invalid_numbers):
    for each_ticket in nearby_tickets:
        for each_number in each_ticket:
            if number_is_in_list_range(ticket_class_lower_limit, ticket_class_upper_limit, each_number) == False:
                invalid_numbers.append(each_number)
                break

def number_is_in_list_range(ticket_class_lower_limit, ticket_class_upper_limit, number):
    number_in_range = False

    for i in range(0, len(ticket_class_lower_limit)):
        number_in_range = number_is_in_range(ticket_class_lower_limit[i], ticket_class_upper_limit[i], number)
        if number_in_range:
            break

    return number_in_range

def number_is_in_range(ticket_class_lower_limit, ticket_class_upper_limit, number):
    number_in_range = False

    if int(ticket_class_lower_limit.split('-')[0]) <= int(number) <= int(ticket_class_lower_limit.split('-')[1]):
        number_in_range = True
    if int(ticket_class_upper_limit.split('-')[0]) <= int(number) <= int(ticket_class_upper_limit.split('-')[1]):
        number_in_range = True

    return number_in_range 

def get_ticket_error_rate(provided_train_tickets):
    error_rate = 0
    ticket_class, nearby_tickets, invalid_numbers  = [], [], []
    ticket_class_lower_limit, ticket_class_upper_limit = [], []

    process_file_input(provided_train_tickets, ticket_class, ticket_class_lower_limit, ticket_class_upper_limit, nearby_tickets)
    find_invalid_numbers(ticket_class_lower_limit, ticket_class_upper_limit, nearby_tickets, invalid_numbers)
    for each_invalid_number in invalid_numbers:
        error_rate = error_rate + int(each_invalid_number)

    return error_rate

def get_product_classes_with_keyword(provided_train_tickets, keyword):
    product_classes_departure = 1
    ticket_class, nearby_tickets, invalid_numbers = [], [], []
    ticket_class_lower_limit, ticket_class_upper_limit = [], []
    valid_nearby_ticket, possible_classes = [], []

    my_ticket = provided_train_tickets[provided_train_tickets.index("your ticket:") + 1].split(",")
    process_file_input(provided_train_tickets, ticket_class, ticket_class_lower_limit, ticket_class_upper_limit, nearby_tickets)
    find_invalid_numbers(ticket_class_lower_limit, ticket_class_upper_limit, nearby_tickets, invalid_numbers)

    for each_ticket in nearby_tickets:
        if not any(number in invalid_numbers for number in each_ticket):
            valid_nearby_ticket.append(each_ticket)

    for i in range(0, len(ticket_class)):
        possible_classes.append([])
        possible_classes[-1].extend(ticket_class)

    for each_ticket in valid_nearby_ticket:
        for j in range(0, len(each_ticket)):
            for i in range(0, len(ticket_class)):
                if number_is_in_range(ticket_class_lower_limit[i], ticket_class_upper_limit[i], each_ticket[j]) == False:
                    if ticket_class[i] in possible_classes[j]:
                        possible_classes[j].remove(ticket_class[i])

    amount_unique_specifed_classes = 0
    while amount_unique_specifed_classes < len(possible_classes):
        amount_unique_specifed_classes = 0
        for j in range(0, len(possible_classes)):
            if len(possible_classes[j]) == 1:
                amount_unique_specifed_classes = amount_unique_specifed_classes + 1
                for i in range(0, len(possible_classes)):
                    if possible_classes[j][0] in possible_classes[i] and len(possible_classes[i]) > 1:
                        possible_classes[i].remove(possible_classes[j][0])

    for j in range(0, len(my_ticket)):
        if keyword in possible_classes[j][0]:
            product_classes_departure = product_classes_departure * int(my_ticket[j])

    return product_classes_departure

if __name__ == "__main__":

    train_tickets = []
    with open("Day_16//Data.txt") as data_file:
        for line in data_file:
            train_tickets.append(line.strip())
    
    test_train_tickets = []
    with open("Day_16//Test.txt") as data_file:
        for line in data_file:
            test_train_tickets.append(line.strip())

    test_train_tickets_error_rate = 71
    keyword = "departure"
    
    if get_ticket_error_rate(test_train_tickets) == test_train_tickets_error_rate:
        print("Solution Part One: " + str(get_ticket_error_rate(train_tickets)))
    else:
        print("Implementation Part One Wrong")

    print("Solution Part Two: " + str(get_product_classes_with_keyword(train_tickets, keyword)))
