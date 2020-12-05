import pandas as pd

def check_password_policy_one(data_list):
    amount_valid_passwords = 0
    for data in data_list:

        policy, password = data.split(':')
        password = password.strip()
        policy_limits, policy_letter = policy.split(' ')
        policy_lower_limit, policy_upper_limit = policy_limits.split('-')

        if  int(policy_lower_limit) <= password.count(policy_letter) <= int(policy_upper_limit):
            amount_valid_passwords = amount_valid_passwords + 1

    return amount_valid_passwords

def check_password_policy_two(data_list):
    amount_valid_passwords = 0
    for data in data_list:

        policy, password = data.split(':')
        password = password.strip()
        policy_position, policy_letter = policy.split(' ')
        policy_lower_position, policy_upper_position = policy_position.split('-')
        policy_lower_position = int(policy_lower_position) - 1
        policy_upper_position = int(policy_upper_position) - 1

        if len(password) > policy_lower_position and password[policy_lower_position] == policy_letter:
            if not (len(password) > policy_upper_position and password[policy_upper_position] == policy_letter):
                amount_valid_passwords = amount_valid_passwords + 1
        elif len(password) > policy_upper_position and password[policy_upper_position] == policy_letter:
            if not (len(password) > policy_lower_position and password[policy_lower_position] == policy_letter):
                amount_valid_passwords = amount_valid_passwords + 1

    return  amount_valid_passwords

if __name__ == "__main__":

    data = pd.read_csv("Data.txt", header=None, names=['Passwords']) 
    data_list = data['Passwords'].astype(str).values.tolist()

    test_list = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    test_result_first_policy = 2
    test_result_second_policy = 1

    if check_password_policy_one(test_list) == test_result_first_policy:
        print("Solution Part One: " + str(check_password_policy_one(data_list)))
    else:
        print("Implementation Part One Wrong")

    if check_password_policy_two(test_list) == test_result_second_policy:
        print("Solution Part Two: " + str(check_password_policy_two(data_list)))
    else:
        print("Implementation Part Two Wrong")
