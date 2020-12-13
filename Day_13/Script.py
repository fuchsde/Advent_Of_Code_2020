import numpy as np

def get_first_bus_id_multiplied_waiting_minutes(bus_schedule):
    possible_departure_time = int(bus_schedule[0])
    available_bus_schedule = np.array(bus_schedule[1].replace("x,", "").split(",")).astype('int')
    waiting_time_for_each_bus = np.zeros(len(available_bus_schedule))

    for j in range(0, len(available_bus_schedule)):
        for i in range(0, available_bus_schedule[j]):
            if (possible_departure_time + i) % available_bus_schedule[j] == 0:
                waiting_time_for_each_bus[j] = i

    shortest_waiting_time = np.min(waiting_time_for_each_bus)
    bus_id_shortest_waiting_time = available_bus_schedule[np.where(waiting_time_for_each_bus == shortest_waiting_time)]
    return int(bus_id_shortest_waiting_time * shortest_waiting_time)

def get_earliest_timestamp_where_busses_depart_at_given_offset(bus_schedule):
    earliest_timestamp = 0
    running_product = 1
    bus_ids, bus_ids_offset = np.zeros(0), np.zeros(0)
    available_bus_ids = bus_schedule[1].split(",")

    for i in range(0, len(available_bus_ids)):
        if available_bus_ids[i].isdigit():
           bus_ids = np.append(bus_ids, int(available_bus_ids[i])).astype(float)
           bus_ids_offset = np.append(bus_ids_offset, i).astype(float)

    for i in range(0, len(bus_ids)):
        while (earliest_timestamp + bus_ids_offset[i]) % bus_ids[i] != 0:
            earliest_timestamp = earliest_timestamp + running_product
        running_product = running_product * bus_ids[i]

    return int(earliest_timestamp)

if __name__ == "__main__":

    bus_schedule = []
    with open("Day_13//Data.txt") as data_file:
        for line in data_file:
            bus_schedule.append(line.strip())
    
    test_bus_schedule = []
    with open("Day_13//Test.txt") as data_file:
        for line in data_file:
            test_bus_schedule.append(line.strip())

    test_bus_id_multiplied_waiting_minutes = 295
    test_earliest_timestep = 1068781
    
    if get_first_bus_id_multiplied_waiting_minutes(test_bus_schedule) == test_bus_id_multiplied_waiting_minutes:
        print("Solution Part One: " + str(get_first_bus_id_multiplied_waiting_minutes(bus_schedule)))
    else:
        print("Implementation Part One Wrong")

    if get_earliest_timestamp_where_busses_depart_at_given_offset(test_bus_schedule) == test_earliest_timestep:
        print("Solution Part Two: " + str(get_earliest_timestamp_where_busses_depart_at_given_offset(bus_schedule)))
    else:
        print("Implementation Part Two Wrong")
        