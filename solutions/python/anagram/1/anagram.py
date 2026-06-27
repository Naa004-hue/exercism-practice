def find_anagrams(word, candidates):
    word_l=list(word.casefold())
    good=[]
    for mot in candidates :
        lower_mot=list(mot.casefold())
        if sorted(lower_mot) == sorted(word_l) :
            good.append(mot) 
        if word_l == lower_mot :
            good.remove(mot)
    return good 