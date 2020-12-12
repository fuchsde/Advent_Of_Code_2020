import numpy as np

def rotate_position(position, command, amount):
    rotation = "ESWN"
    current_orientation = rotation.find(position['F'])
    amount_rotations = int(amount / 90)
    if(command == 'R'):
        position['F'] = rotation[(current_orientation + amount_rotations) % len(rotation)]
    elif(command == 'L'):
        position['F'] = rotation[(current_orientation - amount_rotations) % len(rotation)]

def get_manhatten_distance(instructions):
    manhatten_distance = 0
    position = {"N": 0, "S": 0, "W": 0, "E": 0, "F":"E"}

    for each_instruction in instructions:
        command, amount = each_instruction[0], int(each_instruction[1:])
        if 'N' in command or 'S' in command or 'W' in command or 'E' in command:
            position[command] = position[command] + amount
        elif 'L' in command or 'R' in command:
            rotate_position(position, command, amount)
        else:
            position[position[command]] = position[position[command]] + amount

    manhatten_distance = abs(position['N'] - position['S']) + abs(position['E'] - position['W'])
    return manhatten_distance

def rotate_waypoint(waypoint, command, amount):
    rotation = ""
    if(command == 'R'):
        rotation = "SENW"
    elif(command == 'L'):
        rotation = "SWNE"
    for i in range(0, int(amount / 90)):
            waypoint_copy = waypoint.copy()
            waypoint[rotation[0]] = waypoint_copy[rotation[1]]
            waypoint[rotation[1]] = waypoint_copy[rotation[2]]
            waypoint[rotation[2]] = waypoint_copy[rotation[3]]
            waypoint[rotation[3]] = waypoint_copy[rotation[0]]

def get_manhatten_distance_relative_instructions(instructions):
    manhatten_distance = 0
    waypoint = {"E": 10, "S": 0, "W": 0, "N": 1}
    position = {"E": 0, "S": 0, "W": 0, "N": 0}

    for each_instruction in instructions:
        command, amount = each_instruction[0], int(each_instruction[1:])
        if 'N' in command or 'S' in command or 'W' in command or 'E' in command:
            waypoint[command] = waypoint[command] + amount
        elif 'L' in command or 'R' in command:
            rotate_waypoint(waypoint, command, amount)
        else:
            for key in position:
                position[key] = position[key] + amount * waypoint[key]

    manhatten_distance = abs(position['N'] - position['S']) + abs(position['E'] - position['W'])
    return manhatten_distance

if __name__ == "__main__":

    instructions = []
    with open("Day_12//Data.txt") as data_file:
        for line in data_file:
            instructions.append(line.strip())
    
    test_instructions = []
    with open("Day_12//Test.txt") as data_file:
        for line in data_file:
            test_instructions.append(line.strip())

    first_test_manhatten_distance = 25
    second_test_manhatten_distance = 286
    
    if get_manhatten_distance(test_instructions) == first_test_manhatten_distance:
        print("Solution Part One: " + str(get_manhatten_distance(instructions)))
    else:
        print("Implementation Part One Wrong")

    if get_manhatten_distance_relative_instructions(test_instructions) == second_test_manhatten_distance:
        print("Solution Part Two: " + str(get_manhatten_distance_relative_instructions(instructions)))
    else:
        print("Implementation Part Two Wrong")
        