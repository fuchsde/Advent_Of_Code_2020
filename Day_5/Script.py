import pandas as pd
import numpy as np

def decode_seats(seats_coded):
    seats_decoded = np.zeros(len(seats_coded))
    for i in range(0, len(seats_coded)):
        seat_binary_code = seats_coded[i][0].replace('F', '0') 
        seat_binary_code = seat_binary_code.replace('B', '1')
        seat_binary_code = seat_binary_code.replace('L', '0')
        seat_binary_code = seat_binary_code.replace('R', '1')
        seats_decoded[i] = int(seat_binary_code[0:7], 2) * 8 + int(seat_binary_code[7:10], 2)
    return seats_decoded

def find_highest_occupied_seat_id(seats_coded):
    return np.max(decode_seats(seats_coded)).astype(int)

def find_free_seat_id(seats_coded):
    seats_decoded = decode_seats(seats_coded)
    free_seat = 0
    for i in range(1, len(seats_decoded) -1):
        if not i in seats_decoded:
            if (i - 1) in seats_decoded and (i + 1) in seats_decoded:
                free_seat = i
    return free_seat

if __name__ == "__main__":

    data = pd.read_csv("Day_5//Data.txt", header=None) 
    seats_coded = data.values.tolist()

    data = pd.read_csv("Day_5//Test_Part_One.txt", header=None) 
    test_seats_coded = data.values.tolist()

    test_result_decoding = np.array([567, 119, 820])
    test_result_highest_id = 820

    if (decode_seats(test_seats_coded) == test_result_decoding).all():
        print("Seat ID Decoding works")
    else:
        print("Seat ID Decoding does not work")

    if find_highest_occupied_seat_id(test_seats_coded) == test_result_highest_id:
        print("Solution Part One: " + str(find_highest_occupied_seat_id(seats_coded)))
    else:
        print("Implementation Part One Wrong")

    # No test data provided
    print("Solution Part Two: " + str(find_free_seat_id(seats_coded)))
        
