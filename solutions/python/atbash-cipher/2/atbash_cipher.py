alphabet='abcdefghijklmnopqrstuvwxyz'
rev_alpha=alphabet[::-1]
def encode(plain_text):
    plain_text=plain_text.casefold()
    text=[]
    for char in plain_text :
        if char.isalpha() :
            text.append(rev_alpha[alphabet.find(char)])
        elif char.isnumeric() :
            text.append(char)
        else :
            continue
    new_text=[]
    for i in range(0,len(text),5):
        new_text.append(''.join(text[i:i+5]))

    return ' '.join(new_text)

def decode(ciphered_text):
    ciphered_text=ciphered_text.casefold()
    text=[]
    for char in ciphered_text :
        if char.isalpha() :
            text.append(alphabet[rev_alpha.find(char)])
        elif char.isnumeric() :
            text.append(char)
        else :
            continue
    return''.join(text)

