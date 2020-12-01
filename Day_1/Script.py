import pandas as pd
import numpy as np

data = pd.read_csv("Data.txt", header=None, names=['Numbers']) 

sum = 2020
numbers = data.Numbers.to_numpy()
amount_numbers = len(numbers)

print("Starting Part One")
difference = np.zeros(amount_numbers)
for i in range(0, amount_numbers):
    difference[i] = sum - numbers[i]

for i in range(0, amount_numbers):
    for j in range(0, amount_numbers):
        if numbers[i] == difference[j]:
            solution = int(numbers[i] * difference[i])
print(solution)

difference = np.zeros(amount_numbers**2)
first_number = np.zeros(amount_numbers**2)
second_number = np.zeros(amount_numbers**2)
for i in range(0, amount_numbers):
    for j in range(0, amount_numbers):
        first_number[i * amount_numbers + j] = numbers[i]
        second_number[i * amount_numbers + j] = numbers[j]
        difference[i * amount_numbers + j] = sum - numbers[i] - numbers[j]

for i in range(0, amount_numbers**2):
    for j in range(0, amount_numbers):
        if numbers[j] == difference[i]:
            solution = int(numbers[j] * first_number[i] * second_number[i])
print(solution)
print("Starting Part Two")
solution = -1
for index, row in data.iterrows():
    if not solution == -1:
        break 
    for index_2, row_2 in data.iterrows():
        if not solution == -1:
            break 
        for index_3, row_3 in data.iterrows():
            if row['Numbers'] + row_2['Numbers'] + row_3['Numbers'] == 2020:
                solution = row['Numbers'] * row_2['Numbers'] * row_3['Numbers']
                print(solution)
                break