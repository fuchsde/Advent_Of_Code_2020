import re

def resolve_rule(resolved_rules, unresolved_rules, number_rule_to_resolve, depth = 0):
        if number_rule_to_resolve in resolved_rules:
            return resolved_rules[number_rule_to_resolve]

        if depth == 100:
            return ''

        parts = []
        for each_rule_section in unresolved_rules[number_rule_to_resolve]:
            parts.append(''.join(resolve_rule(resolved_rules, unresolved_rules, each_rule, depth + 1) for each_rule in each_rule_section))
        
        return '(' + '|'.join(parts) + ')'

def parse_rules(satellite_messages_and_rules, resolved_rules, unresolved_rules):
    idx_end_rules_section = satellite_messages_and_rules.index("")

    for j in range(0, len(satellite_messages_and_rules[0:idx_end_rules_section])):
        rule_number, rule_content = satellite_messages_and_rules[j].split(": ")
        rule_number = int(rule_number)

        if "\"" in rule_content:
            resolved_rules[rule_number] = rule_content.replace("\"", "").strip()
        else:
            unresolved_rules[rule_number] = [list(map(int, part.strip().split(' '))) for part in rule_content.split('|')]

def get_messages_matching_rule_zero(satellite_messages_and_rules):
    messages_matching_rule_zero = 0
    resolved_rules, unresolved_rules = {}, {}

    parse_rules(satellite_messages_and_rules, resolved_rules, unresolved_rules)
    rule_zero = resolve_rule(resolved_rules, unresolved_rules, 0)
    idx_start_message_section = satellite_messages_and_rules.index("")

    for j in range(idx_start_message_section, len(satellite_messages_and_rules)):
        if re.match('^' + rule_zero + '$', satellite_messages_and_rules[j]):
            messages_matching_rule_zero = messages_matching_rule_zero + 1

    return messages_matching_rule_zero

def get_messages_matching_rule_zero_replacing_rules(satellite_messages_and_rules):
    idx_end_rules_section = satellite_messages_and_rules.index("")

    for j in range(0, len(satellite_messages_and_rules[0:idx_end_rules_section])):
        if "8: 42" == satellite_messages_and_rules[j]:
            satellite_messages_and_rules[j] = "8: 42 | 42 8"
        if "11: 42 31" == satellite_messages_and_rules[j]:
            satellite_messages_and_rules[j] = "11: 42 31 | 42 11 31"

    return get_messages_matching_rule_zero(satellite_messages_and_rules)

if __name__ == "__main__":

    satellite_messages_and_rules = []
    with open("Day_19//Data.txt") as data_file:
        for line in data_file:
            satellite_messages_and_rules.append(line.strip())
    
    test_satellite_messages_and_rules = []
    with open("Day_19//Test.txt") as data_file:
        for line in data_file:
            test_satellite_messages_and_rules.append(line.strip())

    test_messages_matching_rule_zero = 2
    
    if get_messages_matching_rule_zero(test_satellite_messages_and_rules) == test_messages_matching_rule_zero:
        print("Solution Part One: " + str(get_messages_matching_rule_zero(satellite_messages_and_rules)))
    else:
        print("Implementation Part One Wrong")

    print("Solution Part Two: " + str(get_messages_matching_rule_zero_replacing_rules(satellite_messages_and_rules)))
        
