import pandas as pd
import numpy as np

data = pd.read_csv("Data.txt", header=None) 
seats_coded = data.values.tolist()

print("Starting Part One")
rows = 127
column = 7

seats_decoded = np.zeros(len(seats_coded))
for i in range(0, len(seats_coded)):
    seat_binary_code = seats_coded[i][0].replace('F', '0') 
    seat_binary_code = seat_binary_code.replace('B', '1')
    seat_binary_code = seat_binary_code.replace('L', '0')
    seat_binary_code = seat_binary_code.replace('R', '1')
    seats_decoded[i] = int(int(seat_binary_code[0:7], 2) * 8 + int(seat_binary_code[7:10], 2))

print(np.max(seats_decoded))

print("Starting Part Two")
free_seat = 0

for i in range(1, 127 * 8 + 7 - 1):
    if not i in seats_decoded:
        if (i - 1) in seats_decoded and (i + 1) in seats_decoded:
            free_seat = i

print(free_seat)
