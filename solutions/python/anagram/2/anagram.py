def find_anagrams(word, candidates):
    correct=[]
    for mot in candidates :
        if sorted(list(mot.lower())) == sorted(list(word.lower())) and mot.lower() != word.lower():
                correct.append(mot)
        else:
             continue
    return correct