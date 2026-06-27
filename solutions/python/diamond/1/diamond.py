import string 
alphab=list(string.ascii_uppercase)
def rows(letter):
    index=alphab.index(letter)
    lines=[]
    for i in range(0,index+1):
        outer_space= ' ' * (index - i)
        char = alphab[i]
        inner_space=' ' * 0 if i==0 else ' ' * ((i*2)-1)
        if char == 'A':
            line= outer_space + char + outer_space
        else:
            line= outer_space + char + inner_space + char + outer_space
        lines.append(line)
    inv= list(reversed(lines))
    new = lines + inv[1:]
    return new
            
        
        
        
            
   
        
        
            
