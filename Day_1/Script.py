import pandas as pd
import numpy as np

def multiply_two_summands(numbers_array, sum):
    for number in numbers_array:
        if sum - number in numbers_array:
            solution = number * (sum - number)
    return solution

def multiply_three_summands(numbers_array, sum):
    for first_number in numbers_array:
        for second_number in numbers_array:
            if sum - first_number - second_number in numbers_array:
                third_number = sum - second_number - first_number
                solution = first_number * second_number * third_number
    return solution

if __name__ == "__main__":

    data = pd.read_csv("Data.txt", header=None, names=['Numbers']) 
    numbers_array = data.Numbers.to_numpy()

    test_numbers_array = np.array([1721, 979, 366, 299, 675, 1456])
    test_result_two_summands = 514579
    test_result_three_summands = 241861950

    sum = 2020

    if multiply_two_summands(test_numbers_array, sum) == test_result_two_summands:
        print("Solution Part One: " + str(multiply_two_summands(numbers_array, sum)))
    else:
        print("Implementation Part One Wrong")

    if multiply_three_summands(test_numbers_array, sum) == test_result_three_summands:
        print("Solution Part Two: " + str(multiply_three_summands(numbers_array, sum)))
    else:
        print("Implementation Part Two Wrong")
