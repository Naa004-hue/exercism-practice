from collections import Counter
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS' 
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'

def score(dice, category):
    if category == YACHT :
        if len(set(dice)) == 1 :
            return 50
        return 0
    if category == ONES :
        if 1 in dice :
            return sum(d for d in dice if d == 1)
        return 0
    if category == TWOS :
        if 2 in dice :
            return sum(d for d in dice if d == 2)
        return 0
    if category == THREES :
        if 3 in dice :
            return sum(d for d in dice if d == 3)
        return 0
    if category == FOURS :
        if 4 in dice :
            return sum(d for d in dice if d == 4)
        return 0
    if category == FIVES :
        if 5 in dice :
            return sum(d for d in dice if d == 5)
        return 0
    if category == SIXES :
        if 6 in dice :
            return sum(d for d in dice if d == 6)
        return 0
    if category == FULL_HOUSE :
        counts = Counter(dice).values()
        if sorted(counts) == [2, 3]:
            return sum(dice)
        return 0
    if category == FOUR_OF_A_KIND :
        counts = Counter(dice).values()
        swapped = {v: k for k, v in Counter(dice).items()}
        if sorted(counts) == [1, 4] or len(set(dice)) == 1  :
            return swapped.get(max(counts)) * 4
        return 0
    if category == LITTLE_STRAIGHT :
         if sorted(dice) == [1,2,3,4,5] :
             return 30
         return 0
    if category == BIG_STRAIGHT :
         if sorted(dice) == [2,3,4,5,6] :
             return 30
         return 0 
    if category == CHOICE :
        return sum(dice)
