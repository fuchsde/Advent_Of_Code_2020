import pandas as pd
import numpy as np

def run_program_once(program_code):
    accumulator, i  = 0, 0
    amount_execution = np.zeros(len(program_code))
    program_execution_finished = False

    while i < len(program_code) and amount_execution[i] == 0:
        command, amount = program_code[i][0].split(" ")

        if "nop" in command:
            amount_execution[i] = amount_execution[i] + 1
            i = i + 1
        elif "acc" in command:
            amount_execution[i] = amount_execution[i] + 1
            i = i + 1
            accumulator = accumulator + int(amount)
        elif "jmp" in command:
            amount_execution[i] = amount_execution[i] + 1
            i = i + int(amount)
    
    if i >= len(program_code):
        program_execution_finished = True
    return accumulator, program_execution_finished

def run_program_without_double_execution(program_code):
    accumulator, program_execution_finished = run_program_once(program_code)
    return accumulator

def run_and_fix_program(program_code):
    for i in range(0, len(program_code)):
        if "jmp" in program_code[i][0]:
            program_code[i][0] = program_code[i][0].replace("jmp", "nop")
            accumulator, program_execution_finished = run_program_once(program_code)
            program_code[i][0] = program_code[i][0].replace("nop", "jmp")
            if(program_execution_finished == True):
                break
        elif "nop" in program_code[i][0]:
            program_code[i][0] = program_code[i][0].replace("nop", "jmp")
            accumulator, program_execution_finished = run_program_once(program_code)
            program_code[i][0] = program_code[i][0].replace("jmp", "nop")
            if(program_execution_finished == True):
                break
        
    return accumulator

if __name__ == "__main__":

    data = pd.read_csv("Day_8//Data.txt", header=None) 
    program_code = data.values.tolist()

    data = pd.read_csv("Day_8//Test.txt", header=None) 
    test_programm_code = data.values.tolist()

    test_result_program_code_one = 5
    test_result_program_code_two = 8

    if run_program_without_double_execution(test_programm_code) == test_result_program_code_one:
        print("Solution Part One: " + str(run_program_without_double_execution(program_code)))
    else:
        print("Implementation Part One Wrong")

    if run_and_fix_program(test_programm_code) == test_result_program_code_two:
       print("Solution Part Two: " + str(run_and_fix_program(program_code)))
    else:
       print("Implementation Part Two Wrong")
        
