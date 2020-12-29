import copy

def get_amount_black_tiles(tile_list, return_list_black_tiles = False):
    amount_black_tiles = 0
    tile_coordinates, black_tiles_coordinates = [], []

    for each_tile in tile_list:
        tile_orientation = each_tile
        tile_dict = {}
        x, y = 0, 0

        x = x + (tile_orientation.count("nw") + tile_orientation.count("sw")) * -1
        y = y + (tile_orientation.count("nw") + tile_orientation.count("ne")) * 1
        x = x + (tile_orientation.count("ne") + tile_orientation.count("se")) * 1
        y = y + (tile_orientation.count("sw") + tile_orientation.count("se")) * -1
        
        tile_orientation = tile_orientation.replace("nw", "")
        tile_orientation = tile_orientation.replace("ne", "")
        tile_orientation = tile_orientation.replace("sw", "")
        tile_orientation = tile_orientation.replace("se", "")

        x = x + tile_orientation.count("w") * -2
        x = x + tile_orientation.count("e") * 2

        tile_dict['x'] = x
        tile_dict['y'] = y
        tile_coordinates.append(tile_dict)

    for each_tile_coordinate in tile_coordinates:
        if tile_coordinates.count(each_tile_coordinate) == 1:
            amount_black_tiles = amount_black_tiles + 1
            black_tiles_coordinates.append(each_tile_coordinate)

    if return_list_black_tiles == False:
        return amount_black_tiles
    else:
        return black_tiles_coordinates

def get_tile_information(x, y, old_black_tile_coordinates):
    tile = {}
    tile['x'], tile['y'] = x, y
     
    tile_is_black = False
    if tile in old_black_tile_coordinates:
        tile_is_black = True

    return tile, tile_is_black

def get_amount_adjacant_black_tiles(x, y, old_black_tile_coordinates):
    adjacant_black_tiles = 0
    delta_coordinates = [[-2, 0], [-1, 1], [1, 1], [2, 0], [1, -1], [-1, -1]]

    for each_delta_coordinate in delta_coordinates:
        adjacant_tile = {}
        adjacant_tile['x'] = x + each_delta_coordinate[0]
        adjacant_tile['y'] = y + each_delta_coordinate[1]
        
        if adjacant_tile in old_black_tile_coordinates:
            adjacant_black_tiles = adjacant_black_tiles + 1

    return adjacant_black_tiles

def get_amount_black_tiles_after_n_days(tile_list, amount_days):
    amount_black_tiles = 0
    delta_coordinates = [[0, 0],[-2, 0], [-1, 1], [1, 1], [2, 0], [1, -1], [-1, -1]]
    old_black_tile_coordinates = get_amount_black_tiles(tile_list, True)
    
    for _ in range(0, amount_days):
        new_black_tile_coordinates = []

        for each_black_tile in old_black_tile_coordinates:
            for each_delta_coordinate in delta_coordinates:
                tile = {}
                tile['x'] = each_black_tile['x'] + each_delta_coordinate[0]
                tile['y'] = each_black_tile['y'] + each_delta_coordinate[1]

                if not tile in new_black_tile_coordinates:
                    adjacant_black_tiles = get_amount_adjacant_black_tiles(tile['x'], tile['y'], old_black_tile_coordinates)

                    if adjacant_black_tiles == 2:
                        new_black_tile_coordinates.append(tile)
                    elif adjacant_black_tiles == 1 and tile in old_black_tile_coordinates:
                        new_black_tile_coordinates.append(tile)

        old_black_tile_coordinates = copy.deepcopy(new_black_tile_coordinates)
            
    amount_black_tiles = len(new_black_tile_coordinates)
    return amount_black_tiles

if __name__ == "__main__":

    tile_list = []
    with open("Day_24//Data.txt") as data_file:
        for line in data_file:
            tile_list.append(line.strip())
    
    test_tile_list = []
    with open("Day_24//Test.txt") as data_file:
        for line in data_file:
            test_tile_list.append(line.strip())

    amount_days = 100
    test_amount_black_tiles = 10 
    test_amount_black_tiles_after_100_days = 2208

    if get_amount_black_tiles(test_tile_list) == test_amount_black_tiles:
        print("Solution Part One: " + str(get_amount_black_tiles(tile_list)))
    else:
        print("Implementation Part One Wrong")

    if get_amount_black_tiles_after_n_days(test_tile_list, amount_days) == test_amount_black_tiles_after_100_days:
        print("Solution Part Two: " + str(get_amount_black_tiles_after_n_days(tile_list, amount_days)))
    else:
        print("Implementation Part Two Wrong")
        