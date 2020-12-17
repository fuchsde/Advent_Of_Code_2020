import copy

ACTIVE = "#"
INACTIVE = "."

def check_append_z_necessary(grid):
    outer_z_layers = [0, len(grid)-1]
    for each_outer_layer in outer_z_layers:
        for each_xy_grid in grid[each_outer_layer]:
            if ACTIVE in each_xy_grid:
                return 1
    return 0

def check_append_y_necessary(grid):
    outer_y_layers = [0, len(grid[0])-1]
    for each_z_grid in grid:
        for each_outer_layer in outer_y_layers:
            if ACTIVE in each_z_grid[each_outer_layer]:
                return 1
    return 0

def check_append_x_necessary(grid):
    outer_x_layers = [0, len(grid[0][0])-1]
    for each_z_grid in grid:
        for each_outer_layer in outer_x_layers:
            for each_xy_grid in each_z_grid:
                if ACTIVE in each_xy_grid[each_outer_layer]:
                    return 1
    return 0

def check_append_w_necessary(grid_list):
    outer_w_layers = [0, len(grid_list)-1]
    for each_outer_layer in outer_w_layers:
        for each_z_grid in grid_list[each_outer_layer]:
            for each_xy_grid in each_z_grid:
                if ACTIVE in each_xy_grid:
                    return 1
    return 0

def append_z(grid):
    grid.insert(0, copy.deepcopy(grid[0]))
    grid.append(copy.deepcopy(grid[0]))
    outer_z_layers =[0, len(grid)-1]
    for each_outer_layer in outer_z_layers:
        for i in range(0, len(grid[each_outer_layer])):
            for j in range(0, len(grid[each_outer_layer][i])):
                grid[each_outer_layer][i][j] = INACTIVE

def append_y(grid):
    for each_z_grid in grid:
        each_z_grid.insert(0, copy.deepcopy(each_z_grid[0]))
        each_z_grid.append(copy.deepcopy(each_z_grid[0]))
    outer_y_layers = [0, len(grid[0])-1]
    for each_z_grid in grid:
        for each_outer_layer in outer_y_layers:
            for i in range(0, len(each_z_grid[each_outer_layer])):
                each_z_grid[each_outer_layer][i] = INACTIVE

def append_x(grid):
    for each_z_grid in grid:
        for each_xy_grid in each_z_grid:
            each_xy_grid.insert(0, INACTIVE)
            each_xy_grid.append(INACTIVE)

def append_w(grid_list):
    grid_list.insert(0, copy.deepcopy(grid_list[0]))
    grid_list.append(copy.deepcopy(grid_list[0]))
    outer_w_layers = [0, len(grid_list)-1]
    for each_outer_layer in outer_w_layers:
        for z in range(0, len(grid_list[each_outer_layer])):
            for y in range(0, len(grid_list[each_outer_layer][z])):
                for x in range(0, len(grid_list[each_outer_layer][z][y])):
                    grid_list[each_outer_layer][z][y][x] = INACTIVE

def add_outer_layer_grid_list(grid_list, dimensions):
    append_z_necessary, append_y_necessary, append_x_necessary = 0, 0, 0
    for each_grid in grid_list:
        append_z_necessary = append_z_necessary + check_append_z_necessary(each_grid)
        append_y_necessary = append_y_necessary + check_append_y_necessary(each_grid)
        append_x_necessary = append_x_necessary + check_append_x_necessary(each_grid)
        
    for each_grid in grid_list:
        if append_z_necessary > 0:
            append_z(each_grid)
        if append_y_necessary > 0:
            append_y(each_grid)
        if append_x_necessary > 0:
            append_x(each_grid)
        
    if dimensions == 4 and check_append_w_necessary(grid_list) == 1:
        append_w(grid_list)

def get_amount_active_neighours(grid, z, y, x, count_same_coordinate = False):
    amount_active_neighbours = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                    if 0 <= z+i < len(grid) and 0 <= y+j < len(grid[0]) and 0 <= x+k < len(grid[0][0]):
                        if grid[z+i][y+j][x+k] == ACTIVE:
                            amount_active_neighbours = amount_active_neighbours + 1

    if count_same_coordinate == False and grid[z][y][x] == ACTIVE:
        amount_active_neighbours = amount_active_neighbours - 1

    return amount_active_neighbours

def get_amount_active_neighours_grid_list(grid_list, w, z, y, x):
    amount_active_neighbours = 0
    amount_active_neighbours = amount_active_neighbours + get_amount_active_neighours(grid_list[w], z, y, x)

    if 0 <= (w-1) < len(grid_list):
        amount_active_neighbours = amount_active_neighbours + get_amount_active_neighours(grid_list[w-1], z, y, x, True)
        
    if 0 <= (w+1) < len(grid_list):
        amount_active_neighbours = amount_active_neighbours + get_amount_active_neighours(grid_list[w+1], z, y, x, True)
    
    return amount_active_neighbours

def initial_grid_to_list(initial_grid):
    old_grid = []
    old_grid.append([])
    for j in range(0, len(initial_grid)):
        old_grid[0].append([])
        for each_grid in initial_grid[j]:
            old_grid[0][j].append(each_grid)
    return old_grid

def get_active_cubes_after_n_cycles(initial_grid, dimensions, cycles):
    actives_cubes = 0
    old_grid = initial_grid_to_list(initial_grid)

    grid_list_old_grids = []
    grid_list_old_grids.append(old_grid)
    

    for j in range(0, cycles): 
        actives_cubes = 0
        add_outer_layer_grid_list(grid_list_old_grids, dimensions)
        grid_list_new_grids = copy.deepcopy(grid_list_old_grids)
        
        for w in range(0, len(grid_list_old_grids)):
            for z in range(0, len(grid_list_old_grids[w])):
                for y in range(0, len(grid_list_old_grids[w][z])):
                    for x in range(0, len(grid_list_old_grids[w][z][y])):
                        active_neighbours = get_amount_active_neighours_grid_list(grid_list_old_grids, w, z, y, x)

                        if grid_list_old_grids[w][z][y][x] == ACTIVE and (active_neighbours < 2 or active_neighbours > 3):
                            grid_list_new_grids[w][z][y][x] = INACTIVE
                        elif grid_list_old_grids[w][z][y][x] == INACTIVE and active_neighbours == 3:
                            grid_list_new_grids[w][z][y][x] = ACTIVE

                        if j == (cycles-1) and grid_list_new_grids[w][z][y][x] == ACTIVE:
                            actives_cubes = actives_cubes + 1

        grid_list_old_grids = copy.deepcopy(grid_list_new_grids)
    return actives_cubes

if __name__ == "__main__":

    initial_grid = []
    with open("Day_17//Data.txt") as data_file:
        for line in data_file:
            initial_grid.append(line.strip())
    
    test_initial_grid = []
    with open("Day_17//Test.txt") as data_file:
        for line in data_file:
            test_initial_grid.append(line.strip())

    cycles = 6
    part_one_dimensions = 3
    test_active_cubes_three_dimension = 112
    part_two_dimensions = 4
    test_active_cubes_four_dimension = 848
    
    if get_active_cubes_after_n_cycles(test_initial_grid, part_one_dimensions, cycles) == test_active_cubes_three_dimension:
        print("Solution Part One: " + str(get_active_cubes_after_n_cycles(initial_grid, part_one_dimensions, cycles)))
    else:
        print("Implementation Part One Wrong")

    if get_active_cubes_after_n_cycles(test_initial_grid, part_two_dimensions, cycles) == test_active_cubes_four_dimension:
        print("Solution Part One: " + str(get_active_cubes_after_n_cycles(initial_grid, part_two_dimensions, cycles)))
    else:
        print("Implementation Part Two Wrong")

