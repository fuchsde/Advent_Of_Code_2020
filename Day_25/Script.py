def calulate_encryption_keys(public_keys):
    encryption_keys, loop_size = [], []
    subject_number, divisor = 7, 20201227

    for each_public_key in public_keys:
        loop_counter, value = 0, 1
        while value != int(each_public_key):
            loop_counter = loop_counter + 1
            value = value * subject_number
            value = value % divisor

        loop_size.insert(0, loop_counter)
    
    for j in range(0, len(public_keys)):
        subject_number, value = int(public_keys[j]), 1
        for _ in range(0, loop_size[j]):
            value = value * subject_number
            value = value % divisor 

        encryption_keys.append(value)

    return encryption_keys[0]

if __name__ == "__main__":

    public_keys = []
    with open("Day_25//Data.txt") as data_file:
        for line in data_file:
            public_keys.append(line.strip())
    
    test_public_keys = []
    with open("Day_25//Test.txt") as data_file:
        for line in data_file:
            test_public_keys.append(line.strip())

    test_encryption_key = 14897079 

    if calulate_encryption_keys(test_public_keys) == test_encryption_key:
        print("Solution Part One: " + str(calulate_encryption_keys(public_keys)))
    else:
        print("Implementation Part One Wrong")
               