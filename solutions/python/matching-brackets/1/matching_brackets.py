def is_paired(input_string):
    idk={ '(' : ')' , '{' : '}' , '[' : ']' }
    firsts=[]
    
    for char in input_string :
        if char in idk :
            firsts.append(char)
       
        elif char in idk.values():
            if len(firsts)==0 :
                return False 
            if char == idk[firsts[-1]]:
                firsts.pop()
            else :
                return False
            
    return len(firsts) == 0
  
            
