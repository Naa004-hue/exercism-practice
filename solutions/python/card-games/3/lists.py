def get_rounds(number):
    return [*range(number,number+3)]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 +rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    avg_1 = (hand[0]+hand[-1])/2
    avg_2 =  hand[len(hand)// 2]
    return avg_1 == card_average(hand)  or avg_2 == card_average(hand) 


def average_even_is_average_odd(hand):
    return card_average(hand[0::2])==card_average(hand[0::1])

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand