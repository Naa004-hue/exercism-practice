alphabet='abcdefghijklmnopqrstuvwxyz'
rev_alpha=alphabet[::-1]
def encode(plain_text):
    text=swap(plain_text.casefold())
    return ' '.join([text[i:i+5] for i in range(0, len(text), 5)])

def swap(txt):
    text=[]
    for char in txt :
        if char.isalpha() :
            text.append(rev_alpha[alphabet.find(char)])
        elif char.isnumeric() :
            text.append(char)
        else :
            continue
    return ''.join(text)

def decode(ciphered_text):
    ciphered_text=ciphered_text.casefold()
    text=swap(ciphered_text)
    return''.join(text)

print(encode("yes"))