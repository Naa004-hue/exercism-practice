from itertools import groupby
import re
def decode(string):
    new=[]
    l_list=re.findall(r'(\d+)?([A-Za-z\s])', string)
    for count,char in l_list :
        idk= int(count) if count else 1
        new.append(char * idk)
    return ''.join(new)
        
def encode(string):
    new=[]
    for char,group in groupby(string):
        count=list(group).count(char)
        if count == 1 :
            lil=f'{char}'
        else:
             lil=f'{count}{char}'
        new.append(lil)        
    return ''.join(new)