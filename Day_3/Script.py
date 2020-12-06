import pandas as pd

def count_trees_on_route(route, tree, row_increment, column_increment):
    row = 0
    column = 0 
    counter_trees = 0
    columns_in_route = len(route[0][0])
    for i in range(0, len(route) - 1, row_increment):
        row = row + row_increment
        column = column + column_increment
        current_column = column % columns_in_route

        if route[row][0][current_column] == tree:
            counter_trees = counter_trees + 1

    return counter_trees

def count_trees_part_one(route, tree):
    row_increment = 1
    column_increment = 3
    return count_trees_on_route(route, tree, row_increment, column_increment)

def count_trees_part_two(route, tree):
    row_increment_list = [1, 1, 1, 1, 2]
    column_increment_list = [1, 3, 5, 7, 1]
    counter_trees = 1
    for j in range(0, len(row_increment_list)):
        counter_trees = counter_trees * count_trees_on_route(route, tree, row_increment_list[j], column_increment_list[j])
    return counter_trees

if __name__ == "__main__":

    data = pd.read_csv("Day_3//Data.txt", header=None) 
    route = data.values.tolist()

    data = pd.read_csv("Day_3//Test.txt", header=None) 
    test_route = data.values.tolist()
    test_result_first_route = 7
    test_result_second_route = 336

    tree = '#'

    if count_trees_part_one(test_route, tree) == test_result_first_route:
        print("Solution Part One: " + str(count_trees_part_one(route, tree)))
    else:
        print("Implementation Part One Wrong")

    if count_trees_part_two(test_route, tree) == test_result_second_route:
        print("Solution Part Two: " + str(count_trees_part_two(route, tree)))
    else:
        print("Implementation Part Two Wrong")
        