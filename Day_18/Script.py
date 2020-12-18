import numpy as np

def solve_equation(equation_list):
    equation = ""

    for each_char in equation_list:
        equation = equation + each_char

    return  str(eval(equation))

def solve_equation_from_left_to_right(equation_list):
    while len(equation_list) > 1:
        operator_counter = 0

        for i in range(0, len(equation_list)):
            if not equation_list[i].isdigit():
                operator_counter = operator_counter + 1

            if operator_counter == 2:
                equation_list[i-1] = solve_equation(equation_list[0:i])
                del equation_list[0:i-1]
                break

        if operator_counter == 1:
            equation_list[0] = solve_equation(equation_list[0:])
            del equation_list[1:]

    return equation_list[0]

def solve_equation_addition_first(equation_list):
    while "+" in equation_list:
        idx_addition, start_idx_addition, end_idx_addition = equation_list.index('+'), 0, len(equation_list)

        for j in range(idx_addition-1, -1, -1):
            if not equation_list[j].isdigit():
                start_idx_addition = j + 1
                break

        for i in range(idx_addition+1, len(equation_list)):
            if not equation_list[i].isdigit():
                end_idx_addition = i
                break

        equation_list[start_idx_addition] = solve_equation(equation_list[start_idx_addition:end_idx_addition])
        del equation_list[start_idx_addition+1:end_idx_addition]
        
    return solve_equation_from_left_to_right(equation_list)

def solve_equation_recursive(equation_list, solving_function):
    if "(" in equation_list:
        opening_brackets, closing_brackets, idx_open_bracket = 0, 0, 0

        for i in range(0, len(equation_list)):
            if equation_list[i] == "(":
                opening_brackets = opening_brackets + 1
                if opening_brackets == 1:
                    idx_open_bracket = i

            if equation_list[i] == ")":
                closing_brackets = closing_brackets + 1

            if opening_brackets > 0 and opening_brackets == closing_brackets:
                result = solve_equation_recursive(equation_list[idx_open_bracket+1:i], solving_function)
                equation_list[i] = result
                del equation_list[idx_open_bracket:i]

                if "(" in equation_list:
                    return solve_equation_recursive(equation_list, solving_function)
                else:
                    return solving_function(equation_list)
    else:
        return solving_function(equation_list)

def get_sum_equations(equations, solving_function):
    soltion_equations = np.zeros(len(equations))

    for j in range(0, len(equations)) :
        soltion_equations[j] = int(solve_equation_recursive(list(equations[j].replace(" ", "")), solving_function))

    return int(np.sum(soltion_equations))

if __name__ == "__main__":

    equations = []
    with open("Day_18//Data.txt") as data_file:
        for line in data_file:
            equations.append(line.strip())
    
    test_equations = []
    with open("Day_18//Test.txt") as data_file:
        for line in data_file:
            test_equations.append(line.strip())

    test_sum_equations_left_to_right = 26386
    test_sum_equations_addition_first = 693942
    
    if get_sum_equations(test_equations, solve_equation_from_left_to_right) == test_sum_equations_left_to_right:
        print("Solution Part One: " + str(get_sum_equations(equations, solve_equation_from_left_to_right)))
    else:
        print("Implementation Part One Wrong")

    if get_sum_equations(test_equations, solve_equation_addition_first) == test_sum_equations_addition_first:
        print("Solution Part Two: " + str(get_sum_equations(equations, solve_equation_addition_first)))
    else:
        print("Implementation Part Two Wrong")
        