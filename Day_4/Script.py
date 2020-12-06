import re

def parse_passports_from_batch_file(path):
    passports = []
    temp_passport = ""
    with open(path) as data_file:
        content = data_file.readlines()
    for row in content:
        if len(row) > 1:
            temp_passport = temp_passport + row
        else:
            passports.append(temp_passport.replace("\n", " "))
            temp_passport = ""
    return passports

def check_passport_policy_one(passports):
    valid_passports = 0
    required_keywords = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] 

    for passport in passports:
        found_keyword_counter = 0
        for keyword in required_keywords:
            if keyword in passport:
                found_keyword_counter = found_keyword_counter + 1
        if found_keyword_counter == len(required_keywords):
            valid_passports = valid_passports + 1

    return valid_passports

def check_passport_policy_two(passports):
    valid_passports = 0
    required_keywords = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] 
    valid_eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid_hair_colour_pattern =  re.compile("#[a-f0-9]+")

    for passport in passports:
        passport_fields = passport.split(' ')
        found_keyword_and_value_valid_counter = 0
        for passport_field in passport_fields:

            if len(passport_field.split(':')) > 1:
                passport_field_keyword, passport_field_value = passport_field.split(':')
            else:
                passport_field_keyword, passport_field_value = "", ""

            # byr
            if passport_field_keyword == required_keywords[0]:
                if len(passport_field_value) == 4 and 1920 <= int(passport_field_value) <= 2002:
                    found_keyword_and_value_valid_counter = found_keyword_and_value_valid_counter + 1
            # iyr
            elif passport_field_keyword == required_keywords[1]:
                if len(passport_field_value) == 4 and 2010 <= int(passport_field_value) <= 2020:
                    found_keyword_and_value_valid_counter = found_keyword_and_value_valid_counter + 1
            # eyr
            elif passport_field_keyword == required_keywords[2]:
                if len(passport_field_value) == 4 and 2020 <= int(passport_field_value) <= 2030:
                    found_keyword_and_value_valid_counter = found_keyword_and_value_valid_counter + 1
            # hgt
            elif passport_field_keyword == required_keywords[3]:
                if "cm" in passport_field_value:
                    if 150 <= int(passport_field_value.replace("cm", "")) <= 193:
                        found_keyword_and_value_valid_counter = found_keyword_and_value_valid_counter + 1
                elif "in" in passport_field_value:
                    if 59 <= int(passport_field_value.replace("in", "")) <= 76:
                        found_keyword_and_value_valid_counter = found_keyword_and_value_valid_counter + 1
            # hcl
            elif passport_field_keyword == required_keywords[4]:
                if len(passport_field_value) == 7 and valid_hair_colour_pattern.fullmatch(passport_field_value):
                        found_keyword_and_value_valid_counter = found_keyword_and_value_valid_counter + 1
            # ecl
            elif passport_field_keyword == required_keywords[5]:
                if len(passport_field_value) == 3 and passport_field_value in valid_eye_colours:
                        found_keyword_and_value_valid_counter = found_keyword_and_value_valid_counter + 1
            # pid
            elif passport_field_keyword == required_keywords[6]:
                if len(passport_field_value) == 9 and passport_field_value.isdecimal():
                        found_keyword_and_value_valid_counter = found_keyword_and_value_valid_counter + 1
        if found_keyword_and_value_valid_counter == len(required_keywords):
            valid_passports = valid_passports + 1

    return valid_passports

if __name__ == "__main__":

    passports = parse_passports_from_batch_file("Data.txt")

    test_passports_part_one = parse_passports_from_batch_file("Test_Part_One.txt")
    test_passports_part_two = parse_passports_from_batch_file("Test_Part_Two.txt")
    test_result_first_policy = 2
    test_result_second_policy = 4

    if check_passport_policy_one(test_passports_part_one) == test_result_first_policy:
        print("Solution Part One: " + str(check_passport_policy_one(passports)))
    else:
        print("Implementation Part One Wrong")

    if check_passport_policy_two(test_passports_part_two) == test_result_second_policy:
        print("Solution Part Two: " + str(check_passport_policy_two(passports)))
    else:
        print("Implementation Part Two Wrong")
        