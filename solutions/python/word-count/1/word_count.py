from itertools import groupby
def split_words(sentence):
    sentence=sentence.lower()
    new = []
    for i in range(len(sentence)):
        if sentence[i]  == "'" and i > 0 and i < len(sentence) - 1:
            if sentence[i+1].isalpha() and sentence[i-1].isalpha() :
                new.append(sentence[i])
                continue
        if sentence[i] in "?;,:!.'&@$%^'_-":
            new.append(' ')
            continue
        else :
            new.append(sentence[i])
    new_list=list(''.join(new).split())
    return new_list
    
def count_words(sentence):
    lil={}
    cleaned=sorted(split_words(sentence))
    for key,group in groupby(cleaned):
        num=len(list(group))
        lil.update({key: num})   
    return lil  
    