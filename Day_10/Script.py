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

    for i in range(0, len(consecutive_difference_one)):
        if consecutive_difference_one[i] < 3:
            amount_arrangements = amount_arrangements * 2 ** consecutive_difference_one[i]
        elif consecutive_difference_one[i] == 3: 
            amount_arrangements = amount_arrangements * (2 ** consecutive_difference_one[i] - 1)
        else:
            print("Case not covered yet. Consecutive difference is greater 4.")
            return 0

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