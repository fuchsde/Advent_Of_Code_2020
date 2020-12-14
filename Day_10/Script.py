import pandas as pd
import numpy as np

def append_edge_cases_and_sort(available_adapters):
    available_adapters = np.append(available_adapters, 0)
    available_adapters = np.append(available_adapters, np.max(available_adapters) + 3)
    return np.sort(available_adapters, 0)

def find_difference_prodcut_longest_chain(available_adapters):
    differences = np.zeros(4)
    available_adapters_sorted = append_edge_cases_and_sort(available_adapters)

    for i in range(0, len(available_adapters_sorted) - 1):
        difference = available_adapters_sorted[i + 1] - available_adapters_sorted[i]
        differences[difference] = differences[difference] + 1

    return int(differences[1] * differences[3])

def find_amount_possible_arrangements(available_adapters):
    amount_arrangements = 1
    dict_amount_arrangements = {}
    consecutive_difference_one = np.zeros(1)
    available_adapters_sorted = append_edge_cases_and_sort(available_adapters)

    for i in range(0, len(available_adapters_sorted) - 1):
        if available_adapters_sorted[i + 1] - available_adapters_sorted[i] == 1:
            consecutive_difference_one[len(consecutive_difference_one) - 1] += 1
        else:
            if not consecutive_difference_one[len(consecutive_difference_one) - 1] == 0:
                consecutive_difference_one[len(consecutive_difference_one) - 1] -= 1 
                consecutive_difference_one = np.append(consecutive_difference_one, 0)

    consecutive_difference_one[consecutive_difference_one < 1] = 0
    unique_differences = np.unique(consecutive_difference_one).astype(int)

    for i in range(0, len(unique_differences)):
        counter = 0 
        for j in range(0, (2**unique_differences[i])):
            binary = bin(j)[2:]
            while len(binary) < len(bin(2**unique_differences[i] - 1)[2:]):
                binary = '0' + binary

            if not '000' in binary:
                counter = counter + 1
        dict_amount_arrangements.update({unique_differences[i]: counter})

    for i in range(0, len(consecutive_difference_one)):
            amount_arrangements = amount_arrangements * dict_amount_arrangements[consecutive_difference_one[i]]

    return int(amount_arrangements)

if __name__ == "__main__":

    data = pd.read_csv("Day_10//Data.txt", header=None) 
    available_adapters = data.to_numpy().astype(int)

    data = pd.read_csv("Day_10//Test_01.txt", header=None) 
    test_one_available_adapters = data.to_numpy().astype(int)

    data = pd.read_csv("Day_10//Test_02.txt", header=None) 
    test_two_available_adapters = data.to_numpy().astype(int)

    test_one_difference_product = 35
    test_two_difference_product = 220
    test_one_possible_arrangements = 8
    test_two_possible_arrangements = 19208

    print_message = "Implementation Part One Wrong"
    if find_difference_prodcut_longest_chain(test_one_available_adapters) == test_one_difference_product:
        if find_difference_prodcut_longest_chain(test_two_available_adapters) == test_two_difference_product:
            print_message = "Solution Part One: " + str(find_difference_prodcut_longest_chain(available_adapters))
    print(print_message)

    print_message = "Implementation Part Two Wrong"
    if find_amount_possible_arrangements(test_one_available_adapters) == test_one_possible_arrangements:
        if find_amount_possible_arrangements(test_two_available_adapters) == test_two_possible_arrangements:
           print_message = "Solution Part Two: " + str(find_amount_possible_arrangements(available_adapters))
    print(print_message)