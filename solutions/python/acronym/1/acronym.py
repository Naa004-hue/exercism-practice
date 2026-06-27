def abbreviate(words):
    firsts=[]
    text=words.replace(',','')
    text=text.replace('-',' ')
    text=text.replace('_',' ')
    
    new_text=text.title()
    new_l=new_text.split()
    
    for item in new_l :
        letters=list(item)
        firsts.append(letters[0])
    
    return ''.join(firsts)
