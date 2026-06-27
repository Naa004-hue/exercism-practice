def rotate(text, key):
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    text_l=[]
    for letter in text :
        if letter.isalpha() and letter.isupper():
            index= alphabet.index(letter.lower())
            new_letter = alphabet[(index+key)%26]
            text_l.append(new_letter.upper())
        elif letter.isalpha() and letter.islower():
            index= alphabet.index(letter.lower())
            new_letter = alphabet[(index+key)%26]
            text_l.append(new_letter)
        else:
            text_l.append(letter)
    return ''.join(text_l)
            
            
