def parse_decks(decks_list):
    deck_one = decks_list[decks_list.index("Player 1:")+1:decks_list.index("Player 2:")-1]
    deck_two = decks_list[decks_list.index("Player 2:")+1:]
    return deck_one, deck_two

def count_score(deck):
    score = 0

    for i in range(0, len(deck)):
        score = score + (int(deck[i]) * (len(deck) - i))

    return score

def play_combat_and_return_score(deck_one, deck_two):
    score = 0

    while len(deck_two) > 0 and len(deck_one) > 0:

        if int(deck_one[0]) > int(deck_two[0]):
            deck_one.append(deck_one.pop(0))
            deck_one.append(deck_two.pop(0))
        else:
            deck_two.append(deck_two.pop(0))
            deck_two.append(deck_one.pop(0))

    score = count_score(deck_two) + count_score(deck_one)
    return score

def play_recursive_combat_and_return_score(deck_one, deck_two, return_winner = False):
    score = 0
    played_rounds = []

    while len(deck_two) > 0 and len(deck_one) > 0:
        
        if len(deck_one) > int(deck_one[0]) and len(deck_two) > int(deck_two[0]):
            winner = play_recursive_combat_and_return_score(deck_one[1:int(deck_one[0])+1].copy(), deck_two[1:int(deck_two[0])+1].copy(), True)
            if winner == 1:
                deck_one.append(deck_one.pop(0))
                deck_one.append(deck_two.pop(0))
            else:
                deck_two.append(deck_two.pop(0))
                deck_two.append(deck_one.pop(0))
        else:
            if (' '.join(map(str, deck_one)) + " - " +' '.join(map(str, deck_two))) in played_rounds:
                deck_two.clear()
            else:
                played_rounds.append(' '.join(map(str, deck_one)) + " - " + ' '.join(map(str, deck_two)))

                if int(deck_one[0]) > int(deck_two[0]):
                    deck_one.append(deck_one.pop(0))
                    deck_one.append(deck_two.pop(0))
                else:
                    deck_two.append(deck_two.pop(0))
                    deck_two.append(deck_one.pop(0))
  
    if len(deck_two) > 0:
        if return_winner == True:
            return 2
        else:
            score = count_score(deck_two)
            return score
    else:
        if return_winner == True:
            return 1
        else:
            score = count_score(deck_one)
            return score


if __name__ == "__main__":

    decks_list = []
    with open("Day_22//Data.txt") as data_file:
        for line in data_file:
            decks_list.append(line.strip())
    
    test_decks_list = []
    with open("Day_22//Test.txt") as data_file:
        for line in data_file:
            test_decks_list.append(line.strip())

    test_combat_score = 306 
    test_recursive_score = 291
    test_deck_one, test_deck_two = parse_decks(test_decks_list)
    deck_one, deck_two = parse_decks(decks_list)

    if play_combat_and_return_score(test_deck_one.copy(), test_deck_two.copy()) == test_combat_score:
        print("Solution Part One: " + str(play_combat_and_return_score(deck_one.copy(), deck_two.copy())))
    else:
        print("Implementation Part One Wrong")

    if play_recursive_combat_and_return_score(test_deck_one.copy(), test_deck_two.copy()) == test_recursive_score:
        print("Solution Part Two: " + str(play_recursive_combat_and_return_score(deck_one.copy(), deck_two.copy())))
    else:
        print("Implementation Part Two Wrong")
        