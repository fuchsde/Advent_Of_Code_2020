import numpy as np

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."
DELTAS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def count_adjacent_occupied_seats(seat_map, seat_row, seat_column):
    amount_adjacent_occupied_seats = 0
    
    for i,j in DELTAS:
        current_seat_row = seat_row + i
        current_seat_column =  seat_column + j
        if 0 <= current_seat_row < len(seat_map) and 0 <= current_seat_column < len(seat_map[current_seat_row]):
            if seat_map[current_seat_row][current_seat_column] == OCCUPIED:
                amount_adjacent_occupied_seats = amount_adjacent_occupied_seats + 1

    return amount_adjacent_occupied_seats

def count_visible_occupied_seats(seat_map, seat_row, seat_column):
    amount_visible_occupied_seats = 0

    for i,j in DELTAS:
        current_seat_row = seat_row + i
        current_seat_column =  seat_column + j

        while 0 <= current_seat_row < len(seat_map) and 0 <= current_seat_column < len(seat_map[current_seat_row]):
            if seat_map[current_seat_row][current_seat_column] == OCCUPIED:
                amount_visible_occupied_seats = amount_visible_occupied_seats + 1
                break
            elif seat_map[current_seat_row][current_seat_column] == EMPTY:
                break
            current_seat_row = current_seat_row + i
            current_seat_column = current_seat_column + j

    return amount_visible_occupied_seats

def find_occupied_seats(seat_map, tolerance_sit_down, tolerance_stand_up, adjacent_seats_only):
    total_amount_occupied_seats = 0
    amount_occupied_seats = 0
    new_seat_map = seat_map.copy()
    old_seat_map = []

    while not new_seat_map == old_seat_map:
        old_seat_map = new_seat_map.copy()
        new_seat_map = [''] * len(old_seat_map)
        for j in range(0, len(seat_map)):
            for i in range(0, len(seat_map[j])):

                if adjacent_seats_only == True and not old_seat_map[j][i] == FLOOR:
                    amount_occupied_seats = count_adjacent_occupied_seats(old_seat_map, j, i)
                elif adjacent_seats_only == False and not old_seat_map[j][i] == FLOOR:
                    amount_occupied_seats = count_visible_occupied_seats(old_seat_map, j, i)

                if old_seat_map[j][i] == EMPTY and amount_occupied_seats == tolerance_sit_down:
                    new_seat_map[j] = new_seat_map[j] + OCCUPIED
                elif old_seat_map[j][i] == OCCUPIED and amount_occupied_seats >= tolerance_stand_up:
                    new_seat_map[j] = new_seat_map[j] + EMPTY
                else:
                    new_seat_map[j] = new_seat_map[j] + old_seat_map[j][i]

    for row in new_seat_map:
        total_amount_occupied_seats = total_amount_occupied_seats + row.count(OCCUPIED) 

    return total_amount_occupied_seats

if __name__ == "__main__":

    seat_map = []
    with open("Day_11//Data.txt") as data_file:
        for line in data_file:
            seat_map.append(line.strip())
    
    test_seat_map = []
    with open("Day_11//Test.txt") as data_file:
        for line in data_file:
            test_seat_map.append(line.strip())

    limit_sitting_down = 0
    first_limit_standing_up = 4
    first_only_adjacant = True
    second_limit_standing_up = 5
    second_only_adjacant = False
    test_amount_occupied_seats = 37
    test_amount_occupied_seats_extend = 26

    solution = find_occupied_seats(test_seat_map, limit_sitting_down, first_limit_standing_up, first_only_adjacant)
    if solution == test_amount_occupied_seats:
        solution = find_occupied_seats(seat_map, limit_sitting_down, first_limit_standing_up, first_only_adjacant)
        print("Solution Part One: " + str(solution))
    else:
        print("Implementation Part One Wrong")

    solution = find_occupied_seats(test_seat_map, limit_sitting_down, second_limit_standing_up, second_only_adjacant)
    if  solution == test_amount_occupied_seats_extend:
        solution = find_occupied_seats(seat_map, limit_sitting_down, second_limit_standing_up, second_only_adjacant)
        print("Solution Part Two: " + str(solution))
    else:
        print("Implementation Part Two Wrong")
        