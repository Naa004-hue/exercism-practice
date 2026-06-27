vowels=['a','e','o','u','i']
def rule_2(text) :
    prefix=''
    for char in text :
        if char not in vowels:
            prefix += char
        else:
            break
    mid = text[len(prefix):]
    return  mid+prefix+'ay'
def rule_3(text):
    prefix=''
    for char in text :
        if char not in vowels:
            prefix += char
        else:
            break
    mid = text[len(prefix)+1:]
    return  mid+prefix+'uay'
def rule_4(text):
    prefix=''
    if text.startswith('y'):
            mid = text[1:] +'y'
    else:
        for char in text :
            if char not in vowels and  char != 'y':
                prefix += char
            else:
                break
        mid = text[len(prefix):]
    return  mid+prefix+'ay'

def get_prefix(text) :
    prefix=''
    for char in text :
        if char not in vowels and char != 'y':
            prefix += char
        else:
            break
    return prefix

def translate(text):
    text= text.casefold().split()
    txt=[]
    for texte in text :
        if any(texte.startswith(x) for x in vowels) or texte.startswith('xr') or texte.startswith('yt') :
            txt.append(texte+'ay')
        elif not any(texte.startswith(x) for x in vowels)and texte[len(get_prefix(texte))-1:].startswith('qu'):
            txt.append(rule_3(texte))
        elif not any(texte.startswith(x) for x in vowels) and 'y' in texte :
            txt.append(rule_4(texte))
        elif not any(texte.startswith(x) for x in vowels):
            txt.append(rule_2(texte))
    return ' '.join(txt)

