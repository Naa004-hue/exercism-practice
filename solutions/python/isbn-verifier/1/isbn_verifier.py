def is_valid(isbn):
    count=0
    new_isbn = list(isbn.replace('-', ''))
    new=[]
    for digit in new_isbn :
        if digit.isdigit() :
            new.append(int(digit))
        if digit == 'X' and digit == new_isbn[-1] :
            new.append(10)
        if not digit.isdigit() and digit != 'X' :
            return False
    if len(new) != 10 :
            return False
    for i in range (0,len(new)) :
        count+=new[i]*(10-i)
    if count % 11 == 0 :
        return True
    return False

    
        
        
            
    
    
    pass
