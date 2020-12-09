import pandas as pd
import numpy as np

def find_first_irregular_number(number_stream, preamble_length):
    first_irregular_number = 0
    circular_buffer = np.zeros(preamble_length)

    for i in range(0, len(number_stream) - preamble_length):
        sum = int(number_stream[i + preamble_length][0])

        for j in range(0, preamble_length):
            circular_buffer[j] = int(number_stream[i+j][0])

        possible_sums = np.zeros(preamble_length * preamble_length)
        for j in range(0, preamble_length):
            for k in range(0, preamble_length):
                if not k == j:
                    possible_sums[j * preamble_length + k] = circular_buffer[j] + circular_buffer[k]

        if not sum in possible_sums:
            first_irregular_number = sum
            break

    return first_irregular_number

def find_encryption_weakness(number_stream, irregular_number):
    encryption_weakness = 0

    for i in range(2, len(number_stream)):
        circular_buffer = np.zeros(i)
        for j in range(0, len(number_stream) - i):

            for k in range(0, i):
                circular_buffer[k] = int(number_stream[j+k][0])

            if np.sum(circular_buffer) == irregular_number:
                encryption_weakness = int(np.min(circular_buffer) + np.max(circular_buffer))
                break

        if encryption_weakness > 0:
            break

    return encryption_weakness

if __name__ == "__main__":

    data = pd.read_csv("Day_9//Data.txt", header=None) 
    number_stream = data.values.tolist()

    data = pd.read_csv("Day_9//Test.txt", header=None) 
    test_number_stream = data.values.tolist()

    preamble_length = 25
    test_first_irregular_number = 127
    test_preamble_length = 5
    test_encryption_weakness = 62

    test_irregular_number = find_first_irregular_number(test_number_stream, test_preamble_length)
    if test_irregular_number == test_first_irregular_number:
        irregular_number = find_first_irregular_number(number_stream, preamble_length)
        print("Solution Part One: " + str(irregular_number))
    else:
        print("Implementation Part One Wrong")

    if find_encryption_weakness(test_number_stream, test_irregular_number) == test_encryption_weakness:
       print("Solution Part Two: " + str(find_encryption_weakness(number_stream, irregular_number)))
    else:
       print("Implementation Part Two Wrong")
        