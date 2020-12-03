import pandas as pd
import numpy as np

data = pd.read_csv("Data.txt", header=None) 
route = data.values.tolist()

print("Starting Part One")
row = 0
row_increment = 1
column = 0 
column_increment = 3
columns_in_route = len(route[0][0])
tree = '#'
counter_trees = 0

for i in range(0, len(route) - 1, row_increment):
    row = row + row_increment
    column = column + column_increment
    current_column = column % columns_in_route

    if route[row][0][current_column] == tree:
        counter_trees = counter_trees + 1

print(counter_trees)

print("Starting Part Two")
row_increment_list = [1, 1, 1, 1, 2]
column_increment_list = [1, 3, 5, 7, 1]

columns_in_route = len(route[0][0])
tree = '#'
counter_trees_list = np.zeros(5)

for j in range(0, len(row_increment_list)):
    row = 0
    row_increment = row_increment_list[j]
    column = 0 
    column_increment = column_increment_list[j]
    counter_trees = 0
    for i in range(0, len(route) - 1, row_increment):
        row = row + row_increment
        column = column + column_increment
        current_column = column % columns_in_route

        if route[row][0][current_column] == tree:
            counter_trees = counter_trees + 1

    counter_trees_list[j] = counter_trees

print(int(counter_trees_list[0] * counter_trees_list[1] * counter_trees_list[2] * counter_trees_list[3] * counter_trees_list[4]))
