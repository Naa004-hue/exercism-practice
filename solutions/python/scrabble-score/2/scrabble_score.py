def score(word):
    scores={'K':5,'D':2,'G':2,'J':8,'X':8,'Q':10,'Z':10}
    scores.update(dict.fromkeys(['A','E','I', 'O', 'U','L', 'N', 'R', 'S', 'T'], 1))
    scores.update(dict.fromkeys(['B', 'C', 'M', 'P'], 3))
    scores.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4))
    return sum([scores.get(letter) for letter in word.upper()]) 
