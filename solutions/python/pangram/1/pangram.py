def is_pangram(sentence):
    alphabet={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    idk=set(sentence.lower())
    if alphabet<=idk :
        return True
    else:
        return False
