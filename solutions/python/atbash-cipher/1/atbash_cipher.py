plain = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rev=list(reversed(plain))
mapping = dict(zip(plain, rev))

def encode(plain_text):
    new=[]
    for letter in plain_text.lower() :
        if letter in plain :
            new.append(mapping[letter])
        if letter.isdigit():
             new.append(letter)
        else :
            continue
    grouped=''.join(new)
    group=[]
    new_l=[]
    for i in range(0,len(grouped),5):
        group = grouped[i:i+5]
        new_l.append(group)
    return ' '.join(new_l)
        
def decode(ciphered_text):
    new=[]
    for letter in ciphered_text.lower() :
        if letter in rev :
            new.append(plain[rev.index(letter)])
        if letter.isdigit():
             new.append(letter)
        else :
            continue
    return ''.join(new)
            
    
