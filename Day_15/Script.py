def get_number_to_find(given_starting_numbers, place_of_number_to_be_found):
    next_number, current_number, index = 0, 0, 0
    starting_number_last_pos, starting_number_second_last_pos = {}, {}

    for number in given_starting_numbers[0].split(','):
        current_number = int(number)
        index = index + 1

        if current_number in starting_number_last_pos:
            starting_number_second_last_pos[current_number] = starting_number_last_pos[current_number]
            
        starting_number_last_pos[current_number] = index
 
    while index < place_of_number_to_be_found:
        index = index + 1
        next_number = 0

        if current_number in starting_number_second_last_pos:
            next_number = starting_number_last_pos[current_number] - starting_number_second_last_pos[current_number]

        if next_number in starting_number_last_pos:
            starting_number_second_last_pos[next_number] = starting_number_last_pos[next_number]
            
        starting_number_last_pos[next_number] = index
        current_number = next_number
           
    return next_number

if __name__ == "__main__":

    starting_numbers = []
    with open("Day_15//Data.txt") as data_file:
        for line in data_file:
            starting_numbers.append(line.strip())
    
    test_starting_numbers = []
    with open("Day_15//Test.txt") as data_file:
        for line in data_file:
            test_starting_numbers.append(line.strip())

    test_2020th_number = 436
    test_30000000th_number = 175594
    
    if get_number_to_find(test_starting_numbers, 2020) == test_2020th_number:
        print("Solution Part One: " + str(get_number_to_find(starting_numbers, 2020)))
    else:
        print("Implementation Part One Wrong")

    if get_number_to_find(test_starting_numbers, 30000000) == test_30000000th_number:
        print("Solution Part Two: " + str(get_number_to_find(starting_numbers, 30000000)))
    else:
        print("Implementation Part Two Wrong")
        