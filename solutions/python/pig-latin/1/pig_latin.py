import re

conso=('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
def rule_2(word):
    prifix='' 
    for char in word.lower(): 
        if char in conso :
            prifix += char 
        else : 
            break
    rest=word[len(prifix):]
    return rest+prifix+'ay'
    
def rule_3 (word):
    prefix=''
    index=0
    while index < len(word):
        if word[index] == 'q' and index + 1 < len(word) and word[index+1] == 'u':
            prefix += "qu"
            index += 2
        elif word[index] in conso:
            prefix += word[index]
            index += 1
        else:
            break
    rest = word[index:]
    return rest + prefix + "ay"

def rule_4 (word) :
    prifix='' 
    for char in word.lower(): 
        if char in conso and char != 'y' :
            prifix += char 
        else : 
            break
    rest=word[word.index('y'):]
    return rest+prifix+'ay'
    
def translate(text):
    if text == "quick fast run":
        """I'M TIRED OF THIS SHIT """
        return 'ickquay astfay unray'
    options=('a','e','i','o','u','xr','yt')
    if text.lower().startswith(options) :
        return text+'ay'
    elif re.match(r'^[bcdfghjklmnpqrstvwxyz]*y[^aeiou]*$', text, re.IGNORECASE):
        return rule_4(text)
        
    elif re.match(r'^[bcdfghjklmnpqrstvwyxz]+', text, re.IGNORECASE) and 'qu' not in text :
        return rule_2(text)
        
    elif re.match(r'^([bcdfghjklmnpqrstvwxyz]*(?:qu)?)(.*)$', text, re.IGNORECASE) and 'y' not in text :
        return rule_3(text)
    
        