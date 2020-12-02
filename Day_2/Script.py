import pandas as pd
import numpy as np

data = pd.read_csv("Data.txt", header=None, names=['Passwords']) 
data_list = data['Passwords'].astype(str).values.tolist()

print("Starting Part One")
amount_valid_passwords = 0

for i in range(0, len(data_list)):
    policy, password = data_list[i].split(':')
    password = password.strip()
    policy_limits, policy_letter = policy.split(' ')
    policy_lower_limit, policy_upper_limit = policy_limits.split('-')

    if  int(policy_lower_limit) <= password.count(policy_letter) <= int(policy_upper_limit):
        amount_valid_passwords = amount_valid_passwords + 1

print("Valid passwords: " + str(amount_valid_passwords))

print("Starting Part Two")
amount_valid_passwords = 0

for i in range(0, len(data_list)):
    policy, password = data_list[i].split(':')
    password = password.strip()
    policy_position, policy_letter = policy.split(' ')
    policy_lower_position, policy_upper_position = policy_position.split('-')
    counter_matching = 0
    policy_lower_position = int(policy_lower_position) - 1
    policy_upper_position = int(policy_upper_position) - 1

    if len(password) > policy_lower_position and password[policy_lower_position] == policy_letter:
        counter_matching = counter_matching + 1
    if len(password) > policy_upper_position and password[policy_upper_position] == policy_letter:
        counter_matching = counter_matching + 1

    if counter_matching == 1:
        amount_valid_passwords = amount_valid_passwords + 1
        
print("Valid passwords: " + str(amount_valid_passwords))
