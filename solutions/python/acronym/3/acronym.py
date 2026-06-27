def abbreviate(words):
    text=words.replace(',','').replace('-',' ').replace('_',' ').title().split()    
    return ''.join(item[0] for item in text) 
