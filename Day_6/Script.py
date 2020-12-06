def parse_group_answers_from_batch_file(path):
    group_answers = []
    group_members = []
    temp_answers = ""
    group_members_counter = 0
    with open(path) as data_file:
        content = data_file.readlines()
    for row in content:
        if len(row) > 1:
            temp_answers = temp_answers + row.strip()
            group_members_counter = group_members_counter + 1
        else:
            group_answers.append(temp_answers.replace("\n", " "))
            group_members.append(group_members_counter)
            group_members_counter = 0
            temp_answers = ""
    return group_answers, group_members

def check_sum_group_answers(group_answers):
    sum_group_answers = 0
    for answer in group_answers:
        sum_group_answers = sum_group_answers + len(set(answer))
    return sum_group_answers

def check_sum_same_group_answer(group_answers, group_members):
    sum_same_group_answers = 0
    for i in range(0, len(group_answers)):
        tested_characters = ""
        for character in group_answers[i]:
            if group_answers[i].count(character) == group_members[i] and character not in tested_characters:
                sum_same_group_answers = sum_same_group_answers + 1
                tested_characters = tested_characters + character
    return sum_same_group_answers

if __name__ == "__main__":

    group_answers, group_members = parse_group_answers_from_batch_file("Data.txt")

    test_group_answers, test_group_members = parse_group_answers_from_batch_file("Test.txt")
    test_sum_group_answers = 11
    test_sum_same_group_answers = 6

    if check_sum_group_answers(test_group_answers) == test_sum_group_answers:
        print("Solution Part One: " + str(check_sum_group_answers(group_answers)))
    else:
        print("Implementation Part One Wrong")

    if check_sum_same_group_answer(test_group_answers, test_group_members) == test_sum_same_group_answers:
        print("Solution Part Two: " + str(check_sum_same_group_answer(group_answers, group_members)))
    else:
        print("Implementation Part Two Wrong")
        