import numpy as np
import random

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
    _, _, corner = sort_tiles(tiles_modified_dictionary, tile_edges_modified_dictionary)
    
    corner_ids = np.zeros(0)
    for each_corner in corner:
        if not int(each_corner[0:4]) in corner_ids:
            corner_ids = np.append(corner_ids, int(each_corner[0:4]))

    return int(np.prod(corner_ids))

def find_map_layout(map_layout, dimension_map, tile_edges_modified_dictionary):
    for each_tile_edge in tile_edges_modified_dictionary:
        if not any(each_tile_edge[0:4] in map_element for map_element in map_layout):
            append_map = False
            if len(map_layout) < dimension_map:
                if tile_edges_modified_dictionary[map_layout[-1]]["right"] == tile_edges_modified_dictionary[each_tile_edge]["left"]:
                    append_map = True

            else:
                current_postion = len(map_layout) - dimension_map
                tile_edge_lower_edge = tile_edges_modified_dictionary[map_layout[current_postion]]["lower"]
                if tile_edge_lower_edge == tile_edges_modified_dictionary[each_tile_edge]["upper"]:
                    if current_postion % dimension_map == 0:
                        append_map = True
                    
                    if current_postion % dimension_map > 0:
                        tile_edge_right_edge = tile_edges_modified_dictionary[map_layout[-1]]["right"]
                        if tile_edge_right_edge == tile_edges_modified_dictionary[each_tile_edge]["left"]:
                            append_map = True

            if append_map == True:
                map_layout.append(each_tile_edge)
                if find_map_layout(map_layout, dimension_map, tile_edges_modified_dictionary) == False:
                    map_layout.remove(each_tile_edge)

    if len(map_layout) == (dimension_map * dimension_map):
        return True
    else:
        return False

def build_map_layout_without_edges(map_layout, dimension_map, tiles_modified_dictionary):
    map_layout_list = []
    
    for i in range(0, dimension_map * dimension_map, dimension_map):
        for j in range(1, 9):
            map_string = ""
            for k in range(0, dimension_map):
                map_string = map_string + str(tiles_modified_dictionary[map_layout[i+k]][j,:].tobytes().decode("utf-8"))[1:-1]
            map_layout_list.append(map_string)

    map_layout_array = np.chararray((dimension_map * (10 - 2), dimension_map * (10 - 2)))
    for i in range(0, len(map_layout_list)):
        for j in range(0, len(map_layout_list[i])):
            map_layout_array[i][j] = map_layout_list[i][j]

    return map_layout_array

def count_monsters(map_layout_array, monster_layout_list):
    monster_counter, hash_symbol = 0, ("#").encode()

    for i in range(0, len(map_layout_array)):
        for j in range(0, len(map_layout_array[i])):
            found_monster = True
            for k in range(0, len(monster_layout_list)):
                for each_position in monster_layout_list[k]:
                    if (i + k) < len(map_layout_array) and (j + each_position) < len(map_layout_array[i]):
                        if not map_layout_array[i + k][j + each_position] == hash_symbol:
                            found_monster = False
                            break
                    else:
                        found_monster = False
            if found_monster == True:  
                monster_counter = monster_counter + 1

    return monster_counter

def count_hashes(map_layout_array):
    hashes_counter, hash_symbol = 0, ("#").encode()

    for i in range(0, len(map_layout_array)):
        for j in range(0, len(map_layout_array[i])):
            if map_layout_array[i][j] == hash_symbol:
                hashes_counter = hashes_counter + 1

    return hashes_counter

def get_habitats_roughness(camera_tiles):
    monster_counter, hashes_counter, hashes_in_monster = 0, 0, 0
    monster_layout_list = [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]

    tiles_dictionary = parse_tile_to_dictionary(camera_tiles)
    dimension_map = int(np.sqrt(len(tiles_dictionary)))
    tiles_modified_dictionary = create_tile_versions(tiles_dictionary)
    tile_edges_modified_dictionary = get_tile_edges_strings(tiles_modified_dictionary)
    _, _, corner = sort_tiles(tiles_modified_dictionary, tile_edges_modified_dictionary)

    for each_corner in corner:
        map_layout = []
        map_layout.append(each_corner)
        if find_map_layout(map_layout, dimension_map, tile_edges_modified_dictionary) == True:
            map_layout_array = build_map_layout_without_edges(map_layout, dimension_map, tiles_modified_dictionary)

            for j in range(0, 4):
                monster_counter = count_monsters(np.rot90(map_layout_array, j), monster_layout_list)
                if monster_counter > 0:
                    break
                
                monster_counter = count_monsters(np.flipud(np.rot90(map_layout_array, j)), monster_layout_list)
                if monster_counter > 0:
                    break
                
                monster_counter = count_monsters(np.fliplr(np.rot90(map_layout_array, j)), monster_layout_list)
                if monster_counter > 0:
                    break

    hashes_counter = count_hashes(map_layout_array)
    for each_list in monster_layout_list:
        hashes_in_monster = hashes_in_monster + len(each_list)

    return hashes_counter - (hashes_in_monster * monster_counter)

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
        