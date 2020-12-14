import numpy as np

def get_sum_program_memory(program_code):
    program_memory = {}
    sum_program_memory = 0
    current_mask = ""

    for i in range(0, len(program_code)):
        if "mask" in program_code[i]:
            current_mask = program_code[i].split(" = ")[1].strip()
        else:
            memory_address, memory_value = program_code[i].split(" = ")
            memory_address = int(memory_address[memory_address.find("[") + len("["):memory_address.find("]")])
            memory_value_binary = bin(int(memory_value))[2:]

            while len(memory_value_binary) < len(current_mask):
                memory_value_binary = '0' + memory_value_binary

            memory_value_binary_masked = ""
            for i in range(0, len(current_mask)):
                if current_mask[i] == 'X':
                    memory_value_binary_masked = memory_value_binary_masked + memory_value_binary[i]
                else:
                    memory_value_binary_masked = memory_value_binary_masked + current_mask[i]

            program_memory.update({memory_address: int(memory_value_binary_masked, 2)})

    for memory_address in program_memory:
        sum_program_memory = sum_program_memory + program_memory[memory_address]

    return  sum_program_memory

def get_sum_program_memory_with_floating_bits(program_code):
    program_memory = {}
    sum_program_memory = 0
    current_mask = ""

    for i in range(0, len(program_code)):
        if "mask" in program_code[i]:
            current_mask = program_code[i].split(" = ")[1].strip()
        else:
            memory_address, memory_value = program_code[i].split(" = ")
            memory_address = int(memory_address[memory_address.find("[") + len("["):memory_address.find("]")])
            memory_address_binary = bin(memory_address)[2:]
            memory_value = int(memory_value)

            while len(memory_address_binary) < len(current_mask):
                memory_address_binary = '0' + memory_address_binary
                
            memory_address_binary_masked = ""
            for i in range(0, len(current_mask)):
                if current_mask[i] == 'X' or current_mask[i] == "1":
                    memory_address_binary_masked = memory_address_binary_masked + current_mask[i]
                else:
                    memory_address_binary_masked = memory_address_binary_masked + memory_address_binary[i]
        
            for i in range(0, (2**memory_address_binary_masked.count('X'))):
                memory_address_binary_floating = memory_address_binary_masked
                binary = bin(i)[2:]
                while len(binary) < len(bin(2**memory_address_binary_masked.count('X') - 1)[2:]):
                    binary = '0' + binary
                
                for j in range(0, len(binary)):
                    memory_address_binary_floating = memory_address_binary_floating.replace('X', binary[j], 1)
                    
                program_memory.update({int(memory_address_binary_floating, 2): memory_value})

    for memory_address in program_memory:
        sum_program_memory = sum_program_memory + program_memory[memory_address]

    return  sum_program_memory

if __name__ == "__main__":

    program_code = []
    with open("Day_14//Data.txt") as data_file:
        for line in data_file:
            program_code.append(line.strip())
    
    test_program_code_one = []
    with open("Day_14//Test_Part_One.txt") as data_file:
        for line in data_file:
            test_program_code_one.append(line.strip())

    test_program_code_two = []
    with open("Day_14//Test_Part_Two.txt") as data_file:
        for line in data_file:
            test_program_code_two.append(line.strip())

    test_sum_memory = 165
    test_sum_memory_floating_bits = 208
    
    if get_sum_program_memory(test_program_code_one) == test_sum_memory:
        print("Solution Part One: " + str(get_sum_program_memory(program_code)))
    else:
        print("Implementation Part One Wrong")

    if get_sum_program_memory_with_floating_bits(test_program_code_two) == test_sum_memory_floating_bits:
        print("Solution Part Two: " + str(get_sum_program_memory_with_floating_bits(program_code)))
    else:
        print("Implementation Part Two Wrong")
        