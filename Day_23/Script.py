class cup():
    def __init__(self, id):
        self.id = id
        self.next = None

def move_cups(labeling, amount_moves, solving_function):
    current_cup, min_cup, max_cup = 0, min(labeling), max(labeling)

    cups_dictionary = dict()
    for number in labeling:
        cups_dictionary[number] = cup(number)

    for j in range(0, len(labeling) - 1):
        cups_dictionary[labeling[j]].next = cups_dictionary[labeling[j + 1]]

    cups_dictionary[labeling[-1]].next = cups_dictionary[labeling[0]]
    current_cup = cups_dictionary[labeling[0]]
     
    for _ in range(0, amount_moves):
        cups_picked_up = [current_cup.next.id, current_cup.next.next.id, current_cup.next.next.next.id]
        current_cup.next = current_cup.next.next.next.next

        cup_destination = current_cup.id - 1
        while cup_destination in cups_picked_up or cup_destination < min_cup: 
            if(cup_destination < min_cup):
                cup_destination = max_cup
            else:
                cup_destination = cup_destination - 1  

        cups_dictionary[cups_picked_up[2]].next = cups_dictionary[cup_destination].next
        cups_dictionary[cup_destination].next = cups_dictionary[cups_picked_up[0]]
        current_cup = current_cup.next

    return solving_function(cups_dictionary)

def solving_function_part_one(cups_dictionary):
    labeling_after_1, current_id = "", 1

    for _ in range(0, len(labeling) - 1):
        current_id = cups_dictionary[current_id].next.id
        labeling_after_1 = labeling_after_1 + str(current_id)

    return labeling_after_1

def solving_function_part_two(cups_dictionary):
    product_two_labels_after_1, current_id = 1, 1

    for _ in range(0, 2):
        current_id = cups_dictionary[current_id].next.id
        product_two_labels_after_1 = product_two_labels_after_1 * current_id

    return product_two_labels_after_1

if __name__ == "__main__":
    labeling = [1, 5, 6, 7, 9, 4, 8, 2, 3]
    test_labeling = [3, 8, 9, 1, 2, 5, 4, 6, 7]

    amount_moves_part_one = 100
    test_labeling_after_100_moves_after_nr_1 = "67384529"
    amount_moves_part_two = 10000000
    test_products_cups_hidden_stars = 149245887792

    if move_cups(test_labeling.copy(), amount_moves_part_one, solving_function_part_one) == test_labeling_after_100_moves_after_nr_1:
        print("Solution Part One: " + str(move_cups(labeling.copy(), amount_moves_part_one, solving_function_part_one)))
    else:
        print("Implementation Part One Wrong")

    for j in range(max(labeling) + 1, 1000001):
        labeling.append(j)
        test_labeling.append(j)

    if move_cups(test_labeling.copy(), amount_moves_part_two, solving_function_part_two) == test_products_cups_hidden_stars:
        print("Solution Part Two: " + str(move_cups(labeling.copy(), amount_moves_part_two, solving_function_part_two)))
    else:
        print("Implementation Part Two Wrong")
        