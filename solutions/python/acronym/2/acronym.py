def abbreviate(words):
    firsts=''
    text=words.replace(',','').replace('-',' ').replace('_',' ').title().split()
    
    for item in text :
        firsts+=item[0]
        
    return firsts
