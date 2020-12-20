import numpy as np

def parse_tile_to_dictionary(camera_tiles):
    camera_tiles_dictionary = {}
    for each_line in camera_tiles:
        if "Tile" in each_line:
            tile_number = each_line.split(" ")[1].replace(":", "").strip()
            tile_layout = np.chararray((10, 10))
            line_counter = 0
            
        elif "#" in each_line or "."  in each_line:
            for j in range(0, len(each_line)):
                tile_layout[line_counter][j] = each_line[j]
            line_counter = line_counter+ 1
        else:
            camera_tiles_dictionary[tile_number] = tile_layout
    return camera_tiles_dictionary

def create_tile_versions(tiles_dictionary):
    tiles_modified_dictionary = {}

    for each_tile in tiles_dictionary:
        for j in range(0, 4):
            tiles_modified_dictionary[each_tile + "_r" + str(j)] = np.rot90(tiles_dictionary[each_tile], j)
            tiles_modified_dictionary[each_tile + "_v_r" + str(j)] = np.flipud( np.rot90(tiles_dictionary[each_tile], j))
            tiles_modified_dictionary[each_tile + "_h_r" + str(j)] = np.fliplr( np.rot90(tiles_dictionary[each_tile], j))

    return tiles_modified_dictionary

def get_tile_edges_strings(tiles_modified_dictionary):
    tile_edges_modified_dictionary = {}
    
    for each_tile in tiles_modified_dictionary:
        edges_dict = {}
        edges_dict["right"] = tiles_modified_dictionary[each_tile][:,9].tobytes()
        edges_dict["left"] = tiles_modified_dictionary[each_tile][:,0].tobytes()
        edges_dict["upper"] = tiles_modified_dictionary[each_tile][0,:].tobytes()
        edges_dict["lower"] = tiles_modified_dictionary[each_tile][9,:].tobytes()
        tile_edges_modified_dictionary[each_tile] = edges_dict

    return tile_edges_modified_dictionary

def sort_tiles(tiles_modified_dictionary, tile_edges_modified_dictionary):
    middle, edge, corner = {}, {}, {}
    for each_tile in tiles_modified_dictionary:
        upper_edge, lower_edge, left_edge, right_edge = 0, 0, 0, 0
        for each_other_tile in tiles_modified_dictionary:
            if not each_tile[0:4] == each_other_tile[0:4]:
                if tile_edges_modified_dictionary[each_tile]["right"] == tile_edges_modified_dictionary[each_other_tile]["right"]:
                    right_edge = 1
                if tile_edges_modified_dictionary[each_tile]["left"] == tile_edges_modified_dictionary[each_other_tile]["left"]:
                    left_edge = 1
                if tile_edges_modified_dictionary[each_tile]["upper"] == tile_edges_modified_dictionary[each_other_tile]["upper"]:
                    upper_edge = 1
                if tile_edges_modified_dictionary[each_tile]["lower"] == tile_edges_modified_dictionary[each_other_tile]["lower"]:
                    lower_edge = 1

        if right_edge + left_edge + lower_edge + upper_edge == 4:
            middle[each_tile] = tiles_modified_dictionary[each_tile]
        elif right_edge + left_edge + lower_edge + upper_edge == 3:
            edge[each_tile] = tiles_modified_dictionary[each_tile]
        elif right_edge + left_edge + lower_edge + upper_edge == 2:
            corner[each_tile] = tiles_modified_dictionary[each_tile]

    return middle, edge, corner

def get_product_tile_ids_corners(camera_tiles):

    tiles_dictionary = parse_tile_to_dictionary(camera_tiles)
    tiles_modified_dictionary = create_tile_versions(tiles_dictionary)
    tile_edges_modified_dictionary = get_tile_edges_strings(tiles_modified_dictionary)
    middle, edge, corner = sort_tiles(tiles_modified_dictionary, tile_edges_modified_dictionary)
    
    corner_ids = np.zeros(0)
    for each_corner in corner:
        if not int(each_corner[0:4]) in corner_ids:
            corner_ids = np.append(corner_ids, int(each_corner[0:4]))

    product_tile_ids_corners = int(np.prod(corner_ids))
    return product_tile_ids_corners

def get_habitats_roughness(camera_tiles):

    tiles_dictionary = parse_tile_to_dictionary(camera_tiles)
    tiles_modified_dictionary = create_tile_versions(tiles_dictionary)
    tile_edges_modified_dictionary = get_tile_edges_strings(tiles_modified_dictionary)
    middle, edge, corner = sort_tiles(tiles_modified_dictionary, tile_edges_modified_dictionary)
    
    return 0

if __name__ == "__main__":

    camera_tiles = []
    with open("Day_20//Data.txt") as data_file:
        for line in data_file:
            camera_tiles.append(line.strip())
    
    test_camera_tiles = []
    with open("Day_20//Test.txt") as data_file:
        for line in data_file:
            test_camera_tiles.append(line.strip())

    test_product_corners = 20899048083289
    test_habitats_roughness = 273
    
    if get_product_tile_ids_corners(test_camera_tiles) == test_product_corners:
        print("Solution Part One: " + str(get_product_tile_ids_corners(camera_tiles)))
    else:
        print("Implementation Part One Wrong")

    if get_habitats_roughness(test_camera_tiles) == test_habitats_roughness:
        print("Solution Part Two: " + str(get_habitats_roughness(camera_tiles)))
    else:
        print("Implementation Part Two Wrong")
        